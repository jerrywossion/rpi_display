from PIL import Image


class UIBase:
    def __init__(self, size, pos):
        print(size)
        self.width = size[0]
        self.height = size[1]
        self.image = Image.new("RGB", size, "BLACK")
        self.box = (pos[0], pos[1], pos[0] + self.width, pos[1] + self.height)
        self.components = []

    def append(self, component):
        self.components.append(component)

    def render(self):
        for component in self.components:
            component.render()
            self.image.paste(component.image, component.box)
