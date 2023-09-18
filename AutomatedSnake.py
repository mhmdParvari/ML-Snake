import arcade
from src.fruit import Fruit
from src.snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=795, antialiasing=False)
        self.apple=Fruit()
        self.snake=Snake()
        self.x_priority = True
    
    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.snake.draw()

    def make_snake_move(self):

        if self.snake.center_x < self.apple.center_x and self.x_priority:
            if self.snake.change_x < 0:
                self.snake.change_x = 0
                if self.snake.center_y < self.apple.center_y:
                    self.snake.change_y += self.snake.speed 
                else:
                    self.snake.change_y += -self.snake.speed 
                for i in range(3):
                    self.snake.update_position()
                    self.on_draw()
            self.snake.change_x = self.snake.speed
            self.snake.change_y = 0

        elif self.snake.center_x > self.apple.center_x and self.x_priority:
            if self.snake.change_x > 0:
                self.snake.change_x = 0
                if self.snake.center_y < self.apple.center_y:
                    self.snake.change_y += self.snake.speed 
                else:
                    self.snake.change_y += -self.snake.speed 
                for i in range(3):
                    self.snake.update_position()
                    self.on_draw()
            self.snake.change_x = -self.snake.speed
            self.snake.change_y = 0


        elif self.snake.center_x == self.apple.center_x:
            if self.snake.center_y < self.apple.center_y:
                if self.snake.change_y < 0:
                    self.x_priority = False
                    self.snake.change_y = 0
                    if self.snake.center_x < self.width / 2:
                        self.snake.change_x += self.snake.speed
                    else:
                        self.snake.change_x += -self.snake.speed
                    for i in range(3):
                        self.snake.update_position()
                        self.on_draw()
                self.snake.change_y = self.snake.speed
                self.snake.change_x = 0

            else:
                if self.snake.change_y > 0:
                    self.x_priority = False
                    self.snake.change_y = 0
                    if self.snake.center_x < self.width / 2:
                        self.snake.change_x += self.snake.speed
                    else:
                        self.snake.change_x += -self.snake.speed
                    for i in range(3):
                        self.snake.update_position()
                        self.on_draw()
                self.snake.change_y = -self.snake.speed
                self.snake.change_x = 0

    def on_update(self, delta_time: float):
        self.snake.update_position()
        self.make_snake_move()
         
        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.body.append([self.snake.center_x, self.snake.center_y])
            self.apple = Fruit()
            self.x_priority = True
        
    # def on_key_press(self, key, modifiers: int):
    #     self.snake.change_x=0
    #     self.snake.change_y=0
    #     if key==arcade.key.RIGHT:
    #         self.snake.change_x= self.snake.speed
    #     if key==arcade.key.LEFT:
    #         self.snake.change_x= -self.snake.speed
    #     if key==arcade.key.UP:
    #         self.snake.change_y= self.snake.speed
    #     if key==arcade.key.DOWN:
    #         self.snake.change_y= -self.snake.speed


myGame=Game()
arcade.run()