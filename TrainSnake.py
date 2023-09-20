import time
import threading
import pandas as pd
import arcade
from src.fruit import Fruit
from src.snake import Snake

DATA_GENERATION_RATE = .3 # seconds

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=795, antialiasing=False)
        self.apple=Fruit()
        self.snake=Snake()
        self.x_priority = True
        self.train_data = []
        self.mythread = threading.Thread(target= self.gather_data, daemon=True)
        self.mythread.start()
    
    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.snake.draw()

    def get_sample(self):
        x_diff = self.snake.center_x - self.apple.center_x
        y_diff = self.snake.center_y - self.apple.center_y
        if self.snake.change_x > 0: label = 0
        if self.snake.change_y > 0: label = 1
        if self.snake.change_x < 0: label = 2
        if self.snake.change_y < 0: label = 3
        return [x_diff, y_diff, label]

    def gather_data(self):
        while(True):
            time.sleep(DATA_GENERATION_RATE)
            sample = self.get_sample()
            print(sample)
            self.train_data.append(sample)


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
        

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.ESCAPE:
            df = pd.DataFrame(self.train_data, columns=['x_diff', 'y_diff', 'direction'])
            df.to_csv('directions.csv', index=False)
            self.close()


myGame=Game()
arcade.run()
