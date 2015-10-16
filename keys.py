import pygame

keyList = [
    (pygame.K_UP, ['up', 'up arrow']),
    (pygame.K_DOWN, ['down', 'down arrow']),
    (pygame.K_RIGHT, ['right', 'right arrow']),
    (pygame.K_LEFT, ['left', 'left arrow']),
    (pygame.K_BACKSPACE, ['backspace']),
    (pygame.K_SPACE, ['space', ' ']),
    (pygame.K_RETURN, ['enter', 'return']),
    (pygame.K_TAB, ['tab']),

    (pygame.K_a, ['a']),
    (pygame.K_b, ['b']),
    (pygame.K_c, ['c']),
    (pygame.K_d, ['d']),
    (pygame.K_e, ['e']),
    (pygame.K_f, ['f']),
    (pygame.K_g, ['g']),
    (pygame.K_h, ['h']),
    (pygame.K_i, ['i']),
    (pygame.K_j, ['j']),
    (pygame.K_k, ['k']),
    (pygame.K_l, ['l']),
    (pygame.K_m, ['m']),
    (pygame.K_n, ['n']),
    (pygame.K_o, ['o']),
    (pygame.K_p, ['p']),
    (pygame.K_q, ['q']),
    (pygame.K_r, ['r']),
    (pygame.K_s, ['s']),
    (pygame.K_t, ['t']),
    (pygame.K_u, ['u']),
    (pygame.K_v, ['v']),
    (pygame.K_w, ['w']),
    (pygame.K_x, ['x']),
    (pygame.K_y, ['y']),
    (pygame.K_z, ['z']),
    (pygame.K_0, ['0']),
    (pygame.K_1, ['1']),
    (pygame.K_2, ['2']),
    (pygame.K_3, ['3']),
    (pygame.K_4, ['4']),
    (pygame.K_5, ['5']),
    (pygame.K_6, ['6']),
    (pygame.K_7, ['7']),
    (pygame.K_8, ['8']),
    (pygame.K_9, ['9']),

    (pygame.K_BACKQUOTE, ['`', 'backquote', 'grave', 'grave accent']),
    (pygame.K_MINUS, ['-', 'minus', 'dash', 'hyphen']),
    (pygame.K_EQUALS, ['=', 'equals']),
    (pygame.K_LEFTBRACKET, ['[', 'left bracket']),
    (pygame.K_RIGHTBRACKET, [']', 'right bracket']),
    (pygame.K_BACKSLASH, ['backslash', '\\']),
    (pygame.K_SEMICOLON, [';', 'semicolon']),
    (pygame.K_QUOTE, ['quote', '\'']),
    (pygame.K_COMMA, [',', 'comma']),
    (pygame.K_PERIOD, ['.', 'period']),
    (pygame.K_SLASH, ['/', 'slash', 'divide']),

    (pygame.K_DELETE, ['delete']),
    (pygame.K_INSERT, ['insert']),
    (pygame.K_HOME, ['home']),
    (pygame.K_END, ['end']),
    (pygame.K_PAGEUP, ['page up']),
    (pygame.K_PAGEDOWN, ['page down']),
    (pygame.K_CLEAR, ['clear']),
    (pygame.K_PAUSE, ['pause']),

    (pygame.K_F1, ['F1']),
    (pygame.K_F2, ['F2']),
    (pygame.K_F3, ['F3']),
    (pygame.K_F4, ['F4']),
    (pygame.K_F5, ['F5']),
    (pygame.K_F6, ['F6']),
    (pygame.K_F7, ['F7']),
    (pygame.K_F8, ['F8']),
    (pygame.K_F9, ['F9']),
    (pygame.K_F10, ['F10']),
    (pygame.K_F11, ['F11']),
    (pygame.K_F12, ['F12']),
    (pygame.K_F13, ['F13']),
    (pygame.K_F14, ['F14']),
    (pygame.K_F15, ['F15']),

    (pygame.K_RSHIFT, ['right shift']),
    (pygame.K_LSHIFT, ['left shift']),
    (pygame.K_RCTRL, ['right ctrl']),
    (pygame.K_LCTRL, ['left ctrl']),
    (pygame.K_RALT, ['right alt', 'right option']),
    (pygame.K_LALT, ['left alt', 'left option']),
    (pygame.K_RMETA, ['right command']),
    (pygame.K_LMETA, ['left command']),
    (pygame.K_LSUPER, ['left windows']),
    (pygame.K_RSUPER, ['right windows']),

    (pygame.K_NUMLOCK, ['numlock']),
    (pygame.K_CAPSLOCK, ['capslock']),
    (pygame.K_SCROLLOCK, ['scrollock']),
    (pygame.K_MODE, ['mode']),
    (pygame.K_HELP, ['help']),
    (pygame.K_PRINT, ['print', 'print screen', 'prtsc']),
    (pygame.K_SYSREQ, ['sysrq']),
    (pygame.K_BREAK, ['break']),
    (pygame.K_MENU, ['menu']),
    (pygame.K_POWER, ['power']),
    (pygame.K_EURO, ['euro']),

    (pygame.K_KP0, ['keypad 0']),
    (pygame.K_KP1, ['keypad 1']),
    (pygame.K_KP2, ['keypad 2']),
    (pygame.K_KP3, ['keypad 3']),
    (pygame.K_KP4, ['keypad 4']),
    (pygame.K_KP5, ['keypad 5']),
    (pygame.K_KP6, ['keypad 6']),
    (pygame.K_KP7, ['keypad 7']),
    (pygame.K_KP8, ['keypad 8']),
    (pygame.K_KP9, ['keypad 9']),
    (pygame.K_KP_PERIOD, ['keypad period']),
    (pygame.K_KP_DIVIDE, ['keypad divide']),
    (pygame.K_KP_MULTIPLY, ['keypad multiply']),
    (pygame.K_KP_MINUS, ['keypad minus']),
    (pygame.K_KP_PLUS, ['keypad plus']),
    (pygame.K_KP_EQUALS, ['keypad equals']),
    (pygame.K_KP_ENTER, ['keypad enter'])
]

key2nameDict = {}
name2keyDict = {}
for code, nameList in keyList:
    key2nameDict[code] = nameList[0].lower()
    for name in nameList:
        name2keyDict[name.lower()] = code


def getKeyName(key):
    return key2nameDict.get(key, None)


def getKeyCode(key):
    if key is None:
        return None
    if key in key2nameDict:
        return key
    return name2keyDict.get(key.lower(), None)


def sameKeys(key1, key2):
    code1 = getKeyCode(key1)
    code2 = getKeyCode(key2)
    if code1 is None:
        raise Exception, "unknown key name: " + key1
    if code2 is None:
        raise Exception, "unknown key name: " + key2
    return code1 == code2


if __name__ == "__main__":
    with open("keys.html", "w") as web:
        web.write('<html><head><title>Python Keys</title></head>\n<body><center>\n<h1>Key Names</h1>\n<table>\n')
        for code, nameList in keyList:
            web.write('<tr>')
            for name in nameList:
                web.write('<td>' + name + '</td>')
            web.write('</tr>')
        web.write('</table></center></body></html>')
