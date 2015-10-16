import pygame, events


class Timers:
    def __init__(self):
        self.nextEventType = pygame.USEREVENT

    def onTimer(self, listenerFunction, interval):
        if self.nextEventType > pygame.NUMEVENTS:
            raise ValueError, "too many timer listeners"

        def timer_handler(event, world):
            listenerFunction(world)

        pygame.time.set_timer(self.nextEventType, interval)
        events.handler(self.nextEventType, timer_handler)
        self.nextEventType += 1
