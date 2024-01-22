import socket

def udp_client(server_host, server_port, message):
    # UDPソケットを作成
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # メッセージをサーバーに送信
        udp_socket.sendto(message.encode('utf-8'), (server_host, server_port))
        print(f"データを {server_host}:{server_port} に送信しました: {message}")
    
    finally:
        # ソケットを閉じる
        udp_socket.close()

if __name__ == "__main__":
    # サーバーのホストとポートを指定
    server_host = "127.0.0.1"
    server_port = 12345

    # 送信するメッセージを指定（ここでは文字列として指定していますが、数字データでも問題ありません）
    message = "123"

    # UDPクライアントを起動
    udp_client(server_host, server_port, message)
