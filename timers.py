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
