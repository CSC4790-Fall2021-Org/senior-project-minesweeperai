import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition, PressKey, ReleaseKey, SPACE
import time
import math

# My screen coordinates for the Minesweeper board
board_coords = [37, 157, 1343, 983]

# RGB values for the differnt colors
#[189, 189, 189] # rgb value for 0
#[0, 33, 245] # rgb value for 1
#[53, 120, 32] # rgb value for 2
#[234, 50, 35] # rgb value for 3
#[5, 0, 123] # rgb value for 4
#[123, 1, 0] # rgb value for 5

# Begin the program if mouse position is on the left of the screen
while True:
    mouse_pos = queryMousePosition()
    if mouse_pos.x <= 0:
        break

def click_middle(screen):
    click(board_coords[2]/2,board_coords[3]/2)

print("clicker is ready to go")
while True:
    screen = np.array(ImageGrab.grab(bbox=board_coords))
    click_middle(screen)
    break
    

