#!/usr/bin/env python3
"""
Card news generator for hospital blog posts.

Usage:
    python generate_cards.py --hospital "연세위드유외과" --input manuscript.txt
    python generate_cards.py --hospital "이끌림이비인후과" --input manuscript.docx
    python generate_cards.py  # interactive mode
"""

import argparse
import base64
import json
import os
import re
import sys
import textwrap
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("[오류] playwright가 설치되지 않았습니다. 아래 명령어로 설치해주세요:")
    print("  pip install playwright")
    print("  playwright install chromium")
    sys.exit(1)

try:
    import docx
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# ---------------------------------------------------------------------------
# Project-local imports
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from templates.card_templates import build_card_html
from assets.clipart.medical_icons import get_icon_by_text

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
OUTPUT_BASE = Path(r"C:\Users\Q\Desktop\병원 카드뉴스")
HOSPITALS_JSON = ROOT / "config" / "hospitals.json"


def load_hospital_cfg(hospital_name: str) -> dict:
    with open(HOSPITALS_JSON, encoding="utf-8") as f:
        data = json.load(f)
    hospitals = data["hospitals"]
    cfg = hospitals.get(hospital_name) or hospitals.get("기본병원")
    cfg = dict(cfg)
    cfg["name"] = hospital_name
    return cfg


def load_logo_b64(cfg: dict) -> str:
    logo_path = cfg.get("logo", "")
    if not logo_path:
        return ""
    full_path = ROOT / logo_path
    if not full_path.exists():
        return ""
    ext = full_path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "svg": "image/svg+xml", "webp": "image/webp"}.get(ext, "image/png")
    data = base64.b64encode(full_path.read_bytes()).decode()
    return f"data:{mime};base64,{data}"


# ---------------------------------------------------------------------------
# Manuscript parsing
# ---------------------------------------------------------------------------

def read_manuscript(path: str) -> str:
    p = Path(path)
    if p.suffix.lower() == ".docx":
        if not DOCX_AVAILABLE:
            print("[오류] python-docx가 필요합니다: pip install python-docx")
            sys.exit(1)
        doc = docx.Document(str(p))
        return "\n".join(para.text for para in doc.paragraphs)
    return p.read_text(encoding="utf-8")


def parse_manuscript(text: str) -> dict:
    """
    Parse free-form manuscript text into structured card data.

    Supports explicit markers:
        [제목] 유방암
        [부제] 조기 발견이 중요합니다
        [카드1] 대표적인 증상
        - 유방에서 만져지는 멍울
        - 유방 모양의 변화
        [카드2] ...

    Falls back to auto-splitting when markers are absent.
    """
    result = {"title": "", "subtitle": "", "cards": []}

    # -- Try structured markers --
    title_m = re.search(r"\[제목\]\s*(.+)", text)
    sub_m = re.search(r"\[부제\]\s*(.+)", text)
    if title_m:
        result["title"] = title_m.group(1).strip()
    if sub_m:
        result["subtitle"] = sub_m.group(1).strip()

    card_blocks = re.findall(
        r"\[카드\d*\]\s*(.+?)\n((?:[-•*]\s*.+\n?)*)",
        text, re.MULTILINE
    )
    for heading, body in card_blocks:
        items = re.findall(r"[-•*]\s*(.+)", body)
        result["cards"].append({"heading": heading.strip(), "items": items})

    if result["title"] and result["cards"]:
        return result

    # -- Auto-split fallback --
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
    if not lines:
        return result

    if not result["title"]:
        result["title"] = lines[0]
        lines = lines[1:]

    # Group remaining lines into up to 4 content cards (~3-4 items each)
    ITEMS_PER_CARD = 4
    MAX_CARDS = 4

    current_heading = ""
    current_items: list[str] = []

    def flush():
        if current_items:
            result["cards"].append({
                "heading": current_heading or f"내용 {len(result['cards'])+1}",
                "items": current_items[:]
            })

    for line in lines:
        # Lines that look like headings (short, no punctuation ending)
        is_heading = (
            len(line) <= 20
            and not line.endswith((".", ",", "?", "!", "다", "요", "죠"))
            and not line.startswith(("-", "•", "*", "·"))
        )
        if is_heading and len(result["cards"]) < MAX_CARDS:
            flush()
            current_heading = line
            current_items = []
        else:
            clean = re.sub(r"^[-•*·]\s*", "", line)
            current_items.append(clean)
            if len(current_items) >= ITEMS_PER_CARD and len(result["cards"]) < MAX_CARDS - 1:
                flush()
                current_heading = ""
                current_items = []

    flush()

    # Ensure at least one card
    if not result["cards"] and lines:
        chunks = [lines[i:i+ITEMS_PER_CARD] for i in range(0, len(lines), ITEMS_PER_CARD)]
        for idx, chunk in enumerate(chunks[:MAX_CARDS]):
            result["cards"].append({"heading": f"내용 {idx+1}", "items": chunk})

    return result


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def html_to_png(html: str, output_path: Path, playwright_page) -> None:
    playwright_page.set_content(html, wait_until="networkidle")
    playwright_page.set_viewport_size({"width": 800, "height": 800})
    playwright_page.screenshot(path=str(output_path), full_page=False)


