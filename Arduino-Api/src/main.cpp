/* // Led strip example

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


*/

// Button matrix example
#include "ButtonMatrix.h"
#include <String.h>

uint8_t power_pins_array[] = {13, 12};
uint8_t data_pins_array[] = {7, 8};

ButtonMatrix button_matrix((uint32_t)2, (uint32_t)2, &power_pins_array[0], &data_pins_array[0]);
void setup()
{
  button_matrix.Setup();
}

void loop()
{

  String message = Serial.readStringUntil('\n');
  button_matrix.Scan();
  String answer = "";

  for (uint32_t h = 0; h < button_matrix.GetHeight(); h++)
    for (uint32_t w = 0; w < button_matrix.GetWidth(); w++)
      answer += String(button_matrix.GetState(h, w)) + ' ';

  answer += String(0);
  Serial.write(answer.c_str());
  Serial.write('\n');
}