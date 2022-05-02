// Led strip example

// #include "LedStrip.h"

// LedStrip<5> led_strip(8);

// void setup()
// {
//   led_strip.Clear();

//   for (uint32_t j = 0; j < led_strip.Size(); j++)
//     led_strip.Set(j, CRGB::Beige);
//   led_strip.Update();
// }

// void loop()
// {
//   delay(1000);
// }

// Button matrix example
#include "ButtonMatrix.h"
#include <String.h>
#include "LedStrip.h"

LedStrip<11> led_strip(8);

uint8_t power_pins_array[] = {2, 4};
ButtonMatrix button_matrix((uint32_t)2, (uint32_t)2, &power_pins_array[0], A0);
void setup()
{

  led_strip.TurnRainbowOnAnimation(100);

  button_matrix.Setup();
  Serial.begin(115200);
  Serial.write("ready\n");
}
void loop()
{
  String message = Serial.readStringUntil('\n');

  String answer = "0: " + button_matrix.power_pins_array[0];
  answer += " ";
  button_matrix.SetStripState(0, HIGH);
  answer += button_matrix.Scan();

  answer += "1: " + button_matrix.power_pins_array[1];
  answer += " ";
  button_matrix.SetStripState(1, HIGH);
  answer += button_matrix.Scan();

  Serial.write(answer.c_str());
  Serial.write('\n');
  delay(100);
}

/*
#include <Arduino.h>
#include <String.h>
#include "LedStrip.h"
LedStrip<5> led_strip(4);
CRGB ParseColor(String color_str);

#include "ButtonMatrix.h"
#include <String.h>

uint8_t power_pins_array[] = {13, 12};
uint8_t data_pins_array[] = {A0};

ButtonMatrix button_matrix((uint32_t)2, (uint32_t)2, &power_pins_array[0], &data_pins_array[0]);

uint32_t HandleChar(const char c);
uint32_t ToDecimal(const String &color_str);

void setup()
{
  Serial.begin(115200);
  Serial.write("ready\n");
  led_strip.Fill(CRGB::Green);
  led_strip.Update();
}
void loop()
{
  if (Serial.available())
  {

    String message = Serial.readStringUntil('\n');
    if (message.substring(0, 3) == "set")
    {
      // set board colors
      message.remove(0, 3);
      for (uint32_t i = 0; i < led_strip.Size(); i++)
      {
        String color_str = message.substring(i * 7, 6);
        CRGB color = ParseColor(color_str);
        led_strip.Set(i, color);
      }
      led_strip.Update();
      // Serial.print(1);
      Serial.write("ok\n");
    }
    else if (message.substring(0, 3) == "get")
    {

      // set board state
      message.remove(0, 3);
      Serial.print(0);
      Serial.print('\n');
    }
    // Serial.print('\n');
  }
  else
  {

    button_matrix.Scan();
  }
  // Serial.print("ok\n");
}

CRGB ParseColor(String color_str)
{
  uint8_t r, g, b;
  // incoming data looks as follows:
  // e.g. e5g8ab
  // these are 3 256 bit numbers encoded in base 16 and passed together
  // if one og these is < 16 string would look like:
  // 01b700
  // always 6 characters long

  color_str.toUpperCase();
  // to prepate for base 16 to base 10 conversion
  r = ToDecimal(color_str.substring(0, 2));
  g = ToDecimal(color_str.substring(2, 4));
  b = ToDecimal(color_str.substring(4, 6));
  return CRGB(r, g, b);
}

uint32_t HandleChar(const char c)
{
  if (c >= '0' && c <= '9')
    return (int)c - '0';
  else
    return (int)c - 'A' + 10;
}

// Function to convert a number from base 16 to base 10
// to decimal
uint32_t ToDecimal(const String &color_str)
{
  int len = color_str.length();
  int power = 1; // Initialize power of base
  int num = 0;   // Initialize result
  int i;

  // Decimal equivalent is str[len-1]*1 +
  // str[len-2]*base + str[len-3]*(base^2) + ...
  for (i = len - 1; i >= 0; i--)
  {
    // A digit in input number must be
    // less than number's base
    if (HandleChar(color_str[i]) >= 16)
    {
      return -1;
    }

    num += HandleChar(color_str[i]) * power;
    power = power * 16;
  }

  return num;
}
*/