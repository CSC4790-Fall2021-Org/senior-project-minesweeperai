import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition, PressKey, ReleaseKey, SPACE
import time
import math

board_coords = [37, 157, 1343, 983]

screen = np.array(ImageGrab.grab(bbox=board_coords))
