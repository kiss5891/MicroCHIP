
void setup() {
  pinMode(13, OUTPUT);      //定義13pin為輸出腳位
}

void loop() {
  digitalWrite(13, HIGH);   //第13pin 狀態轉為High
  delay(1000);              //延遲一秒
  digitalWrite(13, LOW);    //第13pin 狀態轉為Low
  delay(1000);              //延遲一秒
}
