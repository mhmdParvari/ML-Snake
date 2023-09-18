import arcade

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x=400
        self.center_y=300
        self.height=15
        self.width=15
        self.speed=5
        self.change_x=0
        self.body=[]
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,arcade.color.GREEN)
        for part in self.body:
            arcade.draw_rectangle_filled(part[0],part[1],self.width,self.height,arcade.color.GREEN)
	
    def update_position(self):
        self.body.append([self.center_x,self.center_y])
        self.body.pop(0)
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.center_x < 0:
            self.center_x=0
        if self.center_x > 799:
            self.center_x=799
        if self.center_y < 0:
            self.center_y=0
        if self.center_y > 599:
            self.center_y=599
