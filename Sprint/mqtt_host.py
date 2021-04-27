import paho.mqtt.client as mqtt
import threading
import json

def __task_publish(client):
    import time
    time.sleep(0.7)
    led_info = {'id':None, 'led':None, 'action':None}
    led_info['id'] = int(input("Target ID: "))
    led_info['led'] = int(input("LED: "))
    led_info['action'] = input("Action: ")
    client.publish("SODA/led/action", json.dumps(led_info))
    

def do_connect(client, usrdata, flags, rc):
    if rc == 0:
        print("ok connect")
        client.subscribe("SODA/led/state") 
        threading.Thread(target=__task_publish, args=(client,)).start()
    else:
        print("not connect")


def do_publish(client, usrdata, mid):
    threading.Thread(target=__task_publish, args=(client,)).start()


def do_message(client, usrdata, message):
    print(' ' * 20, "<<<", message.payload.decode())
    

def main():
    client = mqtt.Client() 
    client.on_connect = do_connect
    client.on_publish = do_publish
    client.on_message = do_message
    client.connect("192.168.101.101")  #실제 브로커 주소 사용
    client.loop_forever()

if __name__ == "__main__":
    main()