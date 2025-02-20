from settings import screen
import pygame


class Sprite:
    def __init__(self, name, spritesheet, sheet_int):
        self.animations = {}
        self.name = name
        self.spritesheet = spritesheet
        self.sheet_inf = sheet_int #list [ [[animation 1(tuple start end int)], [animation 2 ], ect], [frame_width, frame_height], "anim name"]  ]
        self.animation_n = None
        self.rect = None
        self.index = 0
        self.getanim()
        
    def getanim(self):
        spritesheet = pygame.image.load(self.spritesheet)

        for val in self.sheet_inf:
            print(val)
            for i in range(val[0][0], val[0][1]):
                print(val)
                if val[2] not in self.animations:
                    self.animations[val[2]] = []
                print(i * val[1][0], 0, val[1][0] + (val[1][0]*i), val[1][1], i)
                frame = spritesheet.subsurface(pygame.Rect(i * val[1][0], 0, val[1][0] + (val[1][0]*i), val[1][1]))
                self.animations[val[2]].append(frame)
            self.animation_n = val[2]
        self.nextframe()
    
    def nextframe(self):
        self.rect =  self.animations[self.animation_n][self.index]
        self.index += 1

    def display(self, pos):
        screen.blit(self.animation[self.index])
    


    

if __name__ == "__main__": 

    running = True
    sprite =  Sprite("cat", "CAT_1.png", [ [[9, 14], [30, 30], "cat"]])
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800), pygame.NOFRAME  )
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                running = False
        screen.blit(sprite.animations["cat"][0], (400, 400))
        pygame.draw.circle(screen, (100, 100, 100), (500, 100), 5)
        pygame.display.flip()

