import time

from app import App
from tab import Tab


if __name__ == '__main__':
    tab = Tab((128, 128), (0, 0))
    app = App(tab)

    tab.append(None)
    app.run_once()
    time.sleep(1)

    tab.append(None)
    app.run_once()
    time.sleep(1)

    tab.append(None)
    app.run_once()
    time.sleep(1)

    tab.append(None)
    app.run_once()
    time.sleep(1)

    tab.set_index(0)
    app.run_once()
    time.sleep(1)

    tab.set_index(1)
    app.run_once()
    time.sleep(1)

    tab.set_index(2)
    app.run_once()
    time.sleep(1)

    tab.set_index(3)
    app.run_once()
    time.sleep(1)

