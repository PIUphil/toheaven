import socket

port = 2500
address = ("10.10.11.57", port)
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

msg = input("Msg to send : ")
sock.send(msg.encode())

recv_msg = sock.recv(BUFSIZE).decode()
print("echo msg : ", recv_msg)
sock.close()
