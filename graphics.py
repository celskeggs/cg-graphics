"""
This is a simple interactive graphics and animation library for Python.
Author: Andrew Merrill
Version: 3.8 (last updated October, 2015)

This code is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike license
see http://creativecommons.org/licenses/by-nc-sa/3.0/ for details
"""

print "using graphics.py library version 3.8"

import pygame, colors, keys, joysticks, fps, display, audio, gmath, image, keyboard, events


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
        self.joyinfo = joysticks.JoysticksInfo()
        self.keys = keyboard.Keys()
        self.fps = fps.GameClock()

        self.graphicsInited = False
        self.eventListeners = {}
        self.nextEventType = pygame.USEREVENT
        self.keepRunning = False

    def initGraphics(self):
        if not self.graphicsInited:
            self.display.initialize()
            self.initializeListeners()
            self.joyinfo.initialize()
            self.keys.initialize()
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


@events.handler(pygame.QUIT)
def quit(event, _):
    _GLI.keepRunning = False


@events.handler(pygame.KEYDOWN)
def key_down(event, _):
    if event.key == pygame.K_ESCAPE:
        _GLI.keepRunning = False


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

saveScreen = _GLI.display.saveScreen
getScreenPixel = _GLI.display.getScreenPixel

lookupColor = colors.lookupColor
getColorsList = colors.getColorsList

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

loadImage = image.loadImage
saveImage = image.saveImage
getImageWidth = image.getImageWidth
getImageHeight = image.getImageHeight
getImagePixel = image.getImagePixel
getImageRegion = image.getImageRegion

loadSound = audio.loadSound
playSound = audio.playSound
stopSound = audio.stopSound
loadMusic = audio.loadMusic
playMusic = audio.playMusic
stopMusic = audio.stopMusic


#########################################################


onKeyPress = keyboard.onKeyPress
onAnyKeyPress = keyboard.onAnyKeyPress
onKeyRelease = keyboard.onKeyRelease
onAnyKeyRelease = keyboard.onAnyKeyRelease


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


onGameControllerStick = _GLI.joyinfo.onGameControllerStick
onGameControllerDPad = _GLI.joyinfo.onGameControllerDPad
onGameControllerButtonPress = _GLI.joyinfo.onGameControllerButtonPress
onGameControllerButtonRelease = _GLI.joyinfo.onGameControllerButtonRelease


def onTimer(listenerFunction, interval):
    if _GLI.nextEventType > pygame.NUMEVENTS:
        raise ValueError, "too many timer listeners"
    _GLI.eventListeners["timer" + str(_GLI.nextEventType)] = listenerFunction
    pygame.time.set_timer(_GLI.nextEventType, interval)
    _GLI.nextEventType += 1


#########################################################

getMousePosition = keyboard.getMousePosition
getMouseButton = keyboard.getMouseButton
hideMouse = keyboard.hideMouse
showMouse = keyboard.showMouse
moveMouse = keyboard.moveMouse

isKeyPressed = _GLI.keys.isKeyPressed

getKeyName = keys.getKeyName
getKeyCode = keys.getKeyCode
sameKeys = keys.sameKeys

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

polarToCartesian = gmath.polarToCartesian
cartesianToPolarAngle = gmath.cartesianToPolarAngle
pointInPolygon = gmath.pointInPolygon


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
            events.pump(_GLI)
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
