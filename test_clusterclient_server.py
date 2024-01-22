import socket
import time

def convert_text_to_html(text):
    # 簡単なHTML形式に変換する例
    html_content = f"<p>{text}</p>"
    return html_content

def send_file_content_as_html(client_socket):
    file_path = "send_message.txt"  # テキストファイルのパスを指定

    try:
        html_content_first = f"<html><body>\n"
        client_socket.send(html_content_first.encode('utf-8'))
        time.sleep(1)  # 必要に応じて適切な待機時間を調整
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # 各行に改行を追加してHTMLデータを作成
                html_content = convert_text_to_html(line)

                # HTMLデータをクライアントに送信
                client_socket.send(html_content.encode('utf-8'))
                #time.sleep(1)  # 必要に応じて適切な待機時間を調整
        html_content_last = f"\n</body></html>"
        client_socket.send(html_content_last.encode('utf-8'))
        time.sleep(1)  # 必要に応じて適切な待機時間を調整

    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
    except Exception as e:
        print(f"エラー: {e}")
    

def start_server():
    # サーバーソケットの作成
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # 任意のポートを指定
    server_socket.listen(1)

    print('サーバーが起動しました。')

    # クライアントからの接続を待機
    client_socket, addr = server_socket.accept()
    print('クライアントが接続しました。')

    try:
        send_file_content_as_html(client_socket)
    except KeyboardInterrupt:
        print('サーバーが停止しました。')
    finally:
        # ソケットを閉じる
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()
