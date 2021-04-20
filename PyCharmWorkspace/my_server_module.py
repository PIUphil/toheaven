class TCPServer:
    def __init__(self, port):  # 생성자 - 객체 초기화 (자동호출)
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", port))  # IP, port
        self.sock.listen(5)

    def __del__(self):  # 소멸자
        self.sock.close()

    def accept(self):
        data_socket, client_addr = self.sock.accept()
        return data_socket, client_addr

if __name__ == '__main__': # name-모듈이름 / main-프로그램 최상위 진입점(시작점) 영역이름
    sock = TCPServer(2500)  # 현재파일이 최상위 진입점인지, import된 모듈인지 확인하기위함.

    data_socket, client_addr = sock.accept()
    msg = data_socket.recv(1024).decode()
    print("recv : ", msg)

    data_socket.send(msg.encode())
    data_socket.close()



