import time


class App:
    def __init__(self, content):
        self.content = content

    def run(self, display):
        while True:
            display(self.content.render())
            time.sleep(0.05)

    def run_once(self, display):
        display(self.content.render())
