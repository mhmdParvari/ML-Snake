import arcade
import numpy as np
import tensorflow as tf
from src.fruit import Fruit
from src.snake import Snake

model = tf.keras.models.load_model('model.h5')

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

    def get_direction(self):
        x_diff = self.snake.center_x - self.apple.center_x
        y_diff = self.snake.center_y - self.apple.center_y
        probablities = model.predict([[x_diff, y_diff]])
        return np.argmax(probablities)

    def move_snake_in_direction(self, dir):
        if dir == 0:
            self.snake.change_x = self.snake.speed
            self.snake.change_y = 0
        if dir == 1:
            self.snake.change_y = self.snake.speed
            self.snake.change_x = 0
        if dir == 2:
            self.snake.change_x = -self.snake.speed
            self.snake.change_y = 0
        if dir == 3:
            self.snake.change_y = -self.snake.speed
            self.snake.change_x = 0

    def on_update(self, delta_time: float):
        self.snake.update_position()
        self.move_snake_in_direction(self.get_direction())
        
        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.body.append([self.snake.center_x, self.snake.center_y])
            self.apple = Fruit()
        
        
myGame=Game()
arcade.run()