from __future__ import print_function
import RPi.GPIO as GPIO
import time
import subprocess


def play_audio():
    audio = '/home/pi/app/bbq.mp3'
    print('playing {}'.format(audio))
    subprocess.call(['mpg321', audio])


def listen_for_switch():
    """Continuously listens for state change of GPIO"""
    pin_number = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        while True:
            pin_current = GPIO.input(pin_number)
            if pin_current == 1:
                play_audio()
            while GPIO.input(pin_number) == pin_current:
                time.sleep(1)
    except KeyboardInterrupt:
	    GPIO.cleanup()


if __name__ == '__main__':
    listen_for_switch()
