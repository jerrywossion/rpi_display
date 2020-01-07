import time


class App:
    def __init__(self, content):
        self.content = content

    def run(self, display):
        while True:
            self.content.render()
            display(self.content.image)
            time.sleep(0.05)

    def run_once(self):
        self.content.render()
        self.content.image.show()
