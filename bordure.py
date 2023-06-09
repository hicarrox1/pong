from sprite import *

class Camp(Rect_Sprite):

    def __init__(self, pos_x: int, pos_y: int, size: tuple, col: int, equipe: str) -> None:
        super().__init__(pos_x, pos_y, size, col)

        self.equipe = equipe
