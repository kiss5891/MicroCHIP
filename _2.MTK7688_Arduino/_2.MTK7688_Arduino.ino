void setup() {
    Serial.begin(115200);         //電腦與MTK7688(Arduino)通道
    Serial1.begin(57600);         //MTK7688(Arduino) & MTK7688(MPU) UART通道
    pinMode(13, OUTPUT);
}
void loop() {
  int c = Serial1.read();         // 讀取來自MTK7688(MPU)值
  if (c != -1) {
  switch(c) {
    case '0':                     // 如果送過來的值為0
      digitalWrite(13, 0);        // pin 13切換至低電位
    break;
    case '1':                     // 如果送過來的值為1
      digitalWrite(13, 1);        // pin 13切換至高電位
    break;
  }
}
}
