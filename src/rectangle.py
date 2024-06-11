import pygame
from pygame import Surface, Rect
from colors import *
from config import (
    BACKGROUND_COLOR, RECT_HEIGHT, SCREEN_HEIGHT, RECT_COLOR, RECT_WIDTH
)
from dataclasses import dataclass



# class Rectangle:
#     def __init__(self, color, value):
#         self.color = color
#         self.value = value
    
#     def __lt__(self, other: 'Rectangle'):
#         return self.height < other.height
    
#     def __gt__(self, other: 'Rectangle'):
#         return self.height > other.height
    
#     def __le__(self, other: 'Rectangle'):
#         return self.height <= other.height
    
#     def __ge__(self, other: 'Rectangle'):
#         return self.height >= other.height
    
#     def swap(self, other: 'Rectangle'):
#         self.color = other.color = RED
#         yield
#         self = 
#         yield
#         self.color = other.color = RECTANGLES_COLOR

#     def replace(self, other: 'Rectangle'):
#         self.color = other.color = RED
#         yield
#         self.height = other.height
#         self.y = SCREEN_HEIGHT - self.height
#         yield
#         self.color = other.color = RECTANGLES_COLOR
        
    

def update_rectangles(rects_list: list[int], screen: Surface, last_modified=[]):
    screen.fill(BACKGROUND_COLOR)
    
    for i, v in enumerate(rects_list):
        pygame.draw.rect(
            screen, RED if last_modified and v in last_modified else RECT_COLOR,
            Rect(
                i*RECT_WIDTH, SCREEN_HEIGHT-v*RECT_HEIGHT,
                RECT_WIDTH, int(v*RECT_HEIGHT)+(v*RECT_HEIGHT > 0
            ))
        )
    pygame.display.update()






