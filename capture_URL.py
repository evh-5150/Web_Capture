import subprocess
import os
import sys
from datetime import datetime
from playwright.sync_api import sync_playwright

def get_current_safari_url():
    """
    AppleScriptを使って、現在Safariで開かれている最前面のタブのURLを取得します。
    """
    script = 'tell application "Safari" to get URL of front document'
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.strip()
        if "Application isn’t running" in error_message:
            print("エラー: Safariが起動していません。", file=sys.stderr)
        elif "doesn’t have any windows" in error_message:
            print("エラー: Safariにウィンドウがありません。", file=sys.stderr)
        else:
            print(f"AppleScriptエラー: {error_message}", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("エラー: `osascript`コマンドが見つかりません。macOSで実行していますか？", file=sys.stderr)
        return None


def capture_full_page(url, output_path):
    """
    指定されたURLのページ全体のスクリーンショットをPlaywrightで撮影します。
    """
    print(f"URLを取得しました: {url}")
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        try:
            print("ページに移動しています...")
            
            # ★★★ 待機条件を 'networkidle' から 'load' に変更 ★★★
            # これにより、バックグラウンドで通信を続けるサイトでもタイムアウトしにくくなります。
            page.goto(url, wait_until='load', timeout=60000)

            print(f"フルページのスクリーンショットを {output_path} に保存しています...")
            page.screenshot(path=output_path, full_page=True)
            
            print("キャプチャーが正常に完了しました！")
        except Exception as e:
            print(f"キャプチャー中にエラーが発生しました: {e}", file=sys.stderr)
        finally:
            browser.close()


def main():
    """
    メイン処理
    """
    url = get_current_safari_url()

    if not url:
        sys.exit(1)

    desktop_path = os.path.expanduser('~/Desktop')
    timestamp = datetime.now().strftime('%H%M%S')
    filename = f"{timestamp}.png"
    output_path = os.path.join(desktop_path, filename)

    capture_full_page(url, output_path)


if __name__ == "__main__":
    main()