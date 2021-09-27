import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# input port numbers
in1, in2 = 17, 27

# output port numbers
out1, out2, out3 = 16, 20, 21

GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)

# Creating PWM object
pwm_flash = GPIO.PWM(out3)

def blinker(channel):
    if channel == in1:
        pwm = GPIO.PWM(out1)
    elif channel == in2:
        pwm = GPIO.PWM(out2)
    else:
        return
    pwm.start(0)
    while 1:
        for dc in range(101):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.005)
            if not GPIO.input(channel):
                break
        for dc in range(100, -1, -1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.005)
            if not GPIO.input(channel):
                break
    pwm.stop()

try:
    pwm_flash.start(0)
    GPIO.add_event_detect(in1, GPIO.RISING, callback=blinker, bouncetime=100)
    GPIO.add_event_detect(in2, GPIO.RISING, callback=blinker, bouncetime=100)
    while 1:
        pwm_flash.ChangeDutyCycle(0)
        time.sleep(0.5)
        pwm_flash.ChangeDutyCycle(100)
        time.sleep(0.5)
except KeyboardInterrupt:
    print('\nExiting')
finally:
    GPIO.cleanup()
