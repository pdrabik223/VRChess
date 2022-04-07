#include <FastLED.h>

template <uint8_t PIN>
class LedStrip
{
    const uint8_t pin = PIN;
    uint32_t no_leds;
    CRGB *leds;

public:
    LedStrip(uint32_t no_leds)
    {
        SetNoLeds(no_leds);
        Fill(CRGB::Black);
    };

    ~LedStrip() { delete[] leds; }

    void Set(uint32_t led_id, const CRGB &color)
    {
        leds[led_id] = color;
    }

    void Update()
    {
        FastLED.show();
    }

    void Fill(CRGB color)
    {
        for (uint32_t i = 0; i < no_leds; i++)
            leds[i] = color;
    }

    void Clear()
    {
        Fill(CRGB::Black);
    }

    uint8_t GetPin() { return pin; }

    uint32_t GetNoLeds() { return no_leds; }

    void SetNoLeds(uint32_t no_leds)
    {
        delete[] leds;
        this->no_leds = no_leds;
        leds = new CRGB[no_leds];
        FastLED.addLeds<NEOPIXEL, PIN>(leds, no_leds); // GRB ordering is assumed
    }
};
/// calculates color present in id point on the rainbow scale <0 to max_id>
CRGB Rainbow(unsigned id, unsigned max_id);
