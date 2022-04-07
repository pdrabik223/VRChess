#include "LedStrip.h"
// provided led strip has 300 leds
LedStrip<5> led_strip(300);
void setup()
{
  led_strip.Clear();
}

void loop()
{
  for (uint32_t i = 0; i < led_strip.GetNoLeds() - 30; i++)
  {
    led_strip.Clear();
    for (uint32_t j = 0; j < 30; j++)
      led_strip.Set(i + j, Rainbow(j, 30));
    led_strip.Update();
    delay(100);
  }
}