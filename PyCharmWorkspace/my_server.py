import my_server_module as mt  # My TCP

port = 2500
sock = mt.TCPServer(port)

while True:
    data_socket, client_addr = sock.accept()
    print("connected by ", client_addr)
    msg = data_socket.recv(1024).decode()
    print("msg : ", msg)
    data_socket.send(msg.encode())
    data_socket.close()
