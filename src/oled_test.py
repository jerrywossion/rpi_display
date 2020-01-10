import RPi.GPIO as GPIO
import drivers.ssd1351 as OLED

from PIL import ImageFont

from ui.app import App
from ui.tab import Tab
from ui.label import Label


try:
    if __name__ == '__main__':
        tab = Tab(width=128, height=128, position=(0, 0))
        font = ImageFont.truetype("../static/fonts/NotoSansCJKsc-Regular.otf", 24)
        tab.add_child(Label(width=128, text="Hello world", alignment="center", font=font))
        tab.set_index(0)

        app = App(tab)

        OLED.Device_Init()

        def display(img):
            OLED.Display_Image(img)

        app.run(display)
finally:
    OLED.Clear_Screen()
    GPIO.cleanup()
