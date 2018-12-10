#include <Ultrasonic.h>

Ultrasonic ultrasonic(9, 10); // ultrasonic(trigger, echo)

float distance, height;
unsigned long startMillis;
unsigned long currentMillis;

const unsigned long interval = 1250; // read data interval

void setup()
{
  Serial.begin(9600);
  ultrasonic.setTimeout(45000UL);
  startMillis = millis();
}

void loop()
{
  unsigned long currentMillis = millis();
  // printing if statement
  if (currentMillis - startMillis >= interval)
  {
    distance = (ultrasonic.read() * 1.38 / 1.52); //data jarak dibaca
    height = 15 - distance;                       //angka inisial disesuaikan dengan ketinggian baki
    //Serial.print("Distance (cm): ");
    Serial.println(height); //data ketinggian air ditulis
    startMillis = currentMillis;
  }
}
