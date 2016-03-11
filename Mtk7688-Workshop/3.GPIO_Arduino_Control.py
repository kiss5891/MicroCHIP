#coding=utf-8
import serial , time , mraa
s = None
x = mraa.Gpio(44)
x.dir(mraa.DIR_OUT)

def setup():
    global s
    s = serial.Serial("/dev/ttyS0", 57600)

if __name__ == '__main__':
    setup()

while True:
    readVal=repr(s.read())      #將來自ttyS0的值讀出到realVal
    print(readVal[3:5])         #取第第四第五字元來判斷
    if readVal[3:5]=='00':      #如果第四第五字元為00時執行
        x.write(0)              #GPIO(44)切換至High
    else:
        x.write(1)              #GPIO(44)切換至Low
