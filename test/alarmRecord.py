import numpy as np
from datetime import datetime

now = datetime.now().strftime("%y%m%d %H:%M:%S")


# 새로운 알람 기록
newAlarm = np.array([])
ll = np.array(list("a"+str(i) for i in reversed(range(147))))

for line in ll:
    newAlarm = np.append(newAlarm, now + " " + line)
#print(newAlarm)


# 기존 기록 가져오기
oldAlarm = np.array([])
with open('tt.csv', 'r+') as f:
    for line in f.readlines():
        oldAlarm = np.append(oldAlarm, line)
# print(oldAlarm)


# 새 기록 뒤에 기존 기록 붙이기
alarm = np.append(newAlarm, oldAlarm)
# 50줄 이상이면 삭제
if len(alarm)>50:
    alarm = alarm[:50]


# 파일에 알람기록 덮어쓰기
with open('tt.csv', 'w') as f:
    for i in alarm:
        f.write(i+"\n")

print(len(alarm))
# print(alarm)
