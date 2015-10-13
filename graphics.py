"""
This is a simple interactive graphics and animation library for Python.
Author: Andrew Merrill
Version: 3.8 (last updated October, 2015)

This code is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike license
see http://creativecommons.org/licenses/by-nc-sa/3.0/ for details
"""

print "using graphics.py library version 3.8"

import pygame, os, math, colors, keys


class World:
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameLibInfo:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.world = None
        self.graphicsInited = False
        self.fonts = dict()
        self.eventListeners = dict()
        self.frameRate = 60
        self.windowWidth = 0
        self.windowHeight = 0
        self.background = (255, 255, 255)
        self.foreground = (0, 0, 0)
        self.nextEventType = pygame.USEREVENT
        self.keysPressedNow = dict()
        self.FPStime = 0
        self.FPSinterval = 0
        self.FPScount = 0
        self.joysticks = []
        self.joystickLabels = []  # list of dictionaries
        self.numJoysticks = 0
        self.joystickDeadZone = 0.05
        self.joystickLabelDefault = [["X", "Y"]]
        self.joystickLabelDefaults = {
            "Logitech Dual Action": [["X", "Y"], ["LeftX", "LeftY", "RightX", "RightY"]],
            "Logitech RumblePad 2 USB": [["X", "Y"], ["LeftX", "LeftY", "RightX", "RightY"]],
            "Logitech Cordless RumblePad 2": [["X", "Y"], ["LeftX", "LeftY", "RightX", "RightY"]],
            "Logitech Attack 3": [["X", "Y", "Throttle"]],

            "Logitech Logitech Dual Action": [["X", "Y"], ["LeftX", "LeftY", "RightX", "RightY"]],
            "Logitech Logitech RumblePad 2 USB": [["X", "Y"], ["LeftX", "LeftY", "RightX", "RightY"]],
            "Logitech Logitech Cordless RumblePad 2": [["X", "Y"], ["LeftX", "LeftY", "RightX", "RightY"]],
            "Logitech Logitech Attack 3": [["X", "Y", "Throttle"]],

            "Controller (Gamepad F310)": [["X", "Y"], ["LeftX", "LeftY", "Trigger", "RightY", "RightX"]],
            "Controller (Wireless Gamepad F710)": [["X", "Y"], ["LeftX", "LeftY", "Trigger", "RightY", "RightX"]],

            "Saitek Aviator Stick": [["X", "Y", "LeftThrottle", "Twist", "RightThrottle"]],
            "Saitek AV8R Joystick": [["X", "Y", "Twist", "LeftThrottle", "RightThrottle"]],
            "Saitek Pro Flight Throttle Quadrant": [["LeftThrottle", "CenterThrottle", "RightThrottle"]],

            "XBOX 360 For Windows (Controller)": [["X", "Y"], ["LeftX", "LeftY", "Trigger", "RightY", "RightX"]]

        }

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

    def initializeJoysticks(self):
        self.numJoysticks = pygame.joystick.get_count()
        for id in range(self.numJoysticks):
            self.joysticks.append(pygame.joystick.Joystick(id))
            self.joystickLabels.append(dict())
            self.joysticks[id].init()
            stickname = self.joysticks[id].get_name()
            if stickname in self.joystickLabelDefaults:
                print "recognized a " + stickname
                labelList = self.joystickLabelDefaults[stickname]
            else:
                print "unknown game controller: " + stickname
                labelList = self.joystickLabelDefault
            for labels in labelList:
                gameControllerSetStickAxesNames(labels, id)
            print "    with axes:", gameControllerGetStickAxesNames()

    def startGame(self):
        self.clock = pygame.time.Clock()
        self.startTime = pygame.time.get_ticks()
        self.keepRunning = True

    def maybePrintFPS(self):
        self.FPScount += 1
        if self.FPSinterval > 0:
            time = pygame.time.get_ticks()
            if time > self.FPStime + self.FPSinterval:
                print getActualFrameRate()
                self.FPStime = time
                self.FPScount = 0


_GLI = GameLibInfo()


def makeGraphicsWindow(width, height, fullscreen=False):
    initGraphics()
    setGraphicsMode(width, height, fullscreen)


def initGraphics():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    _GLI.initialize()
    _GLI.initializeListeners()
    _GLI.initializeJoysticks()
    _GLI.graphicsInited = True


def endGraphics():
    _GLI.keepRunning = False


