import pygame, keys


def getMousePosition():
    return pygame.mouse.get_pos()


def getMouseButton(button):
    return pygame.mouse.get_pressed()[button - 1]


def hideMouse():
    pygame.mouse.set_visible(False)


def showMouse():
    pygame.mouse.set_visible(True)


def moveMouse(x, y):
    pygame.mouse.set_pos((int(x), int(y)))


class Keys:
    def __init__(self):
        self.keysPressedNow = {}

    def isKeyPressed(self, key):
        return self.keysPressedNow.get(keys.getKeyCode(key), False)

    def pressKey(self, key):
        self.keysPressedNow[key] = True

    def releaseKey(self, key):
        self.keysPressedNow[key] = False
