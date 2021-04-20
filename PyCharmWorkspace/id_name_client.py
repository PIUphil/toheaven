import socket

port = 5000
address = ("127.0.0.1", port)
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

num_input = input("Student_ID to send : ")
sock.send(num_input.encode())

recv_name = sock.recv(BUFSIZE).decode()
print("ID : ", num_input, " Name : ", recv_name)
sock.close()
