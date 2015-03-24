unsigned int ticks = 0;
const int sensorPin = 2;

void tick() {
  ticks++;
}
void setup() {
  pinMode(sensorPin, INPUT);
  attachInterrupt(0,tick,RISING);
  Serial.begin(9600);
}

void loop() {
  ticks = 0;
  delay(1000);
  unsigned int tmp_ticks = ticks;
  float wind = 0.07881 * tmp_ticks + 0.32;
  Serial.println(wind);
}
