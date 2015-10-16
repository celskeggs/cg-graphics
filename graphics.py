"""
This is a simple interactive graphics and animation library for Python.
Author: Andrew Merrill
Version: 3.8 (last updated October, 2015)

This code is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike license
see http://creativecommons.org/licenses/by-nc-sa/3.0/ for details
"""

print "using graphics.py library version 3.8"

import pygame, os, math, colors, keys, joysticks, fps, display, audio


class World:
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameLibInfo:
    def __init__(self):
        self.world = None
        self.display = display.Display()
        self.audio = audio.Audio()
        self.joyinfo = joysticks.JoysticksInfo()
        self.fps = fps.GameClock()

        self.graphicsInited = False
        self.eventListeners = {}
        self.nextEventType = pygame.USEREVENT
        self.keysPressedNow = {}
        self.keepRunning = False

    def initGraphics(self):
        if not self.graphicsInited:
            self.display.initialize()
            self.initializeListeners()
            self.joyinfo.initialize()
            self.graphicsInited = True

    def initializeListeners(self):
        onAnyKeyPress(lambda world, key: 0)
        onAnyKeyRelease(lambda world, key: 0)
        onMousePress(lambda world, x, y, button: 0)
        onMouseRelease(lambda world, x, y, button: 0)
        onWheelForward(lambda world, x, y: 0)
        onWheelBackward(lambda world, x, y: 0)
        onMouseMotion(lambda world, x, y, dx, dy, b1, b2, b3: 0)
        onGameControllerStick(lambda world, device, axis, value: 0)
        onGameControllerDPad(lambda world, device, pad, xvalue, yvalue: 0)
        onGameControllerButtonPress(lambda world, device, button: 0)
        onGameControllerButtonRelease(lambda world, device, button: 0)

    def startGame(self):
        self.fps.start()
        self.keepRunning = True


_GLI = GameLibInfo()


def makeGraphicsWindow(width, height, fullscreen=False):
    _GLI.initGraphics()
    setGraphicsMode(width, height, fullscreen)


def getScreenSize():
    _GLI.initGraphics()
    return _GLI.display.getScreenSize()


def getAllScreenSizes():
    _GLI.initGraphics()
    return _GLI.display.getAllScreenSizes()


getActualFrameRate = _GLI.fps.getActualFPS
displayFPS = _GLI.fps.display

setBackground = _GLI.display.setBackground
setForeground = _GLI.display.setForeground

setGraphicsMode = _GLI.display.setGraphicsMode
getWindowWidth = _GLI.display.getWindowWidth
getWindowHeight = _GLI.display.getWindowHeight
setWindowTitle = _GLI.display.setWindowTitle

lookupColor = colors.lookupColor
getColorsList = colors.getColorsList

###################################################################

drawPixel = _GLI.display.drawPixel
drawLine = _GLI.display.drawLine
drawCircle = _GLI.display.drawCircle
fillCircle = _GLI.display.fillCircle
drawEllipse = _GLI.display.drawEllipse
fillEllipse = _GLI.display.fillEllipse
drawRectangle = _GLI.display.drawRectangle
fillRectangle = _GLI.display.fillRectangle
drawPolygon = _GLI.display.drawPolygon
fillPolygon = _GLI.display.fillPolygon
sizeString = _GLI.display.sizeString
drawString = _GLI.display.drawString
getFontList = _GLI.display.getFontList

getScreenPixel = _GLI.display.getScreenPixel


#########################################################

def loadImage(filename, transparentColor=None, rotate=0, scale=1, flipHorizontal=False, flipVertical=False):
    if transparentColor is None:
        image = pygame.image.load(filename).convert_alpha()
    else:
        image = pygame.image.load(filename).convert();
        if transparentColor is not False:
            image.set_colorkey(lookupColor(transparentColor))
    if flipHorizontal or flipVertical:
        image = pygame.transform.flip(image, flipHorizontal, flipVertical)
    if rotate != 0 or scale != 1:
        image = pygame.transform.rotozoom(image, rotate, scale)
    return image


def drawImage(image, x, y, rotate=0, scale=1, flipHorizontal=False, flipVertical=False):
    if flipHorizontal or flipVertical:
        image = pygame.transform.flip(image, flipHorizontal, flipVertical)
    if rotate != 0 or scale != 1:
        image = pygame.transform.rotozoom(image, rotate, scale)
    _GLI.screen.blit(image, (int(x - image.get_width() / 2), int(y - image.get_height() / 2)))


