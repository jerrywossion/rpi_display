from .uibase import UIBase


class Label(UIBase):
    def __init__(self, *, width, text, font, color="WHITE", alignment="left", scrolling=True, speed=5, position=(0, 0)):
        self.width = width
        self.text_size = font.getsize(text)
        self.height = self.text_size[1]
        self.text = text
        self.font = font
        self.color = color
        self.alignment = alignment
        self.scrolling = scrolling and self.text_size[0] > self.width
        self.speed = speed
        self.scrolling_offset = 0
        super(Label, self).__init__(width=self.width, height=self.height, position=position)

    def render(self):
        # clear
        self.clear()
        if self.scrolling:
            xy = (-self.scrolling_offset, 0)
        else:
            if self.alignment == "right":
                xy = (self.width - self.text_size[0], 0)
            elif self.alignment == "center":
                xy = ((self.width - self.text_size[0]) / 2, 0)
            else:  # self.alignment == "left" or invalid:
                xy = (0, 0)
        self._draw.text(xy, self.text, fill=self.color, font=self.font)
        self.scrolling_offset += self.speed
        if self.scrolling_offset > self.text_size[0]:
            self.scrolling_offset = -self.text_size[0]
        return self._image
