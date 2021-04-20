from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", 2500))  # 포트번호 - 현재 프로그램 찾아가는 내선번호 같은거,,
                       # 0~ 1024 : reserved / 80 : web
                       # 2Byte 사용 => 0~65535 / 2000 이후 번호 사용 권장
sock.listen(5)

while True:
    print("waiting for clients...")
    data_socket, client_addr = sock.accept()
    print("connected by ", client_addr)

    msg = data_socket.recv(1024).decode()  # bufsize

    if msg:
        print("recv : ", msg)
        data_socket.send(msg.encode())

    data_socket.close()