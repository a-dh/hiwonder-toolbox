#!/usr/bin/env python3

import logging
import logging.handlers
import os, sys, time
import RPi.GPIO as GPIO

key1_pin = 33
key2_pin = 16

def reset_wifi():
    os.system("rm /etc/Hiwonder/* -rf > /dev/null 2>&1")
    os.system("systemctl restart hw_wifi.service > /dev/null 2>&1")

if __name__ == "__main__":

    my_logger = logging.getLogger('hw_button_scan')
    my_logger.setLevel(logging.DEBUG)

    handler = logging.handlers.SysLogHandler(address = '/dev/log')

    my_logger.addHandler(handler)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(key1_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(key2_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    key1_pressed = False
    key2_pressed = False
    count = 0
    while True:
        if GPIO.input(key1_pin) == GPIO.LOW:
            time.sleep(0.05)
            if GPIO.input(key1_pin) == GPIO.LOW:
                if key1_pressed == False:
                    key1_pressed = True
                    count = 0
                else:
                    count += 1
                    if count >= 40:
                        count = 0
                        key1_pressed = False
                        my_logger.info('Key 1 pressed for a while')
                        reset_wifi()
            else:
                count = 0
                key1_pressed = False
                continue
        elif GPIO.input(key2_pin) == GPIO.LOW:
            time.sleep(0.05)
            if GPIO.input(key2_pin) == GPIO.LOW:
                if key2_pressed == False:
                    key2_pressed = True
                    count = 0
                else:
                    count += 1
                    if count >= 40:
                        count = 0
                        key2_pressed = False
                        my_logger.info('Key 2 pressed for a while: shutdown')
                        os.system('sync')
                        os.system('sudo poweroff -f -p')
            else:
                count = 0
                key2_pressed = False
                continue
        else:
            count = 0
            key1_pressed = False
            key2_pressed = False
            time.sleep(0.05)

        
