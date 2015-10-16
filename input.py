import pygame, keys, events


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

@events.handler(pygame.KEYDOWN)
def key_down(event, _GLI):
    _GLI.keys.pressKey(event.key)
    if ("keydown", event.key) in _GLI.eventListeners:
        _GLI.eventListeners[("keydown", event.key)](_GLI.world)
    else:
        _GLI.eventListeners["keydown"](_GLI.world, event.key)


@events.handler(pygame.KEYUP)
def key_down(event, _GLI):
    _GLI.keys.releaseKey(event.key)
    if ("keyup", event.key) in _GLI.eventListeners:
        _GLI.eventListeners[("keyup", event.key)](_GLI.world)
    else:
        _GLI.eventListeners["keyup"](_GLI.world, event.key)


@events.handler(pygame.MOUSEBUTTONDOWN)
def mouse_button_down(event, _GLI):
    if event.button <= 3:
        _GLI.eventListeners["mousedown"](_GLI.world, event.pos[0], event.pos[1], event.button)
    elif event.button == 4:
        _GLI.eventListeners["wheelforward"](_GLI.world, event.pos[0], event.pos[1])
    elif event.button == 5:
        _GLI.eventListeners["wheelbackward"](_GLI.world, event.pos[0], event.pos[1])


@events.handler(pygame.MOUSEBUTTONUP)
def mouse_button_up(event, _GLI):
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button <= 3:
            _GLI.eventListeners["mouseup"](_GLI.world, event.pos[0], event.pos[1], event.button)


@events.handler(pygame.MOUSEMOTION)
def mouse_motion(event, _GLI):
    dx, dy = event.rel
    if dx != 0 or dy != 0:
        button1 = (event.buttons[0] == 1)
        button2 = (event.buttons[1] == 1)
        button3 = (event.buttons[2] == 1)
        _GLI.eventListeners["mousemotion"](_GLI.world, event.pos[0], event.pos[1], dx, dy, button1, button2, button3)
