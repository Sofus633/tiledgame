from settings import screen, SCREEN_SIZE, mouse, SIZE_GRID
import pygame
import time
def display_s(scene):
    scene.show()
    for y in range(0, int(SCREEN_SIZE[1]/16)+1):

        for x in range(0, int(SCREEN_SIZE[0]/16)+1):
            pygame.draw.line(screen, (0, 200, 0), (x*SIZE_GRID, 0), (x*SIZE_GRID, SCREEN_SIZE[1]))
            pygame.draw.line(screen, (0, 200, 0), (SCREEN_SIZE[0], y*SIZE_GRID), (0, y*SIZE_GRID))
            

    for (x, y) in mouse.selection:
         pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x*SIZE_GRID, y*SIZE_GRID, SIZE_GRID, SIZE_GRID), 0)
         

    pygame.draw.rect(screen, (0, 0, 200), pygame.Rect(mouse.pos[0]*SIZE_GRID, mouse.pos[1]*SIZE_GRID, SIZE_GRID, SIZE_GRID), 0)
    pygame.display.flip()
    screen.fill(0)