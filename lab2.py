# Creating PWM objects
pwm1 = GPIO.PWM(out1, 100)
pwm2 = GPIO.PWM(out2, 100)
pwm3 = GPIO.PWM(out3, 1)

def blinker(channel):
    if channel == 17:
        global pwm1
        pwm = pwm1
    elif channel ==27:
        global pwm2
        pwm = pwm2
    pwm.start(0)
    while 1:
        for dc in range(101):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.005)
        for dc in range(100, -1, -1):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.005)

def kill_blinker(channel):
    if channel == 17:
        global pwm1
        pwm = pwm1

try:
    pwm3.start(50)
    GPIO.add_event_detect(in1, GPIO.RISING, callback=blinker, bouncetime=100)
    GPIO.add_event_detect(in2, GPIO.RISING, callback=blinker, bouncetime=100)
    while 1:
        pass
except KeyboardInterrupt:
    print('\nExiting')
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    GPIO.cleanup()
