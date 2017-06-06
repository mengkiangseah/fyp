import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    while True:
        GPIO.wait_for_edge(27, GPIO.RISING)
        print("Connected.")
        time.sleep(0.5)
        GPIO.wait_for_edge(27, GPIO.FALLING)
        print("Disconnected.")
        time.sleep(0.5)

if __name__ == '__main__':
    main()
