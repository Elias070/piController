int clockPin = 3; // Digital
int dataPin = 4;   // Digital

void setup() {
  // put your setup code here, to run once:
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  //shiftOut(dataPin, clockPin, LSBFIRST, B00000000);

}

void loop() {
  // put your main code here, to run repeatedly:
  shiftOut(dataPin, clockPin, LSBFIRST, B10010001);
  delay(10);
}
