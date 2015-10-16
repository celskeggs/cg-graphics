import sdl2, events


# TODO: pass SDL_INIT_TIMER to SDL_Init

def onTimer(listenerFunction, interval):
    eventType = sdl2.SDL_RegisterEvents(1)
    assert eventType != 0xFFFFFFFF, "Out of timers!"

    def timer_handler(event, world):
        listenerFunction(world)

    def raw_callback(interval, param):
        event = sdl2.SDL_Event()
        event.type = eventType
        event.user = sdl2.SDL_UserEvent()
        assert sdl2.SDL_PushEvent(event) > 0, "Could not push event: %s" % sdl2.SDL_GetError()
        return interval

    events.handler(eventType, timer_handler)
    assert sdl2.SDL_AddTimer(interval, raw_callback, None) != 0, "Could not create timer: %s" % sdl2.SDL_GetError()


class GameClock:
    def __init__(self):
        self.startGameAt = None
        self.lastDisplayedAt = 0
        self.displayInterval = 0
        self.clock = None
        self.targetFPS = 60

    def maybePrintFPS(self):
        if self.displayInterval > 0:
            time = pygame.time.get_ticks()
            if time > self.lastDisplayedAt + self.displayInterval:
                print self.getActualFPS()
                self.lastDisplayedAt = time

    def displayFPS(self, interval):
        self.displayInterval = interval * 1000
        self.lastDisplayedAt = pygame.time.get_ticks()

    def getActualFPS(self):
        return self.clock.get_fps()

    def start(self):
        self.clock = pygame.time.Clock()
        self.startGameAt = pygame.time.get_ticks()

    def tick(self):
        self.maybePrintFPS()
        self.clock.tick(self.targetFPS)

    def setTargetFPS(self, frameRate):
        self.targetFPS = frameRate

    def getElapsedTime(self):
        return pygame.time.get_ticks() - self.startGameAt

    def resetTime(self):
        self.startGameAt = pygame.time.get_ticks()
