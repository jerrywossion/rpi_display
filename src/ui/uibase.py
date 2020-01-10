from PIL import Image
from PIL import ImageDraw


class UIBase:
    def __init__(self, *, width=0, height=0, position=(0, 0)):
        self.width = width
        self.height = height
        self.position = position

        self._image = Image.new("RGB", (width, height), "BLACK")
        self._draw = ImageDraw.Draw(self._image)
        self.children = []

    def clear(self):
        # self._draw.rectangle([0, 0, *self.size()], fill=fill_color)
        self._image = Image.new("RGB", (self.width, self.height), "BLACK")
        self._draw = ImageDraw.Draw(self._image)

    def size(self):
        return self.width, self.height

    def box(self):
        return self.position[0], self.position[1], self.position[0] + self.width, self.position[1] + self.height

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        for child in self.children:
            self._image.paste(child.render(), child.box())
        return self._image
