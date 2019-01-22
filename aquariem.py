import time
from random import randint
from sense_hat import SenseHat
from GridSenseHat import GridSenseHat

white = (255,255,255) # white
black = (0,0,0) # black
dark_blue = (0,0,112) # dark blue
blue = (0,0,255) # blue
orange = (255,128,0) # food

class fish():

        def __init__(self):
                sense = SenseHat()

                x = 0
                y = 0

                w = white
                b = black
                d = dark_blue
                B = blue
                o = orange

                aquariem = [
                [d, d, d, d, d, d, d, d],
                [d, d, d, d, d, d, d, d],
                [d, d, d, d, d, d, d, d],
                [d, d, d, d, d, d, d, d],
                [d, d, d, d, d, d, d, d],
                [d, d, d, d, d, d, d, d],
                [d, d, d, d, d, d, d, d],
                [d, d, d, d, d, d, d, d]
                ]
                sense = GridSenseHat()
                sense.set_pixels(aquariem)
                sense.set_pixel(0,0,255,255,255)



        def move(self,sense):
                sense = SenseHat()
                x = 0
                y = 0
                while True:
                        while(x<8):
                                time.sleep(1)
                                sense.set_pixel(0,0,0,0,255)
                                x = x+1
                else:
                        while(0<x):
                                time.sleep(1)
                                sense.set_pixel(0,0,0,0,255)
                                x = x-1

class food():
        def food(self,sense):
        food_meter = 100
        while True:
                while food_meter > 0:
                        time.sleep(3)
                        food_meter = food_meter - 10
                else:
                        pass


food_meter = 100
        food = orange
        if (25 <= food_meter):
                sense.set_pixel(randint,randint,255,125,0)
        else:
                pass
