import pygame

class Mouse:
    def __init__(self, pos):
      self.pos = pos
      self.selection = []
      self.clickpos = None
    def update(self):
        pos = pygame.mouse.get_pos()
        self.pos = [pos[0]//SIZE_GRID, pos[1]//SIZE_GRID]
        if pygame.mouse.get_pressed()[0] and self.clickpos == None:
            self.clickpos = self.pos 
            self.selection = []
        if pygame.mouse.get_pressed()[0] and self.clickpos != None:
            self.selection = []
            for y in range(self.clickpos[0], self.pos[0] + 1):
                for x in range(self.clickpos[1], self.pos[1] + 1):
                    self.selection.append((y, x))
                    
        else:
            self.clickpos = None
            

SIZE_GRID = 32
FPS = 60
SCREEN_SIZE = [801, 801]
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.NOFRAME  )
mouse = Mouse([0, 0])