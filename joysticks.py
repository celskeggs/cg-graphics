import pygame, events

joystickLabels = {
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

joystickLabelsUnknown = [["X", "Y"]]


class JoysticksInfo:
    def __init__(self):
        self.joysticks = []
        self.joystickLabels = []
        self.joystickDeadZone = 0.05

    def initialize(self):
        for i in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
            self.joystickLabels.append({})
            self.joysticks[i].init()
            stickname = self.joysticks[i].get_name()
            if stickname in joystickLabels:
                print "recognized a", stickname
                label_list = joystickLabels[stickname]
            else:
                print "unknown game controller:", stickname
                label_list = joystickLabelsUnknown
            for labels in label_list:
                self.setAxisNames(labels, i)
            print "    with axes:", self.getAxisNames(i)

    def setDeadzone(self, deadzone):
        self.joystickDeadZone = deadzone

    def getJoystickCount(self):
        return len(self.joysticks)

    def getAxisCount(self, device=0):
        if 0 <= device < len(self.joysticks):
            return self.joysticks[device].get_numaxes()
        else:
            return 0

    def getDPadCount(self, device=0):
        if 0 <= device < len(self.joysticks):
            return self.joysticks[device].get_numhats()
        else:
            return 0

    def getButtonCount(self, device=0):
        if 0 <= device < len(self.joysticks):
            return self.joysticks[device].get_numbuttons()
        else:
            return 0

    def getAxisNames(self, device=0):
        if 0 <= device < len(self.joysticks):
            label_dict = self.joystickLabels[device]
            axes = label_dict.keys()
            axes.sort(key=lambda axis: label_dict[axis])
            return axes
        return []

    def getAxis(self, axis, device=0):
        if 0 <= device < len(self.joysticks):
            joystick = self.joysticks[device]
            label_dict = self.joystickLabels[device]
            if axis in label_dict:
                axis = label_dict[axis]
            if 0 <= axis < joystick.get_numaxes():
                return self.applyDeadzone(joystick.get_axis(axis))
        return 0

    def setAxisNames(self, axis_list, device=0):
        if 0 <= device < len(self.joysticks):
            label_dict = self.joystickLabels[device]
            for i in range(len(axis_list)):
                label_dict[axis_list[i]] = i

    def getButton(self, button, device=0):
        if 0 <= device < len(self.joysticks):
            joystick = self.joysticks[device]
            button -= 1
            if 0 <= button < joystick.get_numbuttons():
                value = joystick.get_button(button)
                return value == 1
        return False

    def getDPad(self, dpad=0, device=0):
        if 0 <= device < len(self.joysticks):
            joystick = self.joysticks[device]
            if dpad < joystick.get_numhats():
                dx, dy = joystick.get_hat(dpad)
                return dx, dy
        return 0, 0

    def getDPadX(self, dpad=0, device=0):
        dx, dy = self.getDPad(dpad, device)
        return dx

    def getDPadY(self, dpad=0, device=0):
        dx, dy = self.getDPad(dpad, device)
        return dy

    def applyDeadzone(self, value):
        if abs(value) < self.joystickDeadZone:
            return 0
        else:
            return value

    def onGameControllerStick(self, listenerFunction):
        def joystick_motion_handler(event, _GLI):
            listenerFunction(_GLI.world, event.joy, event.axis, self.applyDeadzone(event.value))

        events.handler(pygame.JOYAXISMOTION, joystick_motion_handler)

    def onGameControllerDPad(self, listenerFunction):
        def dpad_motion_handler(event, _GLI):
            listenerFunction(_GLI.world, event.joy, event.hat, event.value[0], event.value[1])

        events.handler(pygame.JOYHATMOTION, dpad_motion_handler)

    def onGameControllerButtonPress(self, listenerFunction):
        def joystick_button_press_handler(event, _GLI):
            listenerFunction(_GLI.world, event.joy, event.button + 1)

        events.handler(pygame.JOYBUTTONDOWN, joystick_button_press_handler)

    def onGameControllerButtonRelease(self, listenerFunction):
        def joystick_button_release_handler(event, _GLI):
            listenerFunction(_GLI.world, event.joy, event.button + 1)

        events.handler(pygame.JOYBUTTONUP, joystick_button_release_handler)
