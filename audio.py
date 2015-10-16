import pygame


class Audio:
    def loadSound(self, filename, volume=1):
        sound = pygame.mixer.Sound(filename)
        if volume != 1:
            sound.set_volume(volume)
        return sound

    def playSound(self, sound, repeat=False):
        if repeat:
            sound.play(-1)
        else:
            sound.play()

    def stopSound(self, sound):
        sound.stop()

    def loadMusic(self, filename, volume=1):
        pygame.mixer.music.load(filename)
        if volume != 1:
            pygame.mixer.music.set_volume(volume)

    def playMusic(self, repeat=False):
        if repeat:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()

    def stopMusic(self):
        pygame.mixer.music.stop()