def getImageWidth(image):
    return image.get_width()


def getImageHeight(image):
    return image.get_height()


def getImagePixel(image, x, y):
    return image.get_at((int(x), int(y)))


def getImageRegion(image, x, y, width, height):
    return image.subsurface(pygame.Rect(int(x), int(y), int(width), int(height)))


def saveImage(image, filename):
    pygame.image.save(image, filename)


def saveScreen(filename):
    pygame.image.save(_GLI.screen, filename)


#########################################################

loadSound = _GLI.audio.loadSound
playSound = _GLI.audio.playSound
stopSound = _GLI.audio.stopSound
loadMusic = _GLI.audio.loadMusic
playMusic = _GLI.audio.playMusic
stopMusic = _GLI.audio.stopMusic


#########################################################


def onKeyPress(listenerFunction, key):
    key = getKeyCode(key)
    if key is None:
        raise Exception("that is not a valid key")
    _GLI.eventListeners[("keydown", key)] = listenerFunction


def onAnyKeyPress(listenerFunction):
    _GLI.eventListeners["keydown"] = listenerFunction


def onKeyRelease(listenerFunction, key):
    key = getKeyCode(key)
    if key == None:
        raise Exception("that is not a valid key")
    _GLI.eventListeners[("keyup", key)] = listenerFunction


def onAnyKeyRelease(listenerFunction):
    _GLI.eventListeners["keyup"] = listenerFunction


def onMousePress(listenerFunction):
    _GLI.eventListeners["mousedown"] = listenerFunction


def onMouseRelease(listenerFunction):
    _GLI.eventListeners["mouseup"] = listenerFunction


def onWheelForward(listenerFunction):
    _GLI.eventListeners["wheelforward"] = listenerFunction


def onWheelBackward(listenerFunction):
    _GLI.eventListeners["wheelbackward"] = listenerFunction


def onMouseMotion(listenerFunction):
    _GLI.eventListeners["mousemotion"] = listenerFunction


def onGameControllerStick(listenerFunction):
    _GLI.eventListeners["stickmotion"] = listenerFunction


def onGameControllerDPad(listenerFunction):
    _GLI.eventListeners["dpadmotion"] = listenerFunction


def onGameControllerButtonPress(listenerFunction):
    _GLI.eventListeners["joybuttondown"] = listenerFunction


def onGameControllerButtonRelease(listenerFunction):
    _GLI.eventListeners["joybuttonup"] = listenerFunction


def onTimer(listenerFunction, interval):
    if _GLI.nextEventType > pygame.NUMEVENTS:
        raise ValueError, "too many timer listeners"
    _GLI.eventListeners["timer" + str(_GLI.nextEventType)] = listenerFunction
    pygame.time.set_timer(_GLI.nextEventType, interval)
    _GLI.nextEventType += 1


#########################################################

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


def isKeyPressed(key):
    key = getKeyCode(key)
    return _GLI.keysPressedNow.get(key, False)


def getKeyName(key):
    return keys.key2nameDict.get(key, None)


def getKeyCode(key):
    if key is None:
        return None
    if key in keys.key2nameDict:
        return key
    return keys.name2keyDict.get(key.lower(), None)


def sameKeys(key1, key2):
    code1 = getKeyCode(key1)
    code2 = getKeyCode(key2)
    if code1 is None:
        raise Exception, "unknown key name: " + key1
    if code2 is None:
        raise Exception, "unknown key name: " + key2
    return code1 == code2


#########################################################

numGameControllers = _GLI.joyinfo.getJoystickCount
gameControllerSetDeadZone = _GLI.joyinfo.setDeadzone

gameControllerNumStickAxes = _GLI.joyinfo.getAxisCount
gameControllerGetStickAxesNames = _GLI.joyinfo.getAxisNames
gameControllerSetStickAxesNames = _GLI.joyinfo.setAxisNames
gameControllerStickAxis = _GLI.joyinfo.getAxis

gameControllerNumButtons = _GLI.joyinfo.getButtonCount
gameControllerButton = _GLI.joyinfo.getButton

gameControllerNumDPads = _GLI.joyinfo.getDPadCount
gameControllerDPadX = _GLI.joyinfo.getDPadX
gameControllerDPadY = _GLI.joyinfo.getDPadY


#########################################################
# Math functions

def polarToCartesian(angle, length):
    angle = math.radians(angle)
    dx = length * math.cos(angle)
    dy = length * -math.sin(angle)
    return (dx, dy)


