import pygame
from pygame import Surface, Rect
from colors import *
from config import BACKGROUND_COLOR, SCREEN_HEIGHT, RECTANGLES_COLOR
from dataclasses import dataclass


class Rectangle(Rect):
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
    
    def __lt__(self, other: 'Rectangle'):
        return self.height < other.height
    
    def __gt__(self, other: 'Rectangle'):
        return self.height > other.height
    
    def __le__(self, other: 'Rectangle'):
        return self.height <= other.height
    
    def __ge__(self, other: 'Rectangle'):
        return self.height >= other.height
    
    def swap(self, other: 'Rectangle'):
        self.color = other.color = RED
        yield
        self.height, other.height = other.height, self.height
        self.y = SCREEN_HEIGHT - self.height
        other.y = SCREEN_HEIGHT - other.height
        yield
        self.color = other.color = RECTANGLES_COLOR

    def replace(self, other: 'Rectangle'):
        self.color = other.color = RED
        yield
        self.height = other.height
        self.y = SCREEN_HEIGHT - self.height
        yield
        self.color = other.color = RECTANGLES_COLOR
        
    

def update_rectangles(rects: list[Rectangle], screen: Surface):
    screen.fill(BACKGROUND_COLOR)
    for rect in rects:
        pygame.draw.rect(screen, rect.color, rect)
    pygame.display.update()






