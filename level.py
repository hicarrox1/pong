import pyxel
from random import randint
from sprite import *
from balle import Balle
from test_rebond import *
from ping import *
from bordure import *

class Level():


    def __init__(self) -> None:
        
        self.score = [0,0]

        self.liste_border = [Rect_Sprite(0,0,(pyxel.width,6),1),Rect_Sprite(0,pyxel.height-6,(pyxel.width,6),1),
                             Rect_Sprite(0,0,(6,pyxel.height),8,),Rect_Sprite(pyxel.width-6,0,(6,pyxel.height),11)]
        
        self.ping_liste = [Ping(30,150-40,pyxel.KEY_UP,pyxel.KEY_DOWN, [1,0]), Ping(400-30,150-40,pyxel.KEY_R,pyxel.KEY_F, [-1,0])]

        self.balle = None
         
        self.run = False

    def start(self):

        self.balle = Balle(200-8,150)

        end = 0
        begin = 0

        droite = randint(0,1)
        haut = randint(0,1)

        if droite == 1 and haut == 1:

            end = 11
            begin = 7

        if droite == 1 and haut == 0:

            end = 57
            begin = 53

        if droite == 0 and haut == 1:

            end = 25
            begin = 21

        if droite == 0 and haut == 0:

            end = 43
            begin = 39

        angle = randint(begin, end) * 10 ** -1

        self.balle.go_to_direction(get_vecteur_with_angle(angle,1))

        self.run = True

    def draw(self):

        pyxel.cls(6)

        if self.run:
        
            self.balle.draw()

        self.draw_ping()

        self.draw_bordure()

        
    def update(self):

        if self.run:

            self.balle.update()

            self.test_border()

            self.test_ping()

        for ping in self.ping_liste:

            ping.update()
    

    def test_border(self):

        if self.balle.pos_x <= 6:

            self.score[0] += 1

            self.start()

        if self.balle.pos_x >= pyxel.width-6-self.balle.size[0]:

            self.score[1] += 1

            self.start()

        if self.balle.pos_y <= 6 or self.balle.pos_y >= pyxel.height-6-self.balle.size[0]:

            self.balle.rebond_y()

    def test_ping(self):

        for ping in self.ping_liste:

                if self.balle.test_collision_sprite(ping):

                    self.balle.rebond_x()

    def draw_bordure(self):

        for border in self.liste_border:

            border.draw()

    def draw_ping(self):

        for ping in self.ping_liste:

            ping.draw()