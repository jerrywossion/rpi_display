import time


class App:
    def __init__(self, content):
        self.content = content

    def run(self):
        while True:
            self.content.render()
            self.content.image.show()
            time.sleep(100)

    def run_once(self):
        self.content.render()
        self.content.image.show()
