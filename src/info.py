# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import drivers.ssd1351 as OLED

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from aggdraw import Draw
from aggdraw import Pen
from aggdraw import Brush
# from aggdraw import Font

import sys
import psutil
from os import path
from subprocess import PIPE
from subprocess import Popen


# global configs
TOTAL_MEMORY = 4  # GB
TOTAL_DISK = 64  # GB
FONTS_HOME="/home/pi/workspace/rpi_display/static/fonts"


def get_temp():
    try:
        f = open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(f.read()) / 1000
        color = "GREEN"
        if temp >= 40 and temp < 50:
            color = "ORANGE"
        elif temp >= 50:
            color = "RED"
        return (round(temp, 1), color)
    except:
        return (-1, "RED")


def get_lan_ip():
    cmd = "ip addr | grep inet | grep -v inet6 | grep -v '127' | awk '{print $2}' | cut -d '/' -f 1"
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    res = output[:-1]
    return res.decode()


def get_resource_usage():
    cpu_usage = round(psutil.cpu_percent(), 2)  # %
    mem_usage = round(psutil.virtual_memory().used / 1024 / 1024 / 1024, 1)  # GB
    disk_usage = round(psutil.disk_usage('/').used / 1024 / 1024 / 1024, 2)  # GB
    return (cpu_usage, mem_usage, disk_usage)


def make_font(font, size):
    return ImageFont.truetype(font, size)


def draw_ui():
    # infos
    temp = get_temp()[0]
    cpu_usage, mem_usage, disk_usage = get_resource_usage()
    ip = get_lan_ip()

    draw = Draw("RGB", (128, 128), "BLACK")

    # pens
    pred = Pen("#fa114f", 8)
    predo = Pen("#fa114f", 8, 32)
    pgreen = Pen("#04de71", 8)
    pgreeno = Pen("#04de71", 8, 32)
    pblue = Pen("#2094fa", 8)
    pblueo = Pen("#2094fa", 8, 32)

    # fonts
    notosans_light = path.join(FONTS_HOME, "NotoSansCJKsc-Light.otf")
    notosans_regular = path.join(FONTS_HOME, "NotoSansCJKsc-Regular.otf")
    notosans_bold = path.join(FONTS_HOME, "NotoSansCJKsc-Bold.otf")

    # draw cpu ring
    draw.arc((4, 6, 79, 81), 0, 360, predo)
    draw.arc((4, 6, 79, 81), 90, 360 * cpu_usage / 100 + 90, pred)
    # draw memory ring
    draw.arc((14, 16, 69, 71), 0, 360, pgreeno)
    draw.arc((14, 16, 69, 71), 90, 360 * (mem_usage / TOTAL_MEMORY) + 90, pgreen)
    # draw disk ring
    draw.arc((24, 26, 59, 61), 0, 360, pblueo)
    draw.arc((24, 26, 59, 61), 90, 360 * (disk_usage / TOTAL_DISK) + 90, pblue)

    # draw bottom bar
    pwhite = Pen("WHITE", 1)
    bwhite = Brush("WHITE")
    pgrey = Pen("#555555", 1)
    bgrey = Brush("#555555")
    draw.ellipse((40, 127 - 6, 46, 127), pwhite, bwhite)
    draw.ellipse((54, 127 - 6, 60, 127), pgrey, bgrey)
    draw.ellipse((68, 127 - 6, 74, 127), pgrey, bgrey)
    draw.ellipse((82, 127 - 6, 88, 127), pgrey, bgrey)

    im = Image.frombytes("RGB", (128, 128), draw.tobytes())

    pildraw = ImageDraw.Draw(im)
    pildraw.text((88, 1), "CPU(%)", font=make_font(notosans_regular, 10), fill="WHITE")
    pildraw.text((88, 11), str(cpu_usage), font=make_font(notosans_bold, 18), fill="WHITE")
    pildraw.text((88, 32), "Mem(G)", font=make_font(notosans_regular, 10), fill="WHITE")
    pildraw.text((88, 42), str(mem_usage), font=make_font(notosans_bold, 18), fill="WHITE")
    pildraw.text((88, 63), "Disk(G)", font=make_font(notosans_regular, 10), fill="WHITE")
    pildraw.text((88, 73), str(disk_usage), font=make_font(notosans_bold, 18), fill="WHITE")

    sz = pildraw.textsize("100%", font=make_font(notosans_light, 8))
    pildraw.text((4 + (79 - 4) / 2 - sz[0] / 2, 81 - 8), "100%", font=make_font(notosans_light, 8), fill="WHITE")
    sz = pildraw.textsize(str(TOTAL_MEMORY) + "GB", font=make_font(notosans_light, 8))
    pildraw.text((14 + (69 - 14) / 2 - sz[0] / 2, 71 - 8), str(TOTAL_MEMORY) + "GB", font=make_font(notosans_light, 8), fill="WHITE")
    sz = pildraw.textsize(str(TOTAL_DISK) + "GB", font=make_font(notosans_light, 8))
    pildraw.text((24 + (59 - 24) / 2 - sz[0] / 2, 61 - 8), str(TOTAL_DISK) + "GB", font=make_font(notosans_light, 8), fill="WHITE")

    pildraw.text((2, 84), "IP Address", font=make_font(notosans_regular, 10), fill="WHITE")
    pildraw.text((4, 94), ip, font=make_font(notosans_regular, 16), fill="WHITE")

    return im


def main():
    OLED.Device_Init()
    while True:
        OLED.Display_Image(draw_ui())
        OLED.Delay(1000)


# if __name__ == '__main__':
#     main()

try:
    if __name__ == '__main__':
        main()
finally:
    OLED.Clear_Screen()
    GPIO.cleanup()
