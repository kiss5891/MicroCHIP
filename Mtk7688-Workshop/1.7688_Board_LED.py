#coding=utf-8
import mraa,time

x = mraa.Gpio(44)       #定義GPIO(44)為x
x.dir(mraa.DIR_OUT)

while True:
    x.write(1)          #將GPIO(44)切換至High
    time.sleep(0.2)     #延遲0.2秒
    x.write(0)          #將GPIO(44)切換至Low
    time.sleep(0.2)     #延遲0.2秒
