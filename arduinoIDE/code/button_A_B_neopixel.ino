#include <Adafruit_NeoPixel.h>

#define PIN 0

const int buttonA = 5;     // the number of the pushbutton pin
const int buttonB = 11;     // the number of the pushbutton pin

Adafruit_NeoPixel strip = Adafruit_NeoPixel(72, PIN, NEO_GRBW + NEO_KHZ800);
 
void setup() {  
  Serial.begin(9600);
  
  Serial.println("microbit is ready!");
  
  pinMode(buttonA, INPUT);  
  pinMode(buttonB, INPUT);
  
  strip.begin();
  strip.show();  
}
 
void loop(){
  if (! digitalRead(buttonA)) {
    Serial.println("Button A pressed");
    colorWipe(strip.Color(255, 0, 0), 50);
  }
  if (! digitalRead(buttonB)) {
    Serial.println("Button B pressed");
    colorWipe(strip.Color(0, 255, 0), 50);
  }
  delay(10);
}

void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}
