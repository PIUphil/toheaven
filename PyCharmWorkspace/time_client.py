import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp socket

server_address = ("127.0.0.1", 5000) # ip주소, port번호 - 튜플형식 #
sock.connect(server_address)   # 127.0.0.1 - loop-back 주소 - 자기자신주소(localhost)

msg = sock.recv(1024).decode()  # decode - encode의 반대
print("recv:", msg)
sock.close()