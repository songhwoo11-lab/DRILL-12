from pico2d import load_image


class Grass:
    image = None
    def __init__(self, x, y):
        if Grass.image == None:
            Grass.image = load_image('grass.png')

        self.x = x
        self.y = y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
