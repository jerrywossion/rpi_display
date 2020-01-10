import RPi.GPIO as GPIO
import drivers.ssd1351 as OLED

import time
from PIL import ImageFont

from ui.app import App
from ui.tab import Tab
from ui.uibase import UIBase
from ui.label import Label


try:
    if __name__ == '__main__':
        tab = Tab((128, 128), (0, 0))
        font = ImageFont.truetype("../static/fonts/NotoSansCJKsc-Regular.otf", 24)
        tab.append(Label(None, (0, 0), "Hello world, This is a very very long text", font, True))
        tab.set_index(0)

        app = App(tab)

        OLED.Device_Init()
        def display(img):
            OLED.Display_Image(img)
        app.run(display)
finally:
    OLED.Clear_Screen()
    GPIO.cleanup()