def generate(hospital_name: str, manuscript_text: str, output_dir: Path | None = None) -> list[Path]:
    cfg = load_hospital_cfg(hospital_name)
    logo_b64 = load_logo_b64(cfg)
    template = cfg.get("template", "clean")
    parsed = parse_manuscript(manuscript_text)

    title = parsed["title"] or "제목 없음"
    subtitle = parsed["subtitle"] or ""
    cards = parsed["cards"][:4]  # max 4 content cards

    total_cards = 1 + len(cards)  # thumbnail + content

    # Determine output folder
    if output_dir is None:
        date_str = datetime.now().strftime("%Y%m%d")
        safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)[:20]
        output_dir = OUTPUT_BASE / hospital_name / f"{date_str}_{safe_title}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Pick clipart icon based on full text
    icon_svg = get_icon_by_text(manuscript_text)

    saved: list[Path] = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Card 1: Thumbnail
        html = build_card_html(
            template, "thumbnail", cfg,
            title=title,
            subtitle=subtitle,
            icon_svg=icon_svg,
            logo_b64=logo_b64,
        )
        out = output_dir / "card_01_thumbnail.png"
        html_to_png(html, out, page)
        saved.append(out)
        print(f"  ✓ {out.name}")

        # Cards 2-5: Content
        for i, card in enumerate(cards, 2):
            heading = card["heading"]
            items = card["items"]
            card_icon = get_icon_by_text(heading + " " + " ".join(items))
            html = build_card_html(
                template, "content", cfg,
                card_num=i - 1,
                total=len(cards),
                heading=heading,
                body_items=items,
                icon_svg=card_icon,
                logo_b64=logo_b64,
            )
            out = output_dir / f"card_{i:02d}.png"
            html_to_png(html, out, page)
            saved.append(out)
            print(f"  ✓ {out.name}")

        browser.close()

    print(f"\n카드뉴스 생성 완료! ({len(saved)}장)")
    print(f"저장 위치: {output_dir}")
    return saved


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def interactive_mode():
    print("=" * 50)
    print("  병원 카드뉴스 생성기")
    print("=" * 50)

    with open(HOSPITALS_JSON, encoding="utf-8") as f:
        data = json.load(f)
    hospital_list = list(data["hospitals"].keys())
    print("\n등록된 병원 목록:")
    for i, h in enumerate(hospital_list, 1):
        print(f"  {i}. {h}")

    choice = input("\n병원 번호 또는 이름을 입력하세요: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        hospital = hospital_list[idx] if 0 <= idx < len(hospital_list) else hospital_list[-1]
    else:
        hospital = choice

    print(f"\n선택된 병원: {hospital}")
    print("\n원고 입력 방법을 선택하세요:")
    print("  1. 파일 경로 입력 (.txt 또는 .docx)")
    print("  2. 직접 텍스트 입력")

    method = input("선택 (1/2): ").strip()
    if method == "1":
        path = input("파일 경로: ").strip().strip('"')
        text = read_manuscript(path)
    else:
        print("원고를 입력하세요 (입력 완료 후 빈 줄에서 Ctrl+Z 또는 Ctrl+D):")
        lines = []
        try:
            while True:
                lines.append(input())
        except EOFError:
            pass
        text = "\n".join(lines)

    print(f"\n[{hospital}] 카드뉴스 생성 중...")
    generate(hospital, text)


def main():
    parser = argparse.ArgumentParser(description="병원 카드뉴스 자동 생성기")
    parser.add_argument("--hospital", "-H", help="병원 이름")
    parser.add_argument("--input", "-i", help="원고 파일 경로 (.txt 또는 .docx)")
    parser.add_argument("--text", "-t", help="원고 텍스트 직접 입력")
    parser.add_argument("--output", "-o", help="출력 폴더 경로 (기본: 바탕화면)")
    args = parser.parse_args()

    if not args.hospital and not args.input and not args.text:
        interactive_mode()
        return

    if not args.hospital:
        print("[오류] --hospital 옵션이 필요합니다.")
        sys.exit(1)

    if args.input:
        text = read_manuscript(args.input)
    elif args.text:
        text = args.text
    else:
        print("[오류] --input 또는 --text 옵션이 필요합니다.")
        sys.exit(1)

    output_dir = Path(args.output) if args.output else None
    generate(args.hospital, text, output_dir)


if __name__ == "__main__":
    main()
