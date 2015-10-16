import sdl2

event_handlers = {}


class EventLoop:
    def __init__(self):
        self.keepRunning = False

    def start(self):
        self.keepRunning = True

    def stop(self):
        self.keepRunning = False

    def pump(self, world):
        eventlist = pygame.event.get()
        for event in eventlist:
            for event_handler in event_handlers.get(event.type, ()):
                event_handler(event, world)
                if not self.keepRunning:
                    break
            if not self.keepRunning:
                break

    def runloop(self, world, loopFunction):
        try:
            while self.keepRunning:
                self.pump(world)
                loopFunction()
        finally:
            pygame.quit()  # TODO: do this differently?


# so that we can use @decorators.
# remember that, since append returns None, all of the functions won't really be defined
def handler(event_type, new_handler=None):
    if event_type not in event_handlers:
        event_handlers[event_type] = []
    if new_handler is None:
        return event_handlers[event_type].append
    else:
        event_handlers[event_type].append(new_handler)
