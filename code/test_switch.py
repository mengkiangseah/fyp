import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    while True:
        GPIO.wait_for_edge(27, GPIO.RISING)
        print("Detected.")

if __name__ == '__main__':
    main()
