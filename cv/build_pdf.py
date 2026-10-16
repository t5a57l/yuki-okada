#!/usr/bin/env python3
"""cv_ja.html / cv_en.html を A4 PDF に変換する。

使い方:
    python3 cv/build_pdf.py            # 両言語
    python3 cv/build_pdf.py ja         # 日本語のみ

依存: playwright (python) と chromium。Inter フォントは Google Fonts から
ビルド時に取得する（オフライン時は Noto Sans CJK JP にフォールバック）。
出力はリポジトリ直下の cv_ja.pdf / cv_en.pdf。
"""
import sys
import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
LANGS = {"ja": "Last updated: {d}", "en": "Last updated: {d}"}


def build(lang: str, updated: str) -> Path:
    src = ROOT / "cv" / f"cv_{lang}.html"
    out = ROOT / f"cv_{lang}.pdf"
    footer = (
        '<div style="font-family:Inter,\'Noto Sans CJK JP\',sans-serif;font-size:7.5pt;'
        'color:#5b6068;width:100%;padding:0 17mm;display:flex;justify-content:space-between;">'
        f'<span>{LANGS[lang].format(d=updated)}</span>'
        '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
    )
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(src.as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.pdf(
            path=str(out),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=footer,
            margin={"top": "15mm", "bottom": "17mm", "left": "17mm", "right": "17mm"},
        )
        browser.close()
    return out


if __name__ == "__main__":
    langs = sys.argv[1:] or ["ja", "en"]
    updated = datetime.date.today().strftime("%Y/%m/%d")
    for lang in langs:
        print("wrote", build(lang, updated))
