import sdl2, events


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


def onMousePress(listenerFunction):
    def mouse_press_handler(event, world):
        if event.button <= 3:
            listenerFunction(world, event.pos[0], event.pos[1], event.button)

    events.handler(pygame.MOUSEBUTTONDOWN, mouse_press_handler)


def onMouseRelease(listenerFunction):
    def mouse_release_handler(event, world):
        if event.button <= 3:
            listenerFunction(world, event.pos[0], event.pos[1], event.button)

    events.handler(pygame.MOUSEBUTTONUP, mouse_release_handler)


def onWheelForward(listenerFunction):
    def wheel_forward_handler(event, world):
        if event.button == 4:
            listenerFunction(world, event.pos[0], event.pos[1])

    events.handler(pygame.MOUSEBUTTONDOWN, wheel_forward_handler)


def onWheelBackward(listenerFunction):
    def wheel_backward_handler(event, world):
        if event.button == 5:
            listenerFunction(world, event.pos[0], event.pos[1])

    events.handler(pygame.MOUSEBUTTONDOWN, wheel_backward_handler)


def onMouseMotion(listenerFunction):
    def mouse_motion_handler(event, world):
        dx, dy = event.rel
        if dx != 0 or dy != 0:
            listenerFunction(world, event.pos[0], event.pos[1], dx, dy, event.buttons[0] == 1,
                             event.buttons[1] == 1, event.buttons[2] == 1)

    events.handler(pygame.MOUSEMOTION, mouse_motion_handler)
