from socket import *
import _thread

BUFSIZE = 1024
host_addr = "127.0.0.1"
port = 2500

def thread_handler(data_sock, dummy):   # addr -> dummy /안씀
    while True:
        msg = data_sock.recv(BUFSIZE).decode()
        if not msg: break
        print("recv : ", msg)
        data_sock.send(msg.encode())
    data_sock.close()

if __name__ == "__main__":
    addr = (host_addr, port)
    serv_addr = socket(AF_INET, SOCK_STREAM)
    serv_addr.bind(addr)
    serv_addr.listen(5)

    while True:
        data_sock, client_addr = serv_addr.accept()
        print("connected by : ", client_addr)
        # create thread for client
        _thread.start_new_thread(thread_handler, (data_sock, 0))

    serv_addr.close()