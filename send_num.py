import socket
import time

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)

    print('サーバーが起動しました。')

    client_socket, addr = server_socket.accept()
    print(f'クライアントが接続しました。')

    try:
        number = 1

        while True:
            data = str(number)
            client_socket.send(data.encode('utf-8'))
            print(f'送信したデータ: {data}')

            number += 1
            time.sleep(1)

    except Exception as e:
        print(f'エラー: {e}')

    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()
