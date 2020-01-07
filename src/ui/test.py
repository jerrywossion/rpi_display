import time
from PIL import ImageFont

from app import App
from tab import Tab
from uibase import UIBase
from label import Label


if __name__ == '__main__':
    tab = Tab((128, 128), (0, 0))
    font = ImageFont.truetype("?.ttf", 24)
    tab.append(Label((0, 0), "Hello world, This is a very very long text", font, True))
    tab.set_index(0)

    app = App(tab)
    app.run()


