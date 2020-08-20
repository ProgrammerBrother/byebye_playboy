from pynput.keyboard import Key, Controller
import clipboard
import time
import os

time.sleep(5)
keyboard = Controller()
controlKey = Key.ctrl if os.name == 'nt' else Key.cmd


def send_message(msg):
    clipboard.copy(msg)
    with keyboard.pressed(controlKey):
        keyboard.press('v')
    keyboard.press(Key.enter)

    time.sleep(0.5)


with open('我想说的话', encoding='UTF-8') as f:
    content = f.readlines()
    for x in content:
        send_message(x.strip())
