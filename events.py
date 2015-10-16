import pygame

event_handlers = {}


# so that we can use @decorators.
# remember that, since append returns None, all of the functions won't really be defined
def handler(event_type, handler=None):
    if event_type not in event_handlers:
        event_handlers[event_type] = []
    if handler is None:
        return event_handlers[event_type].append
    else:
        event_handlers[event_type].append(handler)


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
