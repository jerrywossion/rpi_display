from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from uibase import UIBase


class Label(UIBase):
    def __init__(self, size, pos, text, font, scroll=False):
        if size is None:
            size = font.getsize(text)
        super(Label, self).__init__(size, pos)
        self.offset = 0
        self.text = text
        self.font = font
        self.scroll = scroll

    def render(self):
        # clear
        self.image = Image.new("RGB", (self.width, self.height), "BLACK")
        draw = ImageDraw.Draw(self.image)
        if self.scroll:
            xy = (-self.offset, 0)
        else:
            xy = (0, 0)
        draw.text(xy, self.text, fill="WHITE", font=self.font)
        self.offset += 5
        if self.offset > self.width:
            self.offset = 0
