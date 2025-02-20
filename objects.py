from utulities import Vector2
from settings import SCREEN_SIZE, SIZE_GRID

class Player:
    def __init__(self, position=Vector2(),typee="zombie", minions = []):
        self.typee = typee
        self.minions = minions
        self.position = position
        self.velo = Vector2()
        self.sprite = Sprite()
    def move(self):
        self.pos += self.velo
        
        
class Minion:
    def __init__(self, position=Vector2(),typee="zombie", minions = []):
        self.typee = typee
        self.minions = minions
        self.position = position
        self.velo = Vector2()
    
    def move(self):
        self.pos += self.velo
        
class Scene:
    def __init__(self):
        self.props = []
        self.map = [[[None] for i in range(int(SCREEN_SIZE[0]/SIZE_GRID))]for i in range(int(SCREEN_SIZE[1]/SIZE_GRID))]
    
    def update_sc(self):
        for prop in self.props:
            x, y = self.prop.get()
            if (x, y) != prop.oldpos.get():
                ox , oy = prop.oldpos.get() 
                 if x < SCREEN_SIZE[0] / SIZE_GRID and x > 0 and y < SCREEN_SIZR[1] and y > 0:
                    self.map[y//SIZE_GRID][x//SIZE_GRID] = prop
                self.map[oy//SIZE_FRID][xo//SIZE_GRID] = None
                

    def show(self):
        pass

        
