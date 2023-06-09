import pyxel
from sprite import *

class Gui():

    def __init__(self) -> None:
        
        self.anchor_x = 0
        self.anchor_y = 0

        self.spriteUI_list = []
        self.update_list = []

        self.start = False

        def start_game(e):

            self.start = True

            e.visibility = False

        self.button_start = ButtonRect(175,135,(50,30),start_game,3)

        self.spriteUI_list.extend([self.button_start])
        self.update_list.extend([self.button_start])

        self.score = [0,0]

    def draw(self):

        for sprite in self.spriteUI_list:

            sprite.draw(self.anchor_x,self.anchor_y)

        pyxel.text(20,20,f"score : {self.score[0]} | {self.score[1]}", 0)

        if self.button_start.visibility:

            pyxel.text(200-10,150-5,"Start", 0)

    def set_anchor(self, x: int, y: int):
        self.anchor_x = x
        self.anchor_y = y

    def update(self):
        
        for sprite in self.update_list:

            sprite.update()

class SpriteUi(Sprite):


    def __init__(self, pos_x: int, pos_y: int, size: tuple, pos_image: tuple, transparent_color: int, image_number: int = 0) -> None:
        super().__init__(pos_x, pos_y, size, pos_image, transparent_color, image_number)

    def draw(self,anchor_x: int, anchor_y: int):

        if self.visibility:
            pyxel.blt(self.pos_x+anchor_x ,self.pos_y +anchor_y ,self.image_number,self.pos_image[0],self.pos_image[1],self.size[0],self.size[1],self.transparent_color)


class Button(SpriteUi):

    def __init__(self, pos_x: int, pos_y: int, size: tuple, pos_image: tuple, transparent_color: int, on_click, image_number: int = 0) -> None:
        super().__init__(pos_x, pos_y, size, pos_image, transparent_color, image_number)

        self.on_click = on_click
        self.can_click = True

    def use(self):

        if self.can_click:
            self.on_click(self)

    def update(self):

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.test_collision_point((pyxel.mouse_x, pyxel.mouse_y)):
                self.use()
                self.can_click = False
        else:
            self.can_click = True

class ButtonRect(Button):

    def __init__(self, pos_x: int, pos_y: int, size: tuple, on_click, color: int) -> None:
        super().__init__(pos_x, pos_y, size,(0,0),0, on_click, 0)

        self.color = color

    def draw(self, anchor_x: int, anchor_y: int):
        if self.visibility:
            pyxel.rect(self.pos_x+anchor_x, self.pos_y+anchor_y, self.size[0],self.size[1], self.color)
