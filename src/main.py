import pygame
import random
from colors import *
from config import (
    LIST_LENGTH, RECT_WIDTH, RECT_HEIGHT,
    SCREEN_HEIGHT, SCREEN_WIDTH,
    RECTANGLES_COLOR, FINISHED_RECTANGLES_COLOR
)
from rectangle import Rectangle, update_rectangles
from sorts import bubble_sort, gnome_sort, merge_sort, selection_sort, shaker_sort, comb_sort, insertion_sort, shell_sort
from time import time


height_list = list(range(LIST_LENGTH, 0, -1))

def start_sorting(sort, rects_list, screen):
    sorting_generator = sort(rects_list)

    start = time()
    
    running = True
    
    finished = False
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: running = False     
        
        if not finished:
            pygame.display.set_caption(f'{sort.__name__} {(time() - start):.2f}')
        
        try:
            next(sorting_generator)
        except StopIteration:
            finished = True
            for rectangle in rects_list:
                rectangle.color = FINISHED_RECTANGLES_COLOR
                update_rectangles(rects_list, screen)
                pygame.time.wait(500//LIST_LENGTH)
            break
        update_rectangles(rects_list, screen)
    print(pygame.display.get_caption()[0])

def main(*sorting_algotythms):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    for algorythm in sorting_algotythms:
        random.shuffle(height_list)
        rectangles = [
            Rectangle(
                RECTANGLES_COLOR,
                RECT_WIDTH * i, 
                SCREEN_HEIGHT - v*RECT_HEIGHT,
                RECT_WIDTH,
                v*RECT_HEIGHT
            )
            for i, v in enumerate(height_list)
        ]
        start_sorting(algorythm, rectangles, screen)
    
    pygame.quit()
        
            
if __name__ == "__main__":
    main(*(
        merge_sort,
        selection_sort,
        gnome_sort,
        shell_sort,
        insertion_sort,
        comb_sort,
        shaker_sort,
        bubble_sort
    )*10)
