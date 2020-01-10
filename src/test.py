from PIL import ImageFont

from ui.app import App
from ui.tab import Tab
from ui.label import Label


if __name__ == '__main__':
    tab = Tab(width=128, height=128, position=(0, 0))

    app = App(tab)
    app.run_once(lambda im: im.show())

    font = ImageFont.truetype("?.otf", 24)

    tab.add_child(Label(width=128, text="1", font=font))
    app.run_once(lambda im: im.show())

    tab.add_child(Label(text="2", font=font, alignment="right", width=128))
    app.run_once(lambda im: im.show())

    tab.add_child(Label(text="3", font=font, alignment="center", width=128))
    app.run_once(lambda im: im.show())

    tab.add_child(Label(text="4", font=font, width=128))
    app.run_once(lambda im: im.show())

    tab.set_index(0)
    app.run_once(lambda im: im.show())
    tab.set_index(1)
    app.run_once(lambda im: im.show())
    tab.set_index(2)
    app.run_once(lambda im: im.show())
    tab.set_index(3)
    app.run_once(lambda im: im.show())



