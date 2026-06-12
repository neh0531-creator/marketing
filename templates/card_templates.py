"""
HTML/CSS card templates for card news generation.
Two template styles: 'notebook' (ring-binder style) and 'clean' (modern flat).
"""


def _base_styles(cfg: dict) -> str:
    p = cfg["primary_color"]
    s = cfg["secondary_color"]
    bg = cfg["background_color"]
    txt = cfg["text_color"]
    return f"""
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            width: 800px; height: 800px; overflow: hidden;
            background: {bg};
            font-family: 'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif;
            color: {txt};
        }}
        .primary {{ color: {p}; }}
        .bg-primary {{ background: {p}; }}
        .bg-secondary {{ background: {s}; }}
    """


def thumbnail_notebook(cfg: dict, title: str, subtitle: str, icon_svg: str, logo_b64: str) -> str:
    p = cfg["primary_color"]
    s = cfg["secondary_color"]
    bg = cfg["background_color"]
    txt = cfg["text_color"]
    logo_html = f'<img src="{logo_b64}" class="logo-img" alt="logo"/>' if logo_b64 else ""
    return f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
<style>
    {_base_styles(cfg)}
    body {{ background: {bg}; display: flex; flex-direction: column; }}
    .outer {{
        width: 800px; height: 800px;
        background: {bg};
        display: flex; align-items: center; justify-content: center;
        padding: 30px;
    }}
    .card {{
        width: 100%; height: 100%;
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.10);
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        position: relative;
        overflow: hidden;
        padding: 40px;
    }}
    .rings {{
        position: absolute; left: 0; top: 0; bottom: 0;
        width: 32px;
        display: flex; flex-direction: column;
        align-items: center; justify-content: space-evenly;
        background: {bg};
    }}
    .ring {{
        width: 22px; height: 22px;
        border-radius: 50%;
        border: 4px solid {p};
        background: white;
    }}
    .content {{
        margin-left: 32px;
        width: calc(100% - 32px);
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        gap: 24px;
    }}
    .title {{
        font-size: 72px; font-weight: 900;
        color: {p};
        text-align: center;
        line-height: 1.1;
        letter-spacing: -2px;
    }}
    .divider {{
        width: 80%; height: 2px;
        background: {s};
    }}
    .icon-wrap {{
        width: 280px; height: 280px;
        display: flex; align-items: center; justify-content: center;
    }}
    .icon-wrap svg {{ width: 100%; height: 100%; }}
    .footer {{
        position: absolute; bottom: 0; left: 0; right: 0;
        background: {p};
        height: 64px;
        display: flex; align-items: center; justify-content: center;
        gap: 16px;
        padding: 0 24px;
    }}
    .logo-img {{ height: 36px; object-fit: contain; filter: brightness(0) invert(1); }}
    .hospital-name {{
        color: white; font-size: 20px; font-weight: 700;
    }}
</style>
</head><body>
<div class="outer">
  <div class="card">
    <div class="rings">
      {''.join(['<div class="ring"></div>'] * 9)}
    </div>
    <div class="content">
      <div class="title">{title}</div>
      <div class="divider"></div>
      <div class="icon-wrap">{icon_svg}</div>
      {"<div style='color:" + txt + ";font-size:22px;text-align:center;opacity:0.7'>" + subtitle + "</div>" if subtitle else ""}
    </div>
    <div class="footer">
      {logo_html}
      <span class="hospital-name">{cfg.get('name', '')}</span>
    </div>
  </div>
