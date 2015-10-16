import pygame

event_handlers = {}


# so that we can use @decorators.
# remember that, since append returns None, all of the functions won't really be defined
def registered_handler(event_type):
    if event_type not in event_handlers:
        event_handlers[event_type] = []
    return event_handlers[event_type].append


@registered_handler(pygame.QUIT)
def quit(event, _GLI):
    _GLI.keepRunning = False


@registered_handler(pygame.KEYDOWN)
def key_down(event, _GLI):
    if event.key == pygame.K_ESCAPE:
        _GLI.keepRunning = False
    else:
        _GLI.keys.pressKey(event.key)
        if ("keydown", event.key) in _GLI.eventListeners:
            _GLI.eventListeners[("keydown", event.key)](_GLI.world)
        else:
            _GLI.eventListeners["keydown"](_GLI.world, event.key)


@registered_handler(pygame.KEYUP)
def key_down(event, _GLI):
    _GLI.keys.releaseKey(event.key)
    if ("keyup", event.key) in _GLI.eventListeners:
        _GLI.eventListeners[("keyup", event.key)](_GLI.world)
    else:
        _GLI.eventListeners["keyup"](_GLI.world, event.key)


@registered_handler(pygame.MOUSEBUTTONDOWN)
def mouse_button_down(event, _GLI):
    if event.button <= 3:
        _GLI.eventListeners["mousedown"](_GLI.world, event.pos[0], event.pos[1], event.button)
    elif event.button == 4:
        _GLI.eventListeners["wheelforward"](_GLI.world, event.pos[0], event.pos[1])
    elif event.button == 5:
        _GLI.eventListeners["wheelbackward"](_GLI.world, event.pos[0], event.pos[1])


@registered_handler(pygame.MOUSEBUTTONUP)
def mouse_button_up(event, _GLI):
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button <= 3:
            _GLI.eventListeners["mouseup"](_GLI.world, event.pos[0], event.pos[1], event.button)


@registered_handler(pygame.MOUSEMOTION)
def mouse_motion(event, _GLI):
    dx, dy = event.rel
    if dx != 0 or dy != 0:
        button1 = (event.buttons[0] == 1)
        button2 = (event.buttons[1] == 1)
        button3 = (event.buttons[2] == 1)
        _GLI.eventListeners["mousemotion"](_GLI.world, event.pos[0], event.pos[1], dx, dy, button1, button2, button3)


@registered_handler(pygame.JOYAXISMOTION)
def joystick_axis(event, _GLI):
    joystickValue = _GLI.joyinfo.applyDeadzone(event.value)
    _GLI.eventListeners["stickmotion"](_GLI.world, event.joy, event.axis, joystickValue)


@registered_handler(pygame.JOYHATMOTION)
def joystick_hat(event, _GLI):
    _GLI.eventListeners["dpadmotion"](_GLI.world, event.joy, event.hat, event.value[0], event.value[1])


@registered_handler(pygame.JOYBUTTONUP)
def joystick_button_up(event, _GLI):
    _GLI.eventListeners["joybuttonup"](_GLI.world, event.joy, event.button + 1)


@registered_handler(pygame.JOYBUTTONDOWN)
def joystick_button_down(event, _GLI):
    _GLI.eventListeners["joybuttondown"](_GLI.world, event.joy, event.button + 1)


def pump(_GLI):
    eventlist = pygame.event.get()
    for event in eventlist:
        for handler in event_handlers.get(event.type, ()):
            handler(event, _GLI)
            if not _GLI.keepRunning:
                break
        if event.type >= pygame.USEREVENT:
            _GLI.eventListeners["timer" + str(event.type)](_GLI.world)
        if not _GLI.keepRunning:
            break
