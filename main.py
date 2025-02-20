import pygame
import time
from objects import Scene
from settings import mouse, FPS
from displays import display_s

def mainloop():
    pygame.init()
    running = True
    scene = Scene()
    clock = pygame.time.Clock()
    current_time = time.perf_counter()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                running = False
        display_s(scene)
        mouse.update()
        
        clock.tick(FPS)

    

mainloop()