def setGraphicsMode(width, height, fullscreen=False):
    _GLI.windowWidth = width
    _GLI.windowHeight = height
    flags = 0
    if fullscreen == True:
        flags = flags | pygame.FULLSCREEN  # | pygame.DOUBLEBUF | pygame.HWSURFACE
    _GLI.screen = pygame.display.set_mode((width, height), flags)


def getScreenSize():
    initGraphics()
    info = pygame.display.Info()
    return (info.current_w, info.current_h)


def getAllScreenSizes():
    initGraphics()
    return pygame.display.list_modes()


def setBackground(background):
    if isinstance(background, str):
        _GLI.background = lookupColor(background)
    else:
        _GLI.background = background


def setForeground(foreground):
    _GLI.foreground = foreground


def getActualFrameRate():
    return _GLI.clock.get_fps()


def displayFPS(interval):
    _GLI.FPSinterval = interval * 1000
    _GLI.FPStime = pygame.time.get_ticks()
    _GLI.FPScount = 0


def getWindowWidth():
    return _GLI.windowWidth


def getWindowHeight():
    return _GLI.windowHeight


def setWindowTitle(title):
    pygame.display.set_caption(str(title))


def lookupColor(color):
    return colors.colorTable.get(color, color)


def getColorsList():
    return colors.colorNames


###################################################################

def drawPixel(x, y, color=_GLI.foreground):
    _GLI.screen.set_at((int(x), int(y)), lookupColor(color))


def drawLine(x1, y1, x2, y2, color=_GLI.foreground, thickness=1):
    pygame.draw.line(_GLI.screen, lookupColor(color), (int(x1), int(y1)), (int(x2), int(y2)), int(thickness))


def drawCircle(x, y, radius, color=_GLI.foreground, thickness=1):
    pygame.draw.circle(_GLI.screen, lookupColor(color), (int(x), int(y)), int(radius), int(thickness))


def fillCircle(x, y, radius, color=_GLI.foreground):
    drawCircle(x, y, radius, color, 0)


def drawEllipse(x, y, width, height, color=_GLI.foreground, thickness=1):
    pygame.draw.ellipse(_GLI.screen, lookupColor(color),
                        pygame.Rect(int(x - width / 2), int(y - height / 2), int(width), int(height)), int(thickness))


def fillEllipse(x, y, width, height, color=_GLI.foreground):
    drawEllipse(x, y, width, height, color, 0)


def drawRectangle(x, y, width, height, color=_GLI.foreground, thickness=1):
    pygame.draw.rect(_GLI.screen, lookupColor(color), pygame.Rect(int(x), int(y), int(width), int(height)),
                     int(thickness))


def fillRectangle(x, y, width, height, color=_GLI.foreground):
    drawRectangle(x, y, width, height, color, 0)


def drawPolygon(pointlist, color=_GLI.foreground, thickness=1):
    pygame.draw.polygon(_GLI.screen, lookupColor(color), pointlist, int(thickness))


def fillPolygon(pointlist, color=_GLI.foreground):
    drawPolygon(pointlist, color, 0)


def sizeString(text, size=30, bold=False, italic=False, font=None):
    fontSignature = (font, size, bold, italic)
    if fontSignature not in _GLI.fonts:
        font = pygame.font.SysFont(font, size, bold, italic)
        _GLI.fonts[fontSignature] = font
    else:
        font = _GLI.fonts[fontSignature]
    textimage = font.render(str(text), False, (1, 1, 1))
    return (textimage.get_width(), textimage.get_height())


def drawString(text, x, y, size=30, color=_GLI.foreground, bold=False, italic=False, font=None):
    fontSignature = (font, size, bold, italic)
    if fontSignature not in _GLI.fonts:
        font = pygame.font.SysFont(font, size, bold, italic)
        _GLI.fonts[fontSignature] = font
    else:
        font = _GLI.fonts[fontSignature]
    color = lookupColor(color)
    textimage = font.render(str(text), False, color)
    _GLI.screen.blit(textimage, (int(x), int(y)))
    return (textimage.get_width(), textimage.get_height())


def getFontList():
    return pygame.font.get_fonts()


#########################################################

def loadImage(filename, transparentColor=None, rotate=0, scale=1, flipHorizontal=False, flipVertical=False):
    if transparentColor == None:
        image = pygame.image.load(filename).convert_alpha()
    else:
        image = pygame.image.load(filename).convert();
        if transparentColor != False:
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


