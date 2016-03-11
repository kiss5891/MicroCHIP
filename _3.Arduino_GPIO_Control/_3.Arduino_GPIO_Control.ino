const int analogOutPin = 13;
const int analogInPin = A0;  
int sensorValue = 0;       
int outputValue = 0;        

void setup() {
  Serial.begin(9600);
  Serial1.begin(57600);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  outputValue = map(sensorValue, 0, 1023, 0, 255);
  analogWrite(analogOutPin, outputValue);
  Serial.print("sensor = ");
  Serial.print(sensorValue);
  Serial.print("\t output = ");
  Serial.println(outputValue);
  Serial1.write(outputValue);
  delay(2);
}
