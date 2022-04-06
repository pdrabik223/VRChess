#include <FastLED.h>

// How many leds in your strip?
#define NUM_LEDS 3
#define DATA_PIN 5

// Define the array of leds
CRGB leds[NUM_LEDS];

void setup()
{
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS); // GRB ordering is assumed
}

void loop()
{
  leds[0] = CRGB::AliceBlue;
  FastLED.show();
  delay(500);
  leds[0] = CRGB::Black;
  FastLED.show();
  delay(500);
  leds[1] = CRGB::AliceBlue;
  FastLED.show();
  delay(500);
  leds[1] = CRGB::Black;
  FastLED.show();
  delay(500);

  leds[2] = CRGB::AliceBlue;
  FastLED.show();
  delay(500);
  leds[2] = CRGB::Black;
  FastLED.show();
  delay(500);
}
