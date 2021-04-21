import sys
from socket import *

ECHO_PORT = 2500
BUFSIZE = 1024
if len(sys.argv) > 1:
    port = int(eval(sys.argv[1]))
else:
    port = ECHO_PORT

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', port))
s.listen(1)

print("Waiting for connection from client")
conn, (remotehost, remoteport) = s.accept()
print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    data = float(data.decode())
    data = 9.0/5.0 * data + 32.0
    data = '{:.1f}'.format(data)
    conn.send(data.encode())

conn.close()
