import numpy as np
import PIL
from PIL import ImageGrab
#import cv2
from directKeys import click, queryMousePosition, PressKey, ReleaseKey, SPACE
import time
import math

# My screen coordinates for the Minesweeper board
board_coords = [37, 157, 1343, 983]
pixel_increment = 42

# RGB values for the differnt colors
#[128, 128, 128] # rgb value for 0
rgbOne = (0, 0, 170) # rgb value for 1
rgbTwo = (75, 110, 75) # rgb value for 2
rgbThree = (170, 0, 0) # rgb value for 3
rgbFour = (0, 0, 85) # rgb value for 4
rgbFive = (85, 0, 0) # rgb value for 5

# Begin the program if mouse position is on the left of the screen
while True:
    mouse_pos = queryMousePosition()
    if mouse_pos.x <= 0:
        break

#def click_middle(screen):
    #click(board_coords[2]/2,board_coords[3]/2)
    
num1s = 0
num2s = 0
num3s = 0
num4s = 0
num5s = 0

print("clicker is ready to go")
while True:
    first_click = [668,603]
    mouse_pos = queryMousePosition()
    screen = np.array(ImageGrab.grab(bbox=board_coords))
    click(first_click[0],first_click[1])
    for x in range (first_click[0]-(pixel_increment*8),first_click[0]+(pixel_increment*8),pixel_increment):
        for y in range (first_click[1]-(pixel_increment*8),first_click[1]+(pixel_increment*8),pixel_increment):
            pixel_rgb = PIL.ImageGrab.grab().load()[x,y]
            
            if pixel_rgb == rgbTwo:
                click(x,y)
                time.sleep(.05)
                
    print("clicker is finished")
    break
    

