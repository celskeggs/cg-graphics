import pygame


def loadSound(filename, volume=1):
    sound = pygame.mixer.Sound(filename)
    if volume != 1:
        sound.set_volume(volume)
    return sound


def playSound(sound, repeat=False):
    if repeat:
        sound.play(-1)
    else:
        sound.play()


def stopSound(sound):
    sound.stop()


def loadMusic(filename, volume=1):
    pygame.mixer.music.load(filename)
    if volume != 1:
        pygame.mixer.music.set_volume(volume)


def playMusic(repeat=False):
    if repeat:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()


def stopMusic():
    pygame.mixer.music.stop()
