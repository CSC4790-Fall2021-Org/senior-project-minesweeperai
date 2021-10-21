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
rgbTwo = (0, 85, 0) # rgb value for 2
rgbThree = (170, 0, 0) # rgb value for 3
rgbFour = (0, 0, 85) # rgb value for 4
rgbFive = (85, 0, 0) # rgb value for 5

rgbClicked = (128, 128, 128) # rgb value for clicked in space
rgbUnclicked = (85, 85, 85) # rgb value for the side of an unknown 
rgbFlag = (58,22,22) # rgb value for the part of a flag my program sees
rgbBomb = (8,8,8) # rgb value of the part of a bomb my program sees


# Begin the program if mouse position is on the left of the screen
while True:
    mouse_pos = queryMousePosition()
    if mouse_pos.x <= 0:
        break

#def click_middle(screen):
    #click(board_coords[2]/2,board_coords[3]/2)
    
gameBoard = [[0 for y in range(16)] for x in range(16)]


num1s = 0
num2s = 0
num3s = 0
num4s = 0
num5s = 0

numFlags = 0
numBombs = 0

countY = 0
countX = 0

print("clicker is ready to go")
while True:
    first_click = [118,324]
    mouse_pos = queryMousePosition()
    screen = np.array(ImageGrab.grab(bbox=board_coords))
    for x in range (first_click[0],first_click[0]+(pixel_increment*16),pixel_increment):
        for y in range (first_click[1],first_click[1]+(pixel_increment*16),pixel_increment):
            pixel_rgb = PIL.ImageGrab.grab().load()[x,y]
            
            click(x,y)
            
            countX = int((x-118)/42)
            countY = int((y-324)/42)
            
            #print(countX)
            #print(countY)
            
            #if KeyboardInterrupt:
                #break

            if pixel_rgb == rgbOne:
                gameBoard[countY][countX] = 1
                num1s += 1
            
            elif pixel_rgb == rgbTwo:
                gameBoard[countY][countX] = 2
                num2s += 1
            
            elif pixel_rgb == rgbThree:
                gameBoard[countY][countX] = 3
                num3s += 1
                
            elif pixel_rgb == rgbFour:
                gameBoard[countY][countX] = 4
                num4s += 1
                
            elif pixel_rgb == rgbFive:
                gameBoard[countY][countX] = 5
                num5s += 1
                
            elif pixel_rgb == rgbFlag:
                gameBoard[countY][countX] = 8
                numFlags += 1
                
            elif pixel_rgb == rgbBomb:
                gameBoard[countY][countX] = 7
                numBombs += 1
                
            elif pixel_rgb == rgbClicked:
                x += 19
                grayRGB = PIL.ImageGrab.grab().load()[x,y]
                if grayRGB == rgbUnclicked:
                    gameBoard[countY][countX] = 9
                else:
                    gameBoard[countY][countX] = 0
                x -= 19
                    
    print(np.matrix(gameBoard))
    
    print("There are " + str(num1s) + " ones.")
    print("There are " + str(num2s) + " twos.")
    print("There are " + str(num3s) + " threes.")
    print("There are " + str(num4s) + " fours.")
    print("There are " + str(num5s) + " fives.")
    
    print("There are " + str(numBombs) + " bombs.")
    print("There are " + str(numFlags) + " flags.")
    
    print("clicker is finished")
    
    
    break























