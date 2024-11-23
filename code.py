import board
import pwmio
import digitalio
import time
import random

# Pin definitions
button = digitalio.DigitalInOut(board.D0)
button.direction = digitalio.Direction.INPUT
#button.pull = digitalio.Pull.UP       # Uncomment this line if you want to use a digital pull up

led = digitalio.DigitalInOut(board.D1)
led.direction = digitalio.Direction.OUTPUT

# PWM setup for buzzer (adjust frequency and duty cycle as needed)
pwm = pwmio.PWMOut(board.D2, frequency=12000, duty_cycle=2**15 // 2)  # 50% duty cycle

# Function to toggle the LED
def toggle_led():
    led.value = not led.value
    
# Main loop
while True:
    if not button.value:
        toggle_led()
        while not button.value:
            pass  # Debounce

# Delayed loop
initial_delay = 7 * 24 * 60 * 60  # 1 week in seconds
subsequent_delay = random.randint(1, 4) * random.randint(1, 24) * random.randint(1, 60) * random.randint(1, 60)  # 1-4 days in seconds

time.sleep(initial_delay)
while True:
    # Activate the buzzer for 0.5 seconds
    pwm.duty_cycle = 2**15 // 2  # 50% duty cycle for 12000 Hz
    time.sleep(0.5)
    pwm.duty_cycle = 0  # Turn off the buzzer

    time.sleep(subsequent_delay)
    subsequent_delay = random.randint(1, 4) * random.randint(1, 24) * random.randint(1, 60) * random.randint(1, 60)
