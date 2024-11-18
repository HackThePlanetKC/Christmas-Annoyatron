import machine
import time
import random

# Pin definitions
button_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
led_pin = machine.Pin(14, machine.Pin.OUT)

# Function to toggle the LED
def toggle_led():
    led_pin.value() ^= 1

# Main loop
while True:
    if button_pin.value() == 0:
        toggle_led()
        while button_pin.value() == 0:
            pass  # Debounce

# Delayed loop
initial_delay = 7 * 24 * 60 * 60  # 1 week in seconds
subsequent_delay = random.randint(1, 4) * 24 * 60 * 60  # 1-4 days in seconds

time.sleep(initial_delay)
while True:
    # Do something in this loop, e.g., control other LEDs, sensors, etc.
    time.sleep(subsequent_delay)
    subsequent_delay = random.randint(1, 4) * 24 * 60 * 60
