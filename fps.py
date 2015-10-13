import pygame


class GameClock:
    def __init__(self):
        self.startGameAt = None
        self.lastDisplayedAt = 0
        self.displayInterval = 0
        self.clock = None
        self.targetFPS = 60

    def maybePrintFPS(self):
        self.FPScount += 1
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
