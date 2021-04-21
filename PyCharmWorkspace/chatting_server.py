import socket
import threading

clients = []   # 10명(여러명)의 데이터소켓을 가지고있음,,

def thread_handler(data_socket, dummy):
    global clients
    while True:
        data = data_socket.recv(1024)   # decode  / bytestream 이라서 생략
        for client in clients:
            client.send(data)           # encode 생략
        if not data:
            clients.remove(data_socket)
            data_socket.close()
            break

if __name__ == "__main__":
    #global clients

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 2500))
    sock.listen(5)

    while True:
        data_socket, client_addr = sock.accept()
        clients.append((data_socket))  # (( ))
        print("clients : ", clients)
        t = threading.Thread(target=thread_handler, args=(data_socket, 0))  # 0, dummy = client_address
        t.daemon = True
        t.start()


    sock.close()