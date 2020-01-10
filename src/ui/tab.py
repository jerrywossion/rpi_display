from PIL import Image
from aggdraw import Draw
from aggdraw import Pen
from aggdraw import Brush

from .uibase import UIBase


class Tab(UIBase):
    DOT_SIZE = 6
    DOT_SPACING = 8

    def __init__(self, *, width=0, height=0, position=(0, 0)):
        super(Tab, self).__init__(width=width, height=height, position=position)
        self.index = None

    def set_index(self, index):
        self.index = index

    def tab_count(self):
        return len(self.children)

    def update_bottom(self):
        self.clear()

        draw = Draw(self._image)
        pen_white = Pen("WHITE", 1)
        pen_grey = Pen("#555555", 1)
        brush_white = Brush("WHITE")
        brush_grey = Brush("#555555")

        dots_width = Tab.DOT_SIZE * self.tab_count() + Tab.DOT_SPACING * (self.tab_count() - 1)
        start_x = (self.width - dots_width) / 2
        start_y = self.height - Tab.DOT_SIZE - 1  # padding-bottom: 1px
        end_y = self.height - 1
        for i in range(self.tab_count()):
            pen = pen_grey
            brush = brush_grey
            if self.index == i:
                pen = pen_white
                brush = brush_white
            cur_x = start_x + i * (Tab.DOT_SIZE + Tab.DOT_SPACING)
            draw.ellipse((cur_x, start_y, cur_x + Tab.DOT_SIZE, end_y), pen, brush)
        self._image = Image.frombytes("RGB", (self.width, self.height), draw.tobytes())

    def render(self):
        self.update_bottom()
        if self.tab_count() > 0 and self.index in range(0, self.tab_count()):
            cur_child = self.children[self.index]
            self._image.paste(cur_child.render(), cur_child.box())
        return self._image
