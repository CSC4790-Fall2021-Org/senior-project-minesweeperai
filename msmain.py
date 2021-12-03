import numpy as np
import PIL
from PIL import ImageGrab
#import cv2
from directKeys import click, queryMousePosition, PressKey, ReleaseKey, SPACE, moveMouseTo
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
rgbFlag = (139,6,6) # rgb value for the part of a flag my program sees
rgbBomb = (0,0,0) # rgb value of the part of a bomb my program sees

imp = [319,144]
load = [153,498]

current = 0

num1s = 0
num2s = 0
num3s = 0
num4s = 0
num5s = 0

numFlags = 0
numBombs = 0

countY = 0
countX = 0

finished = False   
    
def scanBoard(): #scans a small board and returns a 2d array with the current game board
    num1s = 0
    num2s = 0
    num3s = 0
    num4s = 0
    num5s = 0

    numFlags = 0
    numBombs = 0

    countY = 0
    countX = 0

    for x in range (first_click[0],first_click[0]+(pixel_increment*9),pixel_increment):
        for y in range (first_click[1],first_click[1]+(pixel_increment*9),pixel_increment):
            pixel_rgb = PIL.ImageGrab.grab().load()[x,y]
            
            countX = int((x-82)/42)
            countY = int((y-310)/42)
            
            moveMouseTo(x,y)
            #PressKey(SPACE)
            #ReleaseKey(SPACE)

            
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
                
    return gameBoard
                
                
def pressSpacebar(x,y): #marks a mine or clears the board
    moveMouseTo(x,y)
    time.sleep(0.05)
    PressKey(SPACE)
    time.sleep(0.05)
    ReleaseKey(SPACE)
    
           
                  
def scanNeighbours(board, xCounter, yCounter): #returns number of empty squares around a square
    blankCount = 0    
    for i in range(xCounter-1, xCounter+2):
        for j in range(yCounter-1, yCounter+2):
            if 16 > i >= 0 and 16 > j >= 0:
                if board[j][i] == 9:
                    blankCount += 1
    return blankCount

def arrayToPixel(x,y): #converts board array indices to pixels
    pixelCoords = [0,0]
    first = (x*pixel_increment)+82
    second = (y*pixel_increment)+310
    pixelCoords = [first,second]
    return pixelCoords
    
# Begin the program if mouse position is on the left of the screen
while True:
    mouse_pos = queryMousePosition()
    if mouse_pos.x <= 0:
        time.sleep(1)
        break
    
gameBoard = [[0 for y in range(9)] for x in range(9)]


print("clicker is ready to go")

middle = [251, 481]

numBlanks = 0;


while True:
    first_click = [82,310]
    mouse_pos = queryMousePosition()
    screen = np.array(ImageGrab.grab(bbox=board_coords))
    
    moveMouseTo(first_click[0]+3*pixel_increment, first_click[1]+2*pixel_increment) 
    
    click(middle[0],middle[1])
    
    board = scanBoard()
    
    print(np.matrix(board))
    wait = 0
    
    for x in range(10):
        pressSpacebar(first_click[0]+3*pixel_increment, first_click[1]+2*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+8*pixel_increment, first_click[1]+2*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+6*pixel_increment, first_click[1]+5*pixel_increment)
        time.sleep(wait)    
        pressSpacebar(first_click[0]+5*pixel_increment, first_click[1]+6*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+1*pixel_increment, first_click[1]+8*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+1*pixel_increment, first_click[1]+7*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+1*pixel_increment, first_click[1]+5*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+2*pixel_increment, first_click[1]+1*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+7*pixel_increment, first_click[1]+3*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+2*pixel_increment, first_click[1]+6*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+6*pixel_increment, first_click[1]+7*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+1*pixel_increment, first_click[1]+6*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+8*pixel_increment, first_click[1]+6*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+8*pixel_increment, first_click[1]+8*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+0*pixel_increment, first_click[1]+7*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+0*pixel_increment, first_click[1]+0*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+7*pixel_increment, first_click[1]+6*pixel_increment)
        time.sleep(wait)
        pressSpacebar(first_click[0]+7*pixel_increment, first_click[1]+6*pixel_increment)
        
        click(imp[0],imp[1])
        click(load[0],load[1])
        wait += 0.01

    
    
# =============================================================================
#     for x in range(0,8):
#         for y in range(0,8):
#             current = board[y][x]
#             print(current)
#             if current != 9 and current != 0:
#                 blanksAround = scanNeighbours(board, x, y)
#                 if blanksAround == current:
#                     for i in range(x-1, x+2):
#                         for j in range(y-1, y+2):
#                             if board[j][i] == 9:
#                                 board[j][i] = 8
#                                 mine = arrayToPixel(j, i)
#                                 pressSpacebar(mine[0], mine[1])
#                                 print(np.matrix(board))
# =============================================================================
                                
    print("clicker is finished")
    
    break














