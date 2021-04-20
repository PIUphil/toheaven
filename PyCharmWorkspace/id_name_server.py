from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", 5000))
sock.listen(5)
table = {'20150001':'Hong',
         '20150002':'Sim',
         '20150003':'Park'}

while True:
    print("waiting for clients...")
    data_socket, client_addr = sock.accept()
    print("connected by ", client_addr)

    num_input = data_socket.recv(1024).decode()

    if num_input:
        print("recv : ", num_input)

        if num_input in table.keys():
            name = table[num_input]
            print("send_name : '", name, "' to ", client_addr)
        else:
            name = "Noname"

        data_socket.send(name.encode())

    data_socket.close()