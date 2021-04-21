import socket
import encapsulation

SIZE = 5
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 2500))

HEAD = 0x05  # 바뀌지않는 상수값 정의할때 대문자 사용
addr = 1
seq_no = 1
frame_seq = ""
msg = "hello world"
#print("전송 메시지: ", msg)

for i in range(0, len(msg), SIZE):
    start = i
    frame_seq += encapsulation.frame(HEAD, addr, seq_no, msg[start:start+SIZE])
#    start += SIZE
    seq_no += 1

sock.send(frame_seq.encode())
msg = sock.recv(2048).decode()
print("recv frame : ", msg)
r_frame = msg.split(chr(0x05))
del r_frame[0]

p_msg = ""
for frame in r_frame:
    p_msg += frame[10:(10+int(frame[6:10]))]  # frame[6:10]  - 헤더의 SIZE 정보 / 페이로드 내용
    #p_msg += frame[10:16]
print("restore msg: ", p_msg)
sock.close()

