from sprite import *
from test_rebond import *

class Balle(MoveSprite):


    def __init__(self, pos_x: int, pos_y: int) -> None:
        super().__init__(pos_x, pos_y, (16,16), (0,32), 0, 200, 10, 0)

        self.norme_limit = 4

    def touche_border(self):
        if self.pos_x < 0 or self.pos_x + self.size[0] > pyxel.width - 6:
            return True
        if self.pos_y < 0 or self.pos_y + self.size[1] > pyxel.height - 6:
            return True
        
        return False
    
    def update(self):

        if get_norme(self.direction) > self.norme_limit:

            pass

        super().update()