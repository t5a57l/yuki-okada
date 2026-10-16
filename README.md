# CV サイト — 岡田 裕貴 (Yuki Okada)

GitHub Pages でホストする静的な個人 CV サイト（日英バイリンガル）。

## 構成
- `index.html` … 日本語ページ
- `index_en.html` … 英語ページ
- `style.css` … 共通スタイル
- `profile.jpg` … プロフィール写真（任意。置けば自動表示、無ければ非表示）
- `cv_ja.pdf` / `cv_en.pdf` … PDF 版の履歴書（ヘッダのリンク先）
- `cv/` … PDF 履歴書のソース（`cv_ja.html` / `cv_en.html` / `cv.css`）と生成スクリプト `build_pdf.py`。詳細は `cv/README.md`

## ローカルプレビュー
```bash
cd cv-site
python3 -m http.server 8000
# ブラウザで http://localhost:8000 を開く
```

## GitHub Pages への公開
1. リポジトリを作成して push
2. リポジトリの Settings → Pages → Source を `main` ブランチの `/ (root)` に設定
3. 数分後 `https://<username>.github.io/<repo>/` で公開

## 更新方法
業績を追加するときは該当セクションの `<li>` を編集する。日本語・英語の両ファイルを更新すること。
筆頭発表者・自分の名前は `<span class="me">` で太字表示。

## PDF 履歴書の更新
`cv/cv_ja.html` と `cv/cv_en.html` を編集し、以下で再生成する（playwright + chromium が必要）。
フッタの「Last updated」は実行日が自動で入る。

```bash
python3 cv/build_pdf.py        # cv_ja.pdf と cv_en.pdf を再生成
python3 cv/build_pdf.py en     # 英語版のみ
```
