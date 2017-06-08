int clockPin = 3; // Analoog
int dataPin = 4;   // Analoog

void setup() {
  // put your setup code here, to run once:
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  shiftOut(dataPin, clockPin, LSBFIRST, B00001111);

}

void loop() {
  // put your main code here, to run repeatedly:
  shiftOut(dataPin, clockPin, LSBFIRST, B00001111);
}
