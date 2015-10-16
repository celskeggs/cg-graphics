import sdl2

keyList = [
    (sdl2.SDLK_UP, ['up', 'up arrow']),
    (sdl2.SDLK_DOWN, ['down', 'down arrow']),
    (sdl2.SDLK_RIGHT, ['right', 'right arrow']),
    (sdl2.SDLK_LEFT, ['left', 'left arrow']),
    (sdl2.SDLK_BACKSPACE, ['backspace']),
    (sdl2.SDLK_SPACE, ['space', ' ']),
    (sdl2.SDLK_RETURN, ['enter', 'return']),
    (sdl2.SDLK_TAB, ['tab']),

    (sdl2.SDLK_a, ['a']),
    (sdl2.SDLK_b, ['b']),
    (sdl2.SDLK_c, ['c']),
    (sdl2.SDLK_d, ['d']),
    (sdl2.SDLK_e, ['e']),
    (sdl2.SDLK_f, ['f']),
    (sdl2.SDLK_g, ['g']),
    (sdl2.SDLK_h, ['h']),
    (sdl2.SDLK_i, ['i']),
    (sdl2.SDLK_j, ['j']),
    (sdl2.SDLK_k, ['k']),
    (sdl2.SDLK_l, ['l']),
    (sdl2.SDLK_m, ['m']),
    (sdl2.SDLK_n, ['n']),
    (sdl2.SDLK_o, ['o']),
    (sdl2.SDLK_p, ['p']),
    (sdl2.SDLK_q, ['q']),
    (sdl2.SDLK_r, ['r']),
    (sdl2.SDLK_s, ['s']),
    (sdl2.SDLK_t, ['t']),
    (sdl2.SDLK_u, ['u']),
    (sdl2.SDLK_v, ['v']),
    (sdl2.SDLK_w, ['w']),
    (sdl2.SDLK_x, ['x']),
    (sdl2.SDLK_y, ['y']),
    (sdl2.SDLK_z, ['z']),
    (sdl2.SDLK_0, ['0']),
    (sdl2.SDLK_1, ['1']),
    (sdl2.SDLK_2, ['2']),
    (sdl2.SDLK_3, ['3']),
    (sdl2.SDLK_4, ['4']),
    (sdl2.SDLK_5, ['5']),
    (sdl2.SDLK_6, ['6']),
    (sdl2.SDLK_7, ['7']),
    (sdl2.SDLK_8, ['8']),
    (sdl2.SDLK_9, ['9']),

    (sdl2.SDLK_BACKQUOTE, ['`', 'backquote', 'grave', 'grave accent']),
    (sdl2.SDLK_MINUS, ['-', 'minus', 'dash', 'hyphen']),
    (sdl2.SDLK_EQUALS, ['=', 'equals']),
    (sdl2.SDLK_LEFTBRACKET, ['[', 'left bracket']),
    (sdl2.SDLK_RIGHTBRACKET, [']', 'right bracket']),
    (sdl2.SDLK_BACKSLASH, ['backslash', '\\']),
    (sdl2.SDLK_SEMICOLON, [';', 'semicolon']),
    (sdl2.SDLK_QUOTE, ['quote', '\'']),
    (sdl2.SDLK_COMMA, [',', 'comma']),
    (sdl2.SDLK_PERIOD, ['.', 'period']),
    (sdl2.SDLK_SLASH, ['/', 'slash', 'divide']),

    (sdl2.SDLK_DELETE, ['delete']),
    (sdl2.SDLK_INSERT, ['insert']),
    (sdl2.SDLK_HOME, ['home']),
    (sdl2.SDLK_END, ['end']),
    (sdl2.SDLK_PAGEUP, ['page up']),
    (sdl2.SDLK_PAGEDOWN, ['page down']),
    (sdl2.SDLK_CLEAR, ['clear']),
    (sdl2.SDLK_PAUSE, ['pause']),

    (sdl2.SDLK_F1, ['F1']),
    (sdl2.SDLK_F2, ['F2']),
    (sdl2.SDLK_F3, ['F3']),
    (sdl2.SDLK_F4, ['F4']),
    (sdl2.SDLK_F5, ['F5']),
    (sdl2.SDLK_F6, ['F6']),
    (sdl2.SDLK_F7, ['F7']),
    (sdl2.SDLK_F8, ['F8']),
    (sdl2.SDLK_F9, ['F9']),
    (sdl2.SDLK_F10, ['F10']),
    (sdl2.SDLK_F11, ['F11']),
    (sdl2.SDLK_F12, ['F12']),
    (sdl2.SDLK_F13, ['F13']),
    (sdl2.SDLK_F14, ['F14']),
    (sdl2.SDLK_F15, ['F15']),

    (sdl2.SDLK_RSHIFT, ['right shift']),
    (sdl2.SDLK_LSHIFT, ['left shift']),
    (sdl2.SDLK_RCTRL, ['right ctrl']),
    (sdl2.SDLK_LCTRL, ['left ctrl']),
    (sdl2.SDLK_RALT, ['right alt', 'right option']),
    (sdl2.SDLK_LALT, ['left alt', 'left option']),
    (sdl2.SDLK_RGUI, ['right command', 'right windows']),  # apparently GUI <- META & SUPER?
    (sdl2.SDLK_LGUI, ['left command', 'left windows']),

    (sdl2.SDLK_NUMLOCKCLEAR, ['numlock']),
    (sdl2.SDLK_CAPSLOCK, ['capslock']),
    (sdl2.SDLK_SCROLLLOCK, ['scrollock']),
    (sdl2.SDLK_MODE, ['mode']),
    (sdl2.SDLK_HELP, ['help']),
    (sdl2.SDLK_PRINTSCREEN, ['print', 'print screen', 'prtsc']),
    (sdl2.SDLK_SYSREQ, ['sysrq']),
    (sdl2.SDLK_PAUSE, ['break']),
    (sdl2.SDLK_MENU, ['menu']),
    (sdl2.SDLK_POWER, ['power']),
    (sdl2.SDLK_CURRENCYUNIT, ['euro']),  # I'm not sure if this is correct but it's what pygame_sdl2 does

    (sdl2.SDLK_KP_0, ['keypad 0']),
    (sdl2.SDLK_KP_1, ['keypad 1']),
    (sdl2.SDLK_KP_2, ['keypad 2']),
    (sdl2.SDLK_KP_3, ['keypad 3']),
    (sdl2.SDLK_KP_4, ['keypad 4']),
    (sdl2.SDLK_KP_5, ['keypad 5']),
    (sdl2.SDLK_KP_6, ['keypad 6']),
    (sdl2.SDLK_KP_7, ['keypad 7']),
    (sdl2.SDLK_KP_8, ['keypad 8']),
    (sdl2.SDLK_KP_9, ['keypad 9']),
    (sdl2.SDLK_KP_PERIOD, ['keypad period']),
    (sdl2.SDLK_KP_DIVIDE, ['keypad divide']),
    (sdl2.SDLK_KP_MULTIPLY, ['keypad multiply']),
    (sdl2.SDLK_KP_MINUS, ['keypad minus']),
    (sdl2.SDLK_KP_PLUS, ['keypad plus']),
    (sdl2.SDLK_KP_EQUALS, ['keypad equals']),
    (sdl2.SDLK_KP_ENTER, ['keypad enter'])
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
