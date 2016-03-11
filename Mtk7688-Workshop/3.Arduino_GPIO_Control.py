#coding=utf-8
import serial , time
s = None
def setup():
    global s
    s = serial.Serial("/dev/ttyS0", 57600)  #建立 Smart 7688(ttys0)與 Smart 7688 Arduino 的通道
def loop():
    s.write("1")                            #將值1寫入s
    time.sleep(1)                           #延遲1秒
    s.write("0")                            #將值0寫入s
    time.sleep(1)                           #延遲1秒
if __name__ == '__main__':                  #程式載入的時候就執行
    setup()                                 #執行setup() function
while True:
    loop()
