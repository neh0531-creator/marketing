#!/usr/bin/env python3
"""
병원 템플릿 추가/수정 도우미

Usage:
    python add_hospital.py
"""

import json
from pathlib import Path

HOSPITALS_JSON = Path(__file__).parent / "config" / "hospitals.json"
TEMPLATE_CHOICES = ["notebook", "clean"]


def hex_input(prompt: str, default: str) -> str:
    val = input(f"{prompt} [{default}]: ").strip()
    if not val:
        return default
    if not val.startswith("#"):
        val = "#" + val
    return val


def main():
    print("=" * 45)
    print("  병원 템플릿 추가/수정")
    print("=" * 45)

    with open(HOSPITALS_JSON, encoding="utf-8") as f:
        data = json.load(f)

    name = input("\n병원 이름 (예: 연세위드유외과): ").strip()
    if not name:
        print("이름을 입력해주세요.")
        return

    existing = data["hospitals"].get(name, {})

    print("\n--- 색상 설정 (HEX 코드, 기본값 그대로 두려면 Enter) ---")
    primary   = hex_input("주색상 (primary_color)",   existing.get("primary_color",   "#2E86AB"))
    secondary = hex_input("보조색상 (secondary_color)", existing.get("secondary_color", "#A8DADC"))
    bg        = hex_input("배경색 (background_color)", existing.get("background_color","#F0F8FF"))
    text_col  = hex_input("텍스트색 (text_color)",     existing.get("text_color",      "#1A2E3A"))

    print("\n--- 템플릿 스타일 ---")
    for i, t in enumerate(TEMPLATE_CHOICES, 1):
        print(f"  {i}. {t}")
    t_input = input(f"선택 [{existing.get('template', 'clean')}]: ").strip()
    if t_input.isdigit() and 1 <= int(t_input) <= len(TEMPLATE_CHOICES):
        template = TEMPLATE_CHOICES[int(t_input) - 1]
    elif t_input in TEMPLATE_CHOICES:
        template = t_input
    else:
        template = existing.get("template", "clean")

    print("\n--- 로고 ---")
    logo_hint = existing.get("logo", f"assets/logos/{name}.png")
    logo = input(f"로고 파일 경로 [{logo_hint}]: ").strip()
    if not logo:
        logo = logo_hint

    data["hospitals"][name] = {
        "primary_color": primary,
        "secondary_color": secondary,
        "background_color": bg,
        "accent_color": "#FFFFFF",
        "text_color": text_col,
        "logo": logo,
        "template": template,
        "font": "Noto Sans KR"
    }

    with open(HOSPITALS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ '{name}' 설정이 저장되었습니다.")
    print(f"  로고 파일을 '{logo}' 경로에 넣어주세요.")


if __name__ == "__main__":
    main()
