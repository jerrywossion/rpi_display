from PIL import Image
from aggdraw import Draw
from aggdraw import Pen
from aggdraw import Brush

from .uibase import UIBase


class Tab(UIBase):
    def __init__(self, size, pos):
        super(Tab, self).__init__(size, pos)
        self.index = None
        self.tabs = 0

    def update_dots(self):
        size = (self.width, self.height)
        draw = Draw("RGB", size, "BLACK")
        pwhite = Pen("WHITE", 1)
        bwhite = Brush("WHITE")
        pgrey = Pen("#555555", 1)
        bgrey = Brush("#555555")
        dot_size = 6
        dot_spacing = 8
        dots_width = dot_size * self.tabs + dot_spacing * (self.tabs - 1)
        print(dots_width)
        start_x = (self.width - dots_width) / 2
        start_y = self.height - dot_size
        end_y = self.height
        for i in range(self.tabs):
            pen = pgrey
            brush = bgrey
            if self.index == i:
                pen = pwhite
                brush = bwhite
            cur_x = start_x + i * (dot_size + dot_spacing)
            draw.ellipse((cur_x, start_y, cur_x + dot_size, end_y), pen, brush)
        self.image = Image.frombytes("RGB", (self.width, self.height), draw.tobytes())

    def append(self, component):
        self.components.append(component)
        self.tabs += 1

    def set_index(self, index):
        self.index = index

    def render(self):
        self.update_dots()
        if self.index in range(0, self.tabs):
            component = self.components[self.index]
            component.render()
            self.image.paste(component.image, component.box)
