import pyxel
from level import Level
from gui import Gui
from sprite import *

class Camera():


    def __init__(self) -> None:

        pyxel.camera()
        
        self.pos_x = 0
        self.pos_y = 0

        self.speed = 4
    
    def input(self):

        """if pyxel.btn(pyxel.KEY_RIGHT):
            self.pos_x += self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            self.pos_x -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            self.pos_y += self.speed
        if pyxel.btn(pyxel.KEY_UP):
            self.pos_y -= self.speed"""

    def update_camera(self):
        pyxel.camera(self.pos_x,self.pos_y)
    
    def update(self):

        self.input()
        self.update_camera()

        

class App():


    def __init__(self) -> None:
        pyxel.init(400,300)
        pyxel.load(r"images.pyxres")
        pyxel.mouse(True)

        self.sprite_liste = []

        self.camera = Camera()

        self.level = Level()

        self.gui = Gui()

        pyxel.run(self.update,self.draw)
    
    def update(self):

        self.update_all_sprite()

        self.camera.update()

        self.level.update()

        self.gui.set_anchor(self.camera.pos_x,self.camera.pos_y)

        self.gui.update()

        if self.gui.start:

            self.level.start()

            self.gui.start = False

        self.gui.score = self.level.score


    def draw(self):

        self.draw_all_sprite()

        self.level.draw()
        
        self.gui.draw()

        
    def draw_all_sprite(self):
        
        for sprite in self.sprite_liste:
            sprite.draw()

    def update_all_sprite(self):

        for sprite in self.sprite_liste:
            sprite.update()
    
App()