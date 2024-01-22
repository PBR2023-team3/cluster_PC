import socket

def udp_server(host, port):
    # UDPソケットを作成
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # ソケットを指定されたホストとポートにバインド
        udp_socket.bind((host, port))

        print(f"UDPサーバーが {host}:{port} で起動しました。")

        while True:
            # データを受信
            data, client_address = udp_socket.recvfrom(1024)
            
            # 受信したデータを表示
            print(f"受信したデータ from {client_address}: {data.decode('utf-8')}")

    except KeyboardInterrupt:
        # Ctrl+Cが押されたときにプログラムを終了
        print("\nプログラムが終了されました。")

    finally:
        # ソケットを閉じる
        udp_socket.close()

if __name__ == "__main__":
    # ホストとポートを指定
    server_host = "172.20.10.5"
    server_port = 12345

    # UDPサーバーを起動
    udp_server(server_host, server_port)
