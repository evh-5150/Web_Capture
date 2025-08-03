import os
import subprocess
from datetime import datetime

def get_safari_window_id():
    """
    AppleScriptを使ってSafariのウィンドウIDのみを取得する。
    ※ウィンドウを特定する最小限の利用にとどめます。
    """
    # ウィンドウのIDを取得するだけのシンプルなスクリプト
    script = 'tell application "Safari" to id of front window'
    try:
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True, text=True, check=True, timeout=5
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"SafariのウィンドウID取得中にエラー: {e}", file=sys.stderr)
        return None

def capture_safari_visible_area():
    """
    macOSのscreencaptureコマンドを使い、Safariのウィンドウをキャプチャーする。
    """
    window_id = get_safari_window_id()
    if not window_id:
        print("Safariのウィンドウが見つからなかったため、処理を中断します。", file=sys.stderr)
        return

    # 保存先のパスを生成
    desktop_path = os.path.expanduser('~/Desktop')
    timestamp = datetime.now().strftime('%H%M%S')
    output_path = os.path.join(desktop_path, f"{timestamp}.png")

    print("Safariの表示領域をキャプチャーしています...")
    try:
        # screencapture コマンドのオプション
        # -l <window_id>: 指定したウィンドウIDのウィンドウをキャプチャー
        # -o: ウィンドウの影を含めない
        # -T 0: 実行までの待ち時間を0秒に
        subprocess.run(
            ['screencapture', '-o', '-T', '0', f'-l{window_id}', output_path],
            check=True
        )
        print(f"キャプチャーが正常に完了しました！ -> {output_path}")

    except subprocess.CalledProcessError as e:
        print(f"キャプチャー中にエラーが発生しました: {e}", file=sys.stderr)
    except FileNotFoundError:
        print("エラー: `screencapture`コマンドが見つかりません。macOSで実行していますか？", file=sys.stderr)


if __name__ == "__main__":
    capture_safari_visible_area()