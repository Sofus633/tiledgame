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
        self.map = [[[] for i in range(int(SCREEN_SIZE[0]/SIZE_GRID))]for i in range(int(SCREEN_SIZE[1]/SIZE_GRID))]
        
    def show(self):
        pass

        