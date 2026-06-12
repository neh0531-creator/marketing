"""
Medical SVG icon library with keyword-based auto-selection.
Icons are inline SVG strings for common medical topics.
"""

ICONS = {
    "유방암": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <circle cx="50" cy="45" r="28" fill="#F9C6C6" stroke="#E07070" stroke-width="2"/>
        <circle cx="50" cy="45" r="12" fill="#E07070" opacity="0.6"/>
        <path d="M30 70 Q50 85 70 70" stroke="#E07070" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <circle cx="38" cy="40" r="4" fill="#C0392B" opacity="0.5"/>
        <circle cx="60" cy="48" r="5" fill="#C0392B" opacity="0.5"/>
    </svg>""",

    "갑상선": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <ellipse cx="38" cy="55" rx="16" ry="22" fill="#A8D8EA" stroke="#5BA4CF" stroke-width="2"/>
        <ellipse cx="62" cy="55" rx="16" ry="22" fill="#A8D8EA" stroke="#5BA4CF" stroke-width="2"/>
        <rect x="44" y="42" width="12" height="8" rx="4" fill="#5BA4CF"/>
        <path d="M50 25 L50 42" stroke="#5BA4CF" stroke-width="3" stroke-linecap="round"/>
    </svg>""",

    "난청": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M35 30 Q35 20 50 20 Q65 20 65 35 Q65 50 55 58 Q50 63 50 72"
              fill="#FFD9A0" stroke="#E8A44A" stroke-width="3" stroke-linecap="round"/>
        <circle cx="50" cy="78" r="4" fill="#E8A44A"/>
        <path d="M72 35 Q78 45 72 55" stroke="#E8A44A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M78 28 Q88 45 78 62" stroke="#E8A44A" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.6"/>
    </svg>""",

    "이명": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M35 30 Q35 20 50 20 Q65 20 65 35 Q65 50 55 58 Q50 63 50 72"
              fill="#FFD9A0" stroke="#E8A44A" stroke-width="3" stroke-linecap="round"/>
        <circle cx="50" cy="78" r="4" fill="#E8A44A"/>
        <path d="M60 40 L75 35 M60 45 L78 45 M60 50 L75 55" stroke="#E07070" stroke-width="2" stroke-linecap="round"/>
    </svg>""",

    "어지럼증": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <circle cx="50" cy="42" r="22" fill="#C8E6C9" stroke="#66BB6A" stroke-width="2"/>
        <path d="M35 42 Q42 35 50 42 Q58 49 65 42" stroke="#388E3C" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M40 35 Q50 28 60 35" stroke="#388E3C" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.5"/>
        <path d="M40 20 Q50 15 60 20" stroke="#66BB6A" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.4"/>
        <circle cx="44" cy="38" r="3" fill="#1B5E20"/>
        <circle cx="56" cy="38" r="3" fill="#1B5E20"/>
        <path d="M44 48 Q50 52 56 48" stroke="#1B5E20" stroke-width="2" fill="none" stroke-linecap="round"/>
    </svg>""",

    "당뇨": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M50 20 C30 20 20 35 20 50 C20 68 33 80 50 80 C67 80 80 68 80 50 C80 35 70 20 50 20Z"
              fill="#FFCDD2" stroke="#E57373" stroke-width="2"/>
        <path d="M35 50 L45 60 L65 40" stroke="#C62828" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="65" cy="30" r="8" fill="#FFF9C4" stroke="#F9A825" stroke-width="2"/>
        <text x="65" y="34" text-anchor="middle" font-size="10" fill="#F9A825" font-weight="bold">%</text>
    </svg>""",

    "고혈압": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M50 75 C50 75 20 58 20 40 C20 29 29 22 38 22 C43 22 47 24 50 28 C53 24 57 22 62 22 C71 22 80 29 80 40 C80 58 50 75 50 75Z"
              fill="#FFCDD2" stroke="#E53935" stroke-width="2"/>
        <polyline points="28,48 35,35 42,52 50,30 58,55 65,42 72,48"
                  stroke="#C62828" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>""",

    "위암": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M25 40 Q25 28 38 28 Q48 28 50 35 Q52 28 62 28 Q75 28 75 40 Q75 58 60 70 Q55 75 50 78 Q45 75 40 70 Q25 58 25 40Z"
              fill="#FFE0B2" stroke="#FF8A65" stroke-width="2"/>
        <ellipse cx="50" cy="52" rx="14" ry="10" fill="#FF8A65" opacity="0.4"/>
        <circle cx="44" cy="48" r="4" fill="#E64A19" opacity="0.6"/>
        <circle cx="56" cy="55" r="5" fill="#E64A19" opacity="0.5"/>
    </svg>""",

    "대장암": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M25 30 Q20 50 30 65 Q40 78 55 75 Q70 72 75 60 Q80 45 70 35 Q60 25 45 28 Q30 31 25 30Z"
              fill="#DCEDC8" stroke="#8BC34A" stroke-width="2"/>
        <path d="M35 45 Q45 38 55 45 Q65 52 55 60 Q45 68 35 60 Q25 52 35 45Z"
              fill="#8BC34A" opacity="0.4"/>
        <circle cx="48" cy="50" r="5" fill="#558B2F" opacity="0.6"/>
    </svg>""",

    "폐암": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M50 22 L50 55" stroke="#90A4AE" stroke-width="3" stroke-linecap="round"/>
        <path d="M50 30 Q35 28 28 35 Q20 43 22 55 Q24 67 35 72 Q45 76 50 68"
              fill="#B0BEC5" stroke="#78909C" stroke-width="2"/>
        <path d="M50 30 Q65 28 72 35 Q80 43 78 55 Q76 67 65 72 Q55 76 50 68"
              fill="#B0BEC5" stroke="#78909C" stroke-width="2"/>
    </svg>""",

    "척추": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <rect x="43" y="15" width="14" height="10" rx="3" fill="#BBDEFB" stroke="#42A5F5" stroke-width="1.5"/>
        <rect x="43" y="28" width="14" height="10" rx="3" fill="#BBDEFB" stroke="#42A5F5" stroke-width="1.5"/>
        <rect x="43" y="41" width="14" height="10" rx="3" fill="#BBDEFB" stroke="#42A5F5" stroke-width="1.5"/>
        <rect x="43" y="54" width="14" height="10" rx="3" fill="#BBDEFB" stroke="#42A5F5" stroke-width="1.5"/>
        <rect x="43" y="67" width="14" height="10" rx="3" fill="#BBDEFB" stroke="#42A5F5" stroke-width="1.5"/>
        <line x1="50" y1="25" x2="50" y2="28" stroke="#42A5F5" stroke-width="2"/>
        <line x1="50" y1="38" x2="50" y2="41" stroke="#42A5F5" stroke-width="2"/>
        <line x1="50" y1="51" x2="50" y2="54" stroke="#42A5F5" stroke-width="2"/>
        <line x1="50" y1="64" x2="50" y2="67" stroke="#42A5F5" stroke-width="2"/>
    </svg>""",

    "무릎": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <rect x="38" y="15" width="24" height="30" rx="8" fill="#BBDEFB" stroke="#42A5F5" stroke-width="2"/>
        <ellipse cx="50" cy="52" rx="16" ry="12" fill="#E3F2FD" stroke="#42A5F5" stroke-width="2"/>
        <rect x="38" y="60" width="24" height="25" rx="8" fill="#BBDEFB" stroke="#42A5F5" stroke-width="2"/>
    </svg>""",

    "피부": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <rect x="18" y="18" width="64" height="64" rx="20" fill="#FFCC80" stroke="#FFA726" stroke-width="2"/>
        <circle cx="37" cy="37" r="5" fill="#FF8A65" opacity="0.5"/>
        <circle cx="63" cy="42" r="4" fill="#FF7043" opacity="0.4"/>
        <circle cx="45" cy="58" r="6" fill="#FF8A65" opacity="0.45"/>
        <path d="M30 65 Q50 72 70 65" stroke="#FFA726" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    </svg>""",

    "눈": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M15 50 Q50 20 85 50 Q50 80 15 50Z" fill="#E3F2FD" stroke="#42A5F5" stroke-width="2"/>
        <circle cx="50" cy="50" r="14" fill="#90CAF9" stroke="#1E88E5" stroke-width="2"/>
        <circle cx="50" cy="50" r="8" fill="#1565C0"/>
        <circle cx="54" cy="46" r="3" fill="white"/>
    </svg>""",

    "치과": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M30 25 Q25 22 22 28 Q18 35 22 50 Q26 65 35 72 Q40 76 45 70 Q48 65 50 65 Q52 65 55 70 Q60 76 65 72 Q74 65 78 50 Q82 35 78 28 Q75 22 70 25 Q62 30 50 30 Q38 30 30 25Z"
              fill="#FAFAFA" stroke="#BDBDBD" stroke-width="2"/>
        <line x1="50" y1="30" x2="50" y2="68" stroke="#E0E0E0" stroke-width="1.5"/>
        <line x1="38" y1="32" x2="38" y2="50" stroke="#E0E0E0" stroke-width="1.5"/>
        <line x1="62" y1="32" x2="62" y2="50" stroke="#E0E0E0" stroke-width="1.5"/>
    </svg>""",

    "심장": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <path d="M50 78 C50 78 18 58 18 38 C18 26 27 18 37 18 C43 18 48 21 50 26 C52 21 57 18 63 18 C73 18 82 26 82 38 C82 58 50 78 50 78Z"
              fill="#FFCDD2" stroke="#E53935" stroke-width="2"/>
        <polyline points="30,42 38,30 46,50 54,28 62,48 70,38"
                  stroke="#C62828" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>""",

    "검진": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <rect x="25" y="18" width="50" height="64" rx="6" fill="#FFFFFF" stroke="#90A4AE" stroke-width="2"/>
        <rect x="38" y="12" width="24" height="14" rx="4" fill="#B0BEC5" stroke="#78909C" stroke-width="2"/>
        <line x1="35" y1="42" x2="65" y2="42" stroke="#90A4AE" stroke-width="2"/>
        <line x1="35" y1="54" x2="65" y2="54" stroke="#90A4AE" stroke-width="2"/>
        <line x1="35" y1="66" x2="55" y2="66" stroke="#90A4AE" stroke-width="2"/>
        <path d="M35 42 L41 48 L55 34" stroke="#4CAF50" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>""",

    "수술": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <line x1="25" y1="75" x2="65" y2="35" stroke="#B0BEC5" stroke-width="5" stroke-linecap="round"/>
        <circle cx="65" cy="35" r="8" fill="#ECEFF1" stroke="#78909C" stroke-width="2"/>
        <line x1="22" y1="78" x2="28" y2="72" stroke="#E57373" stroke-width="3" stroke-linecap="round"/>
        <path d="M40 60 Q50 55 45 70" stroke="#EF9A9A" stroke-width="2" fill="none"/>
    </svg>""",

    "기본": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="35" fill="#E3F2FD" stroke="#42A5F5" stroke-width="2"/>
        <path d="M50 30 L50 58 M38 44 L62 44" stroke="#1565C0" stroke-width="5" stroke-linecap="round"/>
    </svg>"""
}

KEYWORD_MAP = {
    "유방": "유방암", "유방암": "유방암",
    "갑상선": "갑상선", "갑상샘": "갑상선",
    "난청": "난청", "청력": "난청", "청각": "난청",
    "이명": "이명", "귀울림": "이명",
    "어지럼": "어지럼증", "현기증": "어지럼증", "균형": "어지럼증",
    "당뇨": "당뇨", "혈당": "당뇨",
    "고혈압": "고혈압", "혈압": "고혈압",
    "위암": "위암", "위": "위암",
    "대장": "대장암", "대장암": "대장암",
    "폐암": "폐암", "폐": "폐암",
    "척추": "척추", "허리": "척추", "디스크": "척추",
    "무릎": "무릎", "관절": "무릎",
    "피부": "피부", "여드름": "피부", "아토피": "피부",
    "눈": "눈", "시력": "눈", "백내장": "눈", "녹내장": "눈",
    "치과": "치과", "치아": "치과", "임플란트": "치과",
    "심장": "심장", "심근": "심장", "부정맥": "심장",
    "검진": "검진", "건강검진": "검진", "스크리닝": "검진",
    "수술": "수술", "절제": "수술", "시술": "수술",
}


def get_icon(keywords: list[str]) -> str:
    """Return SVG string for the best matching icon given a list of keywords."""
    for kw in keywords:
        for key, icon_name in KEYWORD_MAP.items():
            if key in kw or kw in key:
                return ICONS.get(icon_name, ICONS["기본"])
    return ICONS["기본"]


def get_icon_by_text(text: str) -> str:
    """Return SVG string by scanning text for known medical keywords."""
    for key, icon_name in KEYWORD_MAP.items():
        if key in text:
            return ICONS.get(icon_name, ICONS["기본"])
    return ICONS["기본"]
