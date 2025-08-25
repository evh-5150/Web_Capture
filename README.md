# Safari Full Page Capture

## 概要 (Overview)
このツールは，macOS の Safari で開かれている最前面のタブの URL を取得し，その Web ページ全体のスクリーンショット (フルページキャプチャ) を取得します．
Webページをスクロールしないと見えない部分も含めて，1 枚の画像として保存したい場合に便利です．

## 機能 (Features)
- Safari で現在アクティブなタブの URL を自動で取得します．
- 取得した URL のページ全体のスクリーンショットを撮影します．
- 撮影した画像は，実行時のタイムスタンプ (時分秒) をファイル名としてデスクトップに保存します．

## 動作環境 (Prerequisites)
- **OS:** macOS
- **Python:** Python 3.x
- **ブラウザ:** Safari

## インストール (Installation)
このスクリプトは Playwright ライブラリを使用します．以下の手順でインストールしてください．

1.  **リポジトリをクローンまたはスクリプトをダウンロードします．**

2.  **Playwrightライブラリをインストールします．**
    ```bash
    pip install playwright
    ```
3.  **Playwright用のブラウザエンジンをインストールします．**
    このスクリプトはWebKit (Safari のエンジン) を使用します．
    ```bash
    playwright install webkit
    ```
    (もし他のブラウザも使う可能性がある場合は `playwright install` を実行してください)

## 使い方 (Usage)
1.  キャプチャしたい Web ページを Safari で開いて，最前面に表示します．
2.  ターミナルで以下のコマンドを実行します．
    ```bash
    python safari_fullpage_capture.py
    ```
3.  処理が完了すると，デスクトップに画像ファイルが保存されます．

## 注意点 (Notes)
- このスクリプトは AppleScript を使用して Safari から情報を取得するため，macOS 専用です．
- 初回実行時，macOS から「Python」や「ターミナル」が「Safari」を制御することの許可を求めるダイアログが表示される場合があります．セキュリティ設定で許可してください．
- ログインが必要なページや，JavaScript で動的にコンテンツが生成されるページでは，意図した通りのスクリーンショットが撮れない場合があります．
- ページの読み込みに時間がかかる場合，`timeout`の値を調整する必要がある可能性があります (現在は 60 秒に設定されています)．
