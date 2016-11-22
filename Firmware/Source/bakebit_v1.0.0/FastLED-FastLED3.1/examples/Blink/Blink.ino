#include "FastLED.h"

// How many leds in your strip?
#define NUM_LEDS 5
#define DATA_PIN 3
// Define the array of leds
CRGB leds[NUM_LEDS];

#define ROTARY_ANGLE_SENSOR A0
#define ADC_REF 5
#define FULL_ANGLE 360
#define GROVE_VCC 5


void setup() { 
      pinMode(ROTARY_ANGLE_SENSOR, INPUT);
      Serial.begin(115200);
  	  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
     
}

void loop() { 
  int degrees;
  degrees = getDegree();
  //Serial.print("The angle is:");
 // Serial.println(degrees); 
  FastLED.clear(1);
  if(degrees>0)   leds[0] = CRGB::Green;
  if(degrees>72) leds[1] = CRGB::Green;
  if(degrees>144) leds[2] = CRGB::Green;
  if(degrees>216) leds[3] = CRGB::Yellow;
  if(degrees>288)   leds[4] = CRGB::Red;
  if(degrees==360) {leds[0] = CRGB::Red;leds[1] = CRGB::Red;leds[2] = CRGB::Red; leds[3] = CRGB::Red;leds[4] = CRGB::Red;} 
  
  // Turn the LED on, then pause
 // leds[0] = CRGB::Red;
//  leds[1] = CRGB::Yellow;
 // leds[2] = CRGB::Green;
  FastLED.show();
  delay(50);
  
  // Now turn the LED off, then pause
  //leds[0] = CRGB::Green;
  //leds[1] = CRGB::Blue;
 // leds[2] = CRGB::Red;
 // FastLED.show();
  //delay(500);
//  FastLED.clear(1);
  
}


int getDegree()
{
  int sensor_value = analogRead(ROTARY_ANGLE_SENSOR);
  float voltage;
  voltage = (float)sensor_value*ADC_REF/1023;
  float degrees = (voltage*FULL_ANGLE)/GROVE_VCC;
  return degrees;
}
