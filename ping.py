from sprite import *

class Ping(Rect_Sprite):

    def __init__(self, pos_x: int, pos_y: int,key_up: int, key_down: int, vecteur_reactif: list) -> None:
        super().__init__(pos_x, pos_y, (12,80), 1)

        self.key_up = key_up
        self.key_down = key_down

        self.speed = 4

        self.vecteur_reactif = vecteur_reactif


    def update(self):

        if not self.pos_y < 0:

            if pyxel.btn(self.key_up):

                self.pos_y -= self.speed

        if not self.pos_y + self.size[1] > pyxel.height:

            if pyxel.btn(self.key_down):

                self.pos_y += self.speed