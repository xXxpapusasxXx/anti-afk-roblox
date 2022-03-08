import time
import keyboard
import random

random.seed(int(time.strftime("%d%H%m%M%S")))

teclas = ["a","s","d","w","space"]

def teclapressed(tecla, tiempo):
    keyboard.press(tecla)
    time.sleep(tiempo)
    keyboard.release(tecla)

while True:
    teclapressed(random.choice(teclas),random.random())
    time.sleep(random.randint(1, 5))