def cartesianToPolarAngle(x, y):
    return math.degrees(math.atan2(-y, x))


def pointInPolygon(x, y, polygon):
    # original author: W. Randolph Franklin
    # source: http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
    inside = False
    length = len(polygon)
    i = 0
    j = length - 1
    while i < length:
        (vix, viy) = polygon[i]
        (vjx, vjy) = polygon[j]
        if (((viy > y) != (vjy > y)) and
                (x < (vjx - vix) * (y - viy) / float(vjy - viy) + vix)):
            inside = not inside
        j = i
        i += 1
    return inside


#########################################################


def endGraphics():
    _GLI.keepRunning = False


# use animate for non-interactive animations
def animate(drawFunction, timeLimit, repeat=False):
    def startAnimation(world):
        pass

    def timeExpired(world):
        if getElapsedTime() >= timeLimit:
            if repeat:
                resetTime()
            else:
                _GLI.keepRunning = False

    def drawAnimationFrame(world):
        drawFunction(float(getElapsedTime()))

    runGraphics(startAnimation, timeExpired, drawAnimationFrame)


# use runGraphics for interactive programs like games
def runGraphics(startFunction, updateFunction, drawFunction):
    try:
        _GLI.startGame()
        _GLI.world = World()
        startFunction(_GLI.world)
        while _GLI.keepRunning:
            eventlist = pygame.event.get()
            for event in eventlist:
                if event.type == pygame.QUIT:
                    _GLI.keepRunning = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        _GLI.keepRunning = False
                        break
                    else:
                        _GLI.keysPressedNow[event.key] = True
                        if ("keydown", event.key) in _GLI.eventListeners:
                            _GLI.eventListeners[("keydown", event.key)](_GLI.world)
                        else:
                            _GLI.eventListeners["keydown"](_GLI.world, event.key)
                elif event.type == pygame.KEYUP:
                    _GLI.keysPressedNow[event.key] = False
                    if ("keyup", event.key) in _GLI.eventListeners:
                        _GLI.eventListeners[("keyup", event.key)](_GLI.world)
                    else:
                        _GLI.eventListeners["keyup"](_GLI.world, event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button <= 3:
                        _GLI.eventListeners["mousedown"](_GLI.world, event.pos[0], event.pos[1], event.button)
                    elif event.button == 4:
                        _GLI.eventListeners["wheelforward"](_GLI.world, event.pos[0], event.pos[1])
                    elif event.button == 5:
                        _GLI.eventListeners["wheelbackward"](_GLI.world, event.pos[0], event.pos[1])
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button <= 3:
                        _GLI.eventListeners["mouseup"](_GLI.world, event.pos[0], event.pos[1], event.button)
                elif event.type == pygame.MOUSEMOTION:
                    if event.rel[0] != 0 or event.rel[1] != 0:
                        button1 = (event.buttons[0] == 1)
                        button2 = (event.buttons[1] == 1)
                        button3 = (event.buttons[2] == 1)
                        _GLI.eventListeners["mousemotion"](_GLI.world, event.pos[0], event.pos[1], event.rel[0],
                                                           event.rel[1], button1, button2, button3)
                elif event.type == pygame.JOYAXISMOTION:
                    joystickValue = _GLI.joyinfo.applyDeadzone(event.value)
                    _GLI.eventListeners["stickmotion"](_GLI.world, event.joy, event.axis, joystickValue)
                elif event.type == pygame.JOYHATMOTION:
                    _GLI.eventListeners["dpadmotion"](_GLI.world, event.joy, event.hat, event.value[0], event.value[1])
                elif event.type == pygame.JOYBUTTONUP:
                    _GLI.eventListeners["joybuttonup"](_GLI.world, event.joy, event.button + 1)
                elif event.type == pygame.JOYBUTTONDOWN:
                    _GLI.eventListeners["joybuttondown"](_GLI.world, event.joy, event.button + 1)
                elif event.type >= pygame.USEREVENT:  # timer event
                    _GLI.eventListeners["timer" + str(event.type)](_GLI.world)
            updateFunction(_GLI.world)
            _GLI.display.drawBackground()
            drawFunction(_GLI.world)
            pygame.display.flip()
            _GLI.fps.tick()
    finally:
        pygame.quit()


def getWorld():
    return _GLI.world


getElapsedTime = _GLI.fps.getElapsedTime
resetTime = _GLI.fps.resetTime
setFrameRate = _GLI.fps.setTargetFPS
