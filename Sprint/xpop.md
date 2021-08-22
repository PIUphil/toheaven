```
import pop

def caller(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, "(", args, ")", end=', ')
        ret = func(*args, **kwargs)
        print(ret)
        return ret
    return wrapper

class Out(pop.Out):
    def __init__(self, n):
        print("create Out")
        super().__init__(n)
        
    def __del__(self):
        print("delete Out")
        super().__del__()
    
    @caller
    def on(self):
        super().on()

    @caller
    def off(self):
        print("call Out.off")
        super().off()

class Led(Out, pop.Led):
    def __init__(self, n):
        print("create Led")
        Out.__init__(self, n)
    
    def __del__(self):
        print("delete Led")
        super().__del__()
    
    @caller    
    def blink(self, period, second):
        super().blink(period, second)

class Leds(pop.Leds):    
    def __init__(self, led=None, debug=False):
        print("create Leds")
        self._max = pop.pinMax(pop.LED)
        
        for i in range(self._max):
            pin = pop.pinMap(pop.LED, i)

            if pin is 0xFF:
                self._leds = [None]
                break

            else:
                if debug:
                    print("Led Pin: %d" % pin)
                self._leds.append(Led(pin))
    
    @caller
    def __getitem__(self, item):
        return super().__getitem__(item)
    
    @caller    
    def allOn(self):
        super().allOn()

    @caller
    def allOff(self):
        super().allOff()

if __name__ == "__main__":
    import time
    
    leds = Leds()
    leds.allOn()
    time.sleep(2)
    for i in range(8):
        leds[i].off()
        time.sleep(.5)
```
