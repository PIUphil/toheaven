from pop import Leds, PiezoBuzzer, Oled, PixelDisplay
from pop import Switches, Potentiometer, Sound, Cds, Psd, Gesture
from pop import Sht20 as TempHumi
from pop import PopThread

import time

def led_test():
    leds = Leds()
    leds.allOn()
    time.sleep(1)
    leds.allOff()
    time.sleep(1)

    for i in range(8):
        leds[i].on()
        time.sleep(.5)
        leds[i].off()
        time.sleep(.5)

def piezo_buzzer_test():
    buzzer = PiezoBuzzer()
    
    buzzer.setTempo(120)
    buzzer.tone(4, 1, 4)  # 도
    buzzer.tone(4, 3, 4)  # 레
    buzzer.tone(4, 5, 4)  # 미
    buzzer.tone(4, 6, 4)  # 파
    buzzer.tone(4, 8, 4)  # 솔
    buzzer.tone(4, 10, 4) # 라
    buzzer.tone(4, 12, 4) # 시
    buzzer.tone(5, 1, 4)  # 도 ^

#piezo_buzzer_test()
# 타이밍이 안좋음. -> MCU는 하나만 돌려서 좀더 정확하고 깔끔하게 buzzer 가능 
# 주파수 폭 변조 pwm

def oled_test():
    oled = Oled()
    
    print(oled.width(), oled.height())
    
    oled.drawCircle(60,30,10,oled.WHITE)
    time.sleep(1)
    oled.fillCircle(60,30,10,oled.WHITE)
    time.sleep(1)
    oled.clearDisplay()

# 128x60  width, height
    
def pixel_display_test():
    pixel = PixelDisplay()
    
    # pixel.setBrightness(10)
    # pixel.fill([255,0,0])
    # time.sleep(1)
    
    # pixel.setBrightness(15)
    # for y in range(8):
    #     for x in range(8):
    #         pixel.setColor(x, y, [255,255,0])    # 리스트 느려서 x -> 넘파이 o
    #         time.sleep(.1)
    
    pixel.rainbow()
    pixel.clear()

#pixel_display_test()

def on_switch(sw):
    print("sw2 press" if sw.read() else "sw2 unpress")
    
def switchs_test():
    from pop import Switch, Input
    sw1 = Switch(7, True) # Bug (disable interrupted)   # 스위치 1번
    sw2 = Switch(27, True)                              # 하드웨어 핀번호 GPI
    sw2.setCallback(on_switch, sw2)  # 콜백 / 인터럽트 -> 이벤트발생

    sw1_old = False                 # 이 아래... 폴링 방식
    while True:
        try:
            ret = sw1.read()
            if sw1_old != ret:
                sw1_old = ret
                print("sw1 press" if ret else "sw1 unpress")
            time.sleep(.1)
        except KeyboardInterrupt:
            break
        
def on_potentiometer(val):
    print("%d"%(val))
    time.sleep(.1)    # 민감도

def potentiometer_test():
    poten = Potentiometer()
    poten.setRangeTable([144, 629, 1112, 1621, 2085, 2642, 3158, 3590, 3992, 4094])
                    # 필수로 적어줘야 함 (0~10단계) - 저항값
                    # 픽셀 디스플레이 밝기에 맞춰줄 수 있다
    poten.setCallback(on_potentiometer)
    input("Press <ENTER> key...\n")
    poten.stop()


def on_sound(val):
    ret = abs(val - (4096//2 + 12))  # 4096: 소리크기 / 2: '+','-' / 12: 백색소음(조용한 환경속에서 0이 되도록 조절)-캘리그레이션..?
    if ret > 10:                     # abs 절댓값, '-'값 없앰
        print(ret)
    
def sound_test():
    sound = Sound()
    
    sound.setCallback(on_sound, type=Sound.TYPE_AVERAGE)
    input("Press <ENTER> key...\n")
    sound.stop()


def on_cds(val):    # 슈미드트리거...
    print(val)

def cds_test():
    cds = Cds()
    
    cds.setCallback(on_cds, type=Cds.TYPE_AVERAGE)
    input("Press <ENTER> key...\n")
    cds.stop()
    

def temp_humi_test():
    temphumi = TempHumi()

    while True:
        try:
            print(round(temphumi.readTemp(),1), round(temphumi.readHumi(),1))    
            time.sleep(.5)
        except KeyboardInterrupt:
            break
    
    # 대기 온도 측정 - 둔감함. 체온 측정 어려움

def on_psd(psd):
    def wrapper(val):
        print(psd.calcDist(val), "cm")  # 최소거리 8cm
        time.sleep(.1)
    return wrapper

def psd_test():         
    psd = Psd()     
                                 # 클로저  # 거리에 따른 전압비율
    psd.setCallback(on_psd(psd))   
    input("Press <ENTER> key...\n")  
    psd.stop()


class MyGesture(PopThread):
    def __init__(self):
        self.__gesture = Gesture()
        
    def run(self):                  # run은 고치면 안됨(쓰레드 콜백)
        if self.__gesture.isAvailable():
            print(self.__gesture.read())

def gesture_test():
    gesture = MyGesture()
    
    gesture.start()
    input("Press <ENTER> key...\n")  
    gesture.stop()
    
        
if __name__ == "__main__":
    pass