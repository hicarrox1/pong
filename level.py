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

        self.liste_border = [Rectb_Sprite(i, i, (pyxel.width-(2*i),pyxel.height-(2*i)), 1) for i in range(6)]

        self.liste_border = [Bordure(0,0,(pyxel.width,6),1,[0,+1]),Bordure(0,pyxel.height-6,(pyxel.width,6),1,[0,-1]),
                             Bordure(0,0,(6,pyxel.height),8,[+1,0]),Bordure(pyxel.width-6,0,(6,pyxel.height),11,[-1,0])]
        
        self.camp_list = []

        self.balle = Balle(200-8,150)
        
        self.ping_liste = [Ping(30,150-40,pyxel.KEY_UP,pyxel.KEY_DOWN, [1,0]), Ping(400-30,150-40,pyxel.KEY_R,pyxel.KEY_F, [-1,0])]

    def start(self):

        self.balle.go_to_direction(get_vecteur_with_angle((5*math.pi)/6,1))

    def draw(self):

        pyxel.cls(6)
        
        self.balle.draw()

        self.draw_ping()

        self.draw_bordure()

        
    def update(self):

        self.balle.update()

        for ping in self.ping_liste:

            ping.update()

        for border in self.liste_border:
            
            if self.balle.test_collision_sprite(border):

                self.rebond(border)
            
        for ping in self.ping_liste:

            if self.balle.test_collision_sprite(ping):

                self.rebond(ping)


    def rebond(self, reactif):

        reaction_support = reactif.vecteur_reactif

        reaction_norme = get_norme(self.balle.direction)

        self.balle.go_to_direction(addition_vecteur(self.balle.direction,reaction_support))


    def draw_bordure(self):

        for border in self.liste_border:

            border.draw()

    def draw_ping(self):

        for ping in self.ping_liste:

            ping.draw()
            

        