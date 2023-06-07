from sprite import *

class Bordure(Rect_Sprite):

    def __init__(self, pos_x: int, pos_y: int, size: tuple, col: int, vecteur_reactif: list) -> None:
        super().__init__(pos_x, pos_y, size, col)

        self.vecteur_reactif = vecteur_reactif

class Camp():

    def __init__(self, pos_x: int, pos_y: int, size: tuple, col: int, equipe: list) -> None:
        super().__init__(pos_x, pos_y, size, col)