def getScreenPixel(x, y):
    if x < 0 or x >= _GLI.windowWidth or y < 0 or y >= _GLI.windowHeight:
        return None
    return _GLI.screen.get_at((int(x), int(y)))


def getImageRegion(image, x, y, width, height):
    return image.subsurface(pygame.Rect(int(x), int(y), int(width), int(height)))


def saveImage(image, filename):
    pygame.image.save(image, filename)


def saveScreen(filename):
    pygame.image.save(_GLI.screen, filename)


#########################################################

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

def numGameControllers():
    return _GLI.numJoysticks


def gameControllerNumStickAxes(device=0):
    if device < _GLI.numJoysticks:
        return _GLI.joysticks[device].get_numaxes()
    else:
        return 0


def gameControllerNumDPads(device=0):
    if device < _GLI.numJoysticks:
        return _GLI.joysticks[device].get_numhats()
    else:
        return 0


def gameControllerNumButtons(device=0):
    if device < _GLI.numJoysticks:
        return _GLI.joysticks[device].get_numbuttons()
    else:
        return 0


def gameControllerSetDeadZone(deadzone):
    _GLI.joystickDeadZone = deadzone


def gameControllerGetStickAxesNames(device=0):
    if device < _GLI.numJoysticks:
        labelDict = _GLI.joystickLabels[device]
        axes = labelDict.keys()
        axes.sort(key=lambda axis: labelDict[axis])
        return axes
    return []


def gameControllerStickAxis(axis, device=0):
    if device < _GLI.numJoysticks:
        joystick = _GLI.joysticks[device]
        labelDict = _GLI.joystickLabels[device]
        if axis in labelDict:
            axis = labelDict[axis]
        if axis < joystick.get_numaxes():
            value = joystick.get_axis(axis)
            if abs(value) > _GLI.joystickDeadZone:
                return value
    return 0


def gameControllerSetStickAxesNames(axesList, device=0):
    if device < _GLI.numJoysticks:
        labelDict = _GLI.joystickLabels[device]
        for i in range(len(axesList)):
            labelDict[axesList[i]] = i


def gameControllerButton(button, device=0):
    if device < _GLI.numJoysticks:
        joystick = _GLI.joysticks[device]
        button -= 1
        if button >= 0 and button < joystick.get_numbuttons():
            value = joystick.get_button(button)
            return (value == 1)
    return False


def gameControllerDPadX(dpad=0, device=0):
    if device < _GLI.numJoysticks:
        joystick = _GLI.joysticks[device]
        if dpad < joystick.get_numhats():
            (dx, dy) = joystick.get_hat(dpad)
            return dx
    return 0


def gameControllerDPadY(dpad=0, device=0):
    if device < _GLI.numJoysticks:
        joystick = _GLI.joysticks[device]
        if dpad < joystick.get_numhats():
            (dx, dy) = joystick.get_hat(dpad)
            return dy
    return 0


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
                    if abs(event.value) < _GLI.joystickDeadZone:
                        joystickValue = 0
                    else:
                        joystickValue = event.value
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
            if isinstance(_GLI.background, pygame.Surface):
                _GLI.screen.blit(_GLI.background, (0, 0))
            elif _GLI.background != None:
                _GLI.screen.fill(_GLI.background)
            drawFunction(_GLI.world)
            pygame.display.flip()
            _GLI.maybePrintFPS()
            _GLI.clock.tick(_GLI.frameRate)
    finally:
        pygame.quit()


def getWorld():
    return _GLI.world


def getElapsedTime():
    return pygame.time.get_ticks() - _GLI.startTime


def resetTime():
    _GLI.startTime = pygame.time.get_ticks()


def setFrameRate(frameRate):
    _GLI.frameRate = frameRate

###################################################################
# Backward Compatibility

addKeyDownListener = onKeyPress
addKeyUpListener = onKeyRelease
addMouseDownListener = onMousePress
addMouseUpListener = onMouseRelease
addKeyPressedListener = onKeyPress
addKeyReleasedListener = onKeyRelease
addMousePressedListener = onMousePress
addMouseReleasedListener = onMouseRelease
addWheelForwardListener = onWheelForward
addWheelBackwardListener = onWheelBackward
addMouseMotionListener = onMouseMotion
addGameControllerStickListener = onGameControllerStick
addGameControllerDPadListener = onGameControllerDPad
addGameControllerButtonPressedListener = onGameControllerButtonPress
addGameControllerButtonReleasedListener = onGameControllerButtonRelease
addTimerListener = onTimer
keyPressedNow = isKeyPressed
