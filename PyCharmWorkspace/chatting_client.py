import socket
import _thread

def thread_handler(data_socket, dummy):
    while True:
        data_socket.recv(1024).decode()
        print(msg)


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 2500))

    _thread.start_new_thread(thread_handler, (sock, 0))

    # create thread for print recv msg
    while True:
        msg = input("msg : ")
        msg = "[phil] :" + msg
        sock.send(msg.encode())
        if msg == "[phil] :0": break