</div>
</body></html>"""


def content_notebook(cfg: dict, card_num: int, total: int, heading: str,
                     body_items: list[str], icon_svg: str, logo_b64: str) -> str:
    p = cfg["primary_color"]
    s = cfg["secondary_color"]
    bg = cfg["background_color"]
    txt = cfg["text_color"]
    logo_html = f'<img src="{logo_b64}" class="logo-img" alt="logo"/>' if logo_b64 else ""

    items_html = ""
    for i, item in enumerate(body_items, 1):
        items_html += f"""
        <div class="item">
          <div class="item-num">{i:02d}</div>
          <div class="item-text">{item}</div>
        </div>"""

    return f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
<style>
    {_base_styles(cfg)}
    body {{ background: {bg}; }}
    .outer {{
        width: 800px; height: 800px;
        background: {bg};
        display: flex; align-items: center; justify-content: center;
        padding: 30px;
    }}
    .card {{
        width: 100%; height: 100%;
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.10);
        display: flex; flex-direction: row;
        position: relative;
        overflow: hidden;
    }}
    .rings {{
        width: 32px; min-width: 32px;
        background: {bg};
        display: flex; flex-direction: column;
        align-items: center; justify-content: space-evenly;
    }}
    .ring {{
        width: 22px; height: 22px;
        border-radius: 50%;
        border: 4px solid {p};
        background: white;
    }}
    .main {{
        flex: 1;
        display: flex; flex-direction: column;
        padding: 36px 36px 70px 24px;
        gap: 0;
    }}
    .heading-wrap {{
        display: flex; align-items: center; gap: 16px;
        margin-bottom: 14px;
    }}
    .heading {{
        font-size: 40px; font-weight: 900;
        color: {p};
        line-height: 1.15;
    }}
    .heading em {{ color: {p}; font-style: normal; }}
    .divider {{
        width: 100%; height: 2px;
        background: linear-gradient(to right, {p}, {s});
        margin-bottom: 22px;
        border-radius: 2px;
    }}
    .icon-side {{
        width: 180px; min-width: 180px;
        display: flex; align-items: center; justify-content: center;
        padding: 20px 16px 70px 0;
    }}
    .icon-side svg {{ width: 140px; height: 140px; }}
    .items {{ display: flex; flex-direction: column; gap: 14px; flex: 1; }}
    .item {{
        display: flex; align-items: flex-start; gap: 14px;
        background: {bg};
        border-radius: 12px;
        padding: 12px 16px;
    }}
    .item-num {{
        width: 32px; height: 32px; min-width: 32px;
        border-radius: 50%;
        background: {p};
        color: white;
        font-size: 14px; font-weight: 700;
        display: flex; align-items: center; justify-content: center;
    }}
    .item-text {{
        font-size: 20px; line-height: 1.5;
        color: {txt};
        flex: 1;
    }}
    .footer {{
        position: absolute; bottom: 0; left: 0; right: 0;
        background: {p};
        height: 60px;
        display: flex; align-items: center; justify-content: center;
        gap: 14px;
        padding: 0 24px;
    }}
    .logo-img {{ height: 32px; object-fit: contain; filter: brightness(0) invert(1); }}
    .hospital-name {{ color: white; font-size: 18px; font-weight: 700; }}
</style>
</head><body>
<div class="outer">
  <div class="card">
    <div class="rings">
      {''.join(['<div class="ring"></div>'] * 9)}
    </div>
    <div class="main">
      <div class="heading-wrap">
        <div class="heading">{heading}</div>
      </div>
      <div class="divider"></div>
      <div class="items">{items_html}</div>
    </div>
    <div class="icon-side">{icon_svg}</div>
    <div class="footer">
      {logo_html}
      <span class="hospital-name">{cfg.get('name', '')}</span>
    </div>
  </div>
</div>
</body></html>"""


def thumbnail_clean(cfg: dict, title: str, subtitle: str, icon_svg: str, logo_b64: str) -> str:
    p = cfg["primary_color"]
    s = cfg["secondary_color"]
    bg = cfg["background_color"]
    txt = cfg["text_color"]
    logo_html = f'<img src="{logo_b64}" class="logo-img" alt="logo"/>' if logo_b64 else ""
    return f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
<style>
    {_base_styles(cfg)}
    body {{ background: {p}; }}
    .outer {{
        width: 800px; height: 800px;
        background: {p};
        display: flex; align-items: center; justify-content: center;
        position: relative;
    }}
    .deco-top {{
        position: absolute; top: 0; left: 0; right: 0;
        height: 6px; background: {s};
    }}
    .deco-bottom {{
        position: absolute; bottom: 0; left: 0; right: 0;
        height: 6px; background: {s};
    }}
    .plus1 {{
        position: absolute; top: 24px; left: 50%;
        transform: translateX(-50%);
        color: {s}; font-size: 24px; opacity: 0.7;
    }}
    .plus2 {{
        position: absolute; bottom: 24px; left: 50%;
        transform: translateX(-50%);
        color: {s}; font-size: 24px; opacity: 0.7;
    }}
    .card {{
        width: 680px; height: 680px;
        background: white;
        border-radius: 24px;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        gap: 24px;
        padding: 40px;
        box-shadow: 0 12px 48px rgba(0,0,0,0.18);
    }}
    .title {{
        font-size: 72px; font-weight: 900;
        color: {p};
        text-align: center;
        line-height: 1.1;
        letter-spacing: -2px;
    }}
    .icon-wrap {{
        width: 260px; height: 260px;
    }}
    .icon-wrap svg {{ width: 100%; height: 100%; }}
    .footer {{
        display: flex; align-items: center; gap: 12px;
    }}
    .logo-img {{ height: 32px; object-fit: contain; }}
    .hospital-name {{
        color: {p}; font-size: 18px; font-weight: 700;
    }}
</style>
</head><body>
<div class="outer">
  <div class="deco-top"></div>
  <span class="plus1">+ ∨</span>
  <div class="card">
    <div class="title">{title}</div>
    <div class="icon-wrap">{icon_svg}</div>
    <div class="footer">
      {logo_html}
      <span class="hospital-name">{cfg.get('name', '')}</span>
    </div>
  </div>
  <span class="plus2">∧ +</span>
  <div class="deco-bottom"></div>
</div>
</body></html>"""


def content_clean(cfg: dict, card_num: int, total: int, heading: str,
                  body_items: list[str], icon_svg: str, logo_b64: str) -> str:
    p = cfg["primary_color"]
    s = cfg["secondary_color"]
    bg = cfg["background_color"]
    txt = cfg["text_color"]
    logo_html = f'<img src="{logo_b64}" class="logo-img" alt="logo"/>' if logo_b64 else ""

    items_html = ""
    for i, item in enumerate(body_items, 1):
        items_html += f"""
        <div class="item">
          <div class="item-num">{i}</div>
          <div class="item-text">{item}</div>
        </div>"""

    return f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
<style>
    {_base_styles(cfg)}
    body {{ background: {p}; }}
    .outer {{
        width: 800px; height: 800px;
        background: {p};
        display: flex; flex-direction: column;
    }}
    .header-bar {{
        background: {p};
        padding: 24px 36px 16px;
        display: flex; align-items: center; justify-content: space-between;
    }}
    .heading {{
        font-size: 36px; font-weight: 900;
        color: white;
    }}
    .card-num {{
        color: {s}; font-size: 18px; font-weight: 700;
    }}
    .body {{
        flex: 1;
        background: {bg};
        display: flex;
        gap: 0;
        overflow: hidden;
    }}
    .items-col {{
        flex: 1;
        padding: 28px 28px 28px 36px;
        display: flex; flex-direction: column; gap: 14px;
    }}
    .item {{
        display: flex; align-items: flex-start; gap: 14px;
        background: white;
        border-radius: 12px;
        padding: 14px 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    .item-num {{
        width: 30px; height: 30px; min-width: 30px;
        background: {p};
        color: white;
        border-radius: 6px;
        font-size: 15px; font-weight: 700;
        display: flex; align-items: center; justify-content: center;
    }}
    .item-text {{
        font-size: 19px; line-height: 1.5;
        color: {txt};
    }}
    .icon-col {{
        width: 180px; min-width: 180px;
        display: flex; align-items: center; justify-content: center;
        padding: 20px 20px 20px 0;
    }}
    .icon-col svg {{ width: 140px; height: 140px; }}
    .footer {{
        background: {p};
        height: 58px;
        display: flex; align-items: center; justify-content: center;
        gap: 12px;
    }}
    .logo-img {{ height: 30px; object-fit: contain; filter: brightness(0) invert(1); }}
    .hospital-name {{ color: white; font-size: 17px; font-weight: 700; }}
</style>
</head><body>
<div class="outer">
  <div class="header-bar">
    <div class="heading">{heading}</div>
    <div class="card-num">{card_num} / {total}</div>
  </div>
  <div class="body">
    <div class="items-col">{items_html}</div>
    <div class="icon-col">{icon_svg}</div>
  </div>
  <div class="footer">
    {logo_html}
    <span class="hospital-name">{cfg.get('name', '')}</span>
  </div>
</div>
</body></html>"""


def build_card_html(template: str, card_type: str, cfg: dict, **kwargs) -> str:
    """Dispatch to the right template function."""
    if template == "notebook":
        if card_type == "thumbnail":
            return thumbnail_notebook(cfg, **kwargs)
        return content_notebook(cfg, **kwargs)
    else:
        if card_type == "thumbnail":
            return thumbnail_clean(cfg, **kwargs)
        return content_clean(cfg, **kwargs)
