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
    readVal=repr(s.read())
    print(readVal[3:5])
    if readVal[3:5]=='00':
        x.write(0)
    else:
        x.write(1)
