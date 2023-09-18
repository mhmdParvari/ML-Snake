import random
import arcade

class Fruit(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x=random.randint(0,799) // 5 * 5
        self.center_y=random.randint(0,599) // 5 * 5
        self.width=20
        self.height=20

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,5,arcade.color.YELLOW)
