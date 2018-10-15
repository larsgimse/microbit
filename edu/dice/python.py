from microbit import *
import random
import time

dice0 = Image("00000:00000:00000:00000:00000")
dice1 = Image("00000:00000:00900:00000:00000")
dice2 = Image("00000:00090:00000:09000:00000")
dice3 = Image("00000:09000:00900:00090:00000")
dice4 = Image("00000:09090:00000:09090:00000")
dice5 = Image("00000:09090:00900:09090:00000")
dice6 = Image("00000:09090:09090:09090:00000")

all_dice = [dice1, dice2, dice3, dice4, dice5, dice6]

random.seed(1337) #https://microbit-micropython.readthedocs.io/en/latest/tutorials/random.html

while True:
    if button_a.was_pressed():
        display.show(all_dice, delay=200, clear=True)
        display.show(random.choice(all_dice))
