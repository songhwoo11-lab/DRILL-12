import game_world
import random
from pico2d import get_canvas_width, load_image


class Ball:
    image = []
    def __init__(self, x, y, direction):
        if len(Ball.image) == 0:
            Ball.image.append(load_image('ball21x21.png')) 
            Ball.image.append(load_image('ball41x41.png')) 
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 10
        self.imageIdx = random.randint(0, 1)

    def update(self):
        self.x += self.direction * self.speed
        if self.x < -21 or self.x > get_canvas_width() + 21:
            game_world.remove_object(self)

    def draw(self):
        self.image[self.imageIdx].draw(self.x, self.y)