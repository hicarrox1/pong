from sprite import *
from test_rebond import *

class Balle(MoveSprite):


    def __init__(self, pos_x: int, pos_y: int) -> None:
        super().__init__(pos_x, pos_y, (16,16), (0,32), 0, 300, 10, 0)

        self.norme_limit = 4
    
    def rebond_y(self):

        self.direction[1] = -self.direction[1]

    def rebond_x(self):

        add = 0.2

        if self.direction[0] >= 0:
            
            add = -0.2

        self.direction[0] = -self.direction[0] + add
    
    def update(self):

        if get_norme(self.direction) > self.norme_limit:

            self.direction[0] - 0.2
            self.direction[1] - 0.2

        super().update()