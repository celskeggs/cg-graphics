import pygame, keys, events


class Keys:
    def __init__(self):
        self.keysPressedNow = {}

    def initialize(self):
        events.handler(pygame.KEYDOWN, self.onPress)
        events.handler(pygame.KEYUP, self.onRelease)

    def isKeyPressed(self, key):
        return self.keysPressedNow.get(keys.getKeyCode(key), False)

    def onPress(self, event, _GLI):
        self.keysPressedNow[event.key] = True

    def onRelease(self, event, _GLI):
        self.keysPressedNow[event.key] = False


def onKeyPress(listenerFunction, key):
    key = keys.getKeyCode(key)
    if key is None:
        raise Exception("that is not a valid key")

    def key_press_handler(event, _GLI):
        if event.key == key:
            listenerFunction(_GLI.world)

    events.handler(pygame.KEYDOWN, key_press_handler)


def onAnyKeyPress(listenerFunction):
    def any_key_press_handler(event, _GLI):
        listenerFunction(_GLI.world, event.key)

    events.handler(pygame.KEYDOWN, any_key_press_handler)


def onKeyRelease(listenerFunction, key):
    key = keys.getKeyCode(key)
    if key is None:
        raise Exception("that is not a valid key")

    def key_release_handler(event, _GLI):
        if event.key == key:
            listenerFunction(_GLI.world)

    events.handler(pygame.KEYUP, key_release_handler)


def onAnyKeyRelease(listenerFunction):
    def any_key_release_handler(event, _GLI):
        listenerFunction(_GLI.world, event.key)

    events.handler(pygame.KEYUP, any_key_release_handler)
