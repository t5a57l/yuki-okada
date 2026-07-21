# CV サイト — 岡田 裕貴 (Yuki Okada)

GitHub Pages でホストする静的な個人 CV サイト（日英バイリンガル）。

## 構成
- `index.html` … 日本語ページ
- `index_en.html` … 英語ページ
- `style.css` … 共通スタイル
- `profile.jpg` … プロフィール写真（任意。置けば自動表示、無ければ非表示）

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
