# PDF 履歴書のソース

`cv_ja.pdf` / `cv_en.pdf`（リポジトリ直下）は、このディレクトリの HTML から生成する。
**HTML が正本**。PDF を直接編集しない。

## ファイル
- `cv_ja.html` … 日本語版の内容
- `cv_en.html` … 英語版の内容
- `cv.css` … 共通スタイル（A4 想定。英語版は `html[lang="en"]` で少し詰めている）
- `build_pdf.py` … HTML → PDF 変換（playwright + chromium）

## 更新手順
1. `cv_ja.html` と `cv_en.html` の該当セクションを編集する（ウェブページ `index.html` / `index_en.html` も忘れずに更新）
2. リポジトリ直下で PDF を再生成する。フッタの「Last updated」には実行日が自動で入る

```bash
python3 cv/build_pdf.py        # 両言語
python3 cv/build_pdf.py ja     # 日本語のみ
```

3. 2 ページに収まっているか確認する（`pdfinfo cv_ja.pdf | grep Pages`）。
   あふれたら `cv.css` の `.entry` の `margin` や `h2` の `margin` を少し詰める

## 依存
- Python 3 + `playwright`（`pip install playwright && playwright install chromium`）
- 欧文フォント Inter は Google Fonts からビルド時に取得する。オフラインでは Noto Sans CJK JP にフォールバックする

## エントリの記法
時系列を左、内容を右に置く 2 列構成。内容側は次のクラスで書き分ける。

```html
<div class="entry">
  <div class="d">2025.04–現在</div>            <!-- 期間。英語版は 2025.04–Today -->
  <div class="c">
    <div class="t">機関 部局（太字のタイトル行）</div>
    <div class="s">肩書・課程など（灰色の副行。英語版は斜体）</div>
    <div class="a">著者行（発表・論文のみ。本人は <span class="me">…</span>）</div>
    <div class="m">会議名, 番号, 開催地（ポスター発表）（灰色の行）</div>
    <ul class="n"><li>補足（箇条書き）</li></ul>
  </div>
</div>
```

- 横幅に収まらない長い演題・会議名は、句の切れ目で `<div class="t">` / `<div class="m">` を 2 つに分けて明示的に改行する
- 自己紹介は `<div class="bio">` 内の `<p>` を段落ごとに分ける（字下げなし、段落間に余白）
