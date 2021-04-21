def frame(start_ch, addr, seq_no, msg):  # 시작문자, 주소, 순서번호, 길이 // (헤더)
    addr = str(addr).zfill(2)
    seq_no = str(seq_no).zfill(4)
    length = str(len(msg)).zfill(4)
    return chr(start_ch) + addr + seq_no + length + msg

if __name__ == "__main__":
    start_ch = 0x05  # 16진수 5
    addr = 2
    seq_no = 1

    msg = input('input msg : ')
    capsule = frame(start_ch, addr, seq_no, msg)
    print(capsule)
