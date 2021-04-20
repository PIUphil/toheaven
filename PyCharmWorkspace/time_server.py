import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 네트워크 패밀리 / tcp-sockstream , ip-,,,
# tcp소켓 -> af_inet, sock_stream
address = ("",5000)   # 서버 ip = "" - NULL
sock.bind(address)
sock.listen(5)  # backlog -> 동시접속자가 많으면 크기를 많이줌..

while True:
    data_socket, client_addr = sock.accept()
    print("connection requested from", client_addr)
    data_socket.send(time.ctime(time.time()).encode())  # ctime-문자열로 바꾸어줌, encode-bytestream으로 바꿔줘야함
    data_socket.close()
    # 접속하면 현재시간을 알려주는 서버
    # 클라이언트 순차 처리
