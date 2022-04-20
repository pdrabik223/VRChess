/// Handles button pres detection
/// Can by multiplexing over provided connections
/// Library is Arduino specific
#include <stdint.h>
#include <assert.h>

#include <Arduino.h>

struct PinState
{

    inline static uint8_t High = 1;
    inline static uint8_t Low = 0;
    static uint8_t Not(uint8_t state)
    {
        if (state == 0)
            return PinState::High;
        else
            return PinState::Low;
    }
};

class ButtonMatrix
{
    // button matrix height (no_buttons in height)
    uint32_t height;
    // button matrix width (no_buttons in width), number of pins used as output
    uint32_t width;
    // pins used as outputs (array length must mach width parameter)
    uint8_t *power_pins_array;
    // pins used as inputs  (array length must mach height parameter)
    uint8_t *data_pins_array;
    // button current states, has length of height * width
    bool *button_matrix;

public:
    uint32_t no_debouncer_measurements = 100;
    ButtonMatrix(const uint32_t height,
                 const uint32_t width,
                 uint8_t *power_pins_array,
                 uint8_t *data_pins_array) : width(width), height(height)
    {
        /// constructs ButtonMatrix object, in main file should be constructed
        /// as global object
        /// @param width button matrix width (no_buttons in width)
        /// @param height button matrix height (no_buttons in height)
        /// @param power_pins_array pins used as outputs (array length must mach width parameter)
        /// @param data_pins_array pins used as inputs  (array length must mach height parameter)
        /// @note passed pins must be addresable pins on your board

        this->power_pins_array = new uint8_t[width];
        for (uint32_t i = 0; i < width; i++)
            this->power_pins_array[i] = power_pins_array[i];

        this->data_pins_array = new uint8_t[height];
        for (uint32_t i = 0; i < height; i++)
            this->data_pins_array[i] = data_pins_array[i];

        button_matrix = new bool[width * height];
        for (uint32_t i = 0; i < width * height; i++)
            button_matrix[i] = false;

        // memmove(power_pins_array, this->power_pins_array, width);
    };
    void Setup()
    {
        /// SEt up function should be invoked in the "setup()" function
        for (uint32_t i = 0; i < width; i++)
            pinMode(power_pins_array[i], OUTPUT);

        for (uint32_t i = 0; i < height; i++)
            pinMode(data_pins_array[i], INPUT);
    }
    void Scan()
    {
        /// scans buttons and updates button matrix field with new states
        /// this function might take a while to excute
        for (uint32_t w = 0; w < width; w++)
        {
            SetStripState(w, PinState::High);
            ReadStripState(w);
        }
        button_matrix[3] = true;
    }

    bool GetState(const uint32_t w, const uint32_t h)
    {
        return button_matrix[Conv1d(w, h)];
    }

    uint32_t GetHeight()
    {
        return height;
    }
    uint32_t GetWidth()
    {
        return width;
    }

private:
    void SetStripState(const uint32_t w, const uint8_t state)
    {
        for (uint32_t i = 0; i < width * height; i++)
            digitalWrite(power_pins_array[i], PinState::Not(state));

        for (uint32_t h = 0; h < height; h++)
            digitalWrite(power_pins_array[h], state);
    }
    void ReadStripState(const uint32_t w)
    {

        uint8_t debouncer_array[height];
        for (uint32_t i = 0; i < no_debouncer_measurements; i++)
            for (uint32_t h = 0; h < height; h++)
                debouncer_array[h] += digitalRead(data_pins_array[Conv1d(w, h)]);

        for (uint32_t h = 0; h < height; h++)
            if (float(debouncer_array[h]) / no_debouncer_measurements > 0.5)
                button_matrix[Conv1d(w, h)] = true;
            else
                button_matrix[Conv1d(w, h)] = false;
    }

    uint32_t Conv1d(const uint32_t h, const uint32_t w)
    {
        assert(h < height && w < width);
        return h * width + w;
    }
};
