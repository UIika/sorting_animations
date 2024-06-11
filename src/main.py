import pygame
import random
from colors import *
from config import (
    LIST_LENGTH, RECT_WIDTH, RECT_HEIGHT,
    SCREEN_HEIGHT, SCREEN_WIDTH,
    RECT_COLOR, FINISHED_RECTANGLES_COLOR
)
from rectangle import update_rectangles
from sorts import *
from time import time


rectangles = list(range(LIST_LENGTH, 0, -1))

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
            last_modified = next(sorting_generator)
        except StopIteration:
            update_rectangles(rectangles, screen)
            finished = True
            for i, v in enumerate(rectangles):
                pygame.draw.rect(screen, GREEN, pygame.Rect(
                    i*RECT_WIDTH, SCREEN_HEIGHT-v*RECT_HEIGHT,
                    RECT_WIDTH, int(v*RECT_HEIGHT)+(v*RECT_HEIGHT > 0)
                ))
                pygame.time.wait(500//LIST_LENGTH)
                pygame.display.update()
            break
        update_rectangles(rectangles, screen, last_modified)
    print(pygame.display.get_caption()[0])

def main(*sorting_algotythms):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    for algorythm in sorting_algotythms:
        random.shuffle(rectangles)
        start_sorting(algorythm, rectangles, screen)
    
    pygame.quit()
        
            
if __name__ == "__main__":
    main(*(
        merge_sort,
        selection_sort,
        #gnome_sort,
        shell_sort,
        insertion_sort,
        comb_sort,
        shaker_sort,
        bubble_sort,
    )*10)
