import sdl2, colors

DEFAULT_BACKGROUND = (255, 255, 255)
DEFAULT_FOREGROUND = (0, 0, 0)


class Display:
    def __init__(self):
        self.windowWidth, self.windowHeight = 0, 0
        self.background = DEFAULT_BACKGROUND
        self.foreground = DEFAULT_FOREGROUND
        self.window = None
        self.renderer = None
        self.fonts = {}

    def initialize(self):
        sdl2.SDL_SetHint(sdl2.SDL_HINT_RENDER_SCALE_QUALITY, "linear")

    def setGraphicsMode(self, width, height, fullscreen=False):
        self.windowWidth, self.windowHeight = width, height
        if fullscreen:
            self.window = sdl2.SDL_CreateWindow("graphics.py", sdl2.SDL_WINDOWPOS_UNDEFINED,
                                                sdl2.SDL_WINDOWPOS_UNDEFINED, 0, 0, sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)
        else:
            self.window = sdl2.SDL_CreateWindow("graphics.py", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
                                                width, height, 0)
        assert self.window is not None, "Could not create window: %s" % sdl2.SDL_GetError()
        self.renderer = sdl2.SDL_CreateRenderer(self.window, -1, 0)
        assert self.renderer is not None, "Could not create renderer: %s" % sdl2.SDL_GetError()
        if fullscreen:
            assert sdl2.SDL_RenderSetLogicalSize(self.renderer, width,
                                                 height) == 0, "Could not set logical size: %s" % sdl2.SDL_GetError()

    def getWindowWidth(self):
        return self.windowWidth

    def getWindowHeight(self):
        return self.windowHeight

    def setWindowTitle(self, title):
        sdl2.SDL_SetWindowTitle(self.window, str(title))

    def drawPixel(self, x, y, color=DEFAULT_FOREGROUND):
        self.screen.set_at((int(x), int(y)), colors.lookupColor(color))

    def getScreenPixel(self, x, y):
        if 0 <= x < self.windowWidth and 0 <= y < self.windowHeight:
            return self.screen.get_at((int(x), int(y)))
        else:
            return None

    def drawLine(self, x1, y1, x2, y2, color=DEFAULT_FOREGROUND, thickness=1):
        pygame.draw.line(self.screen, colors.lookupColor(color), (int(x1), int(y1)), (int(x2), int(y2)), int(thickness))

    def drawCircle(self, x, y, radius, color=DEFAULT_FOREGROUND, thickness=1):
        pygame.draw.circle(self.screen, colors.lookupColor(color), (int(x), int(y)), int(radius), int(thickness))

    def fillCircle(self, x, y, radius, color=DEFAULT_FOREGROUND):
        self.drawCircle(x, y, radius, color, 0)

    def drawEllipse(self, x, y, width, height, color=DEFAULT_FOREGROUND, thickness=1):
        pygame.draw.ellipse(self.screen, colors.lookupColor(color),
                            pygame.Rect(int(x - width / 2), int(y - height / 2), int(width), int(height)),
                            int(thickness))

    def fillEllipse(self, x, y, width, height, color=DEFAULT_FOREGROUND):
        self.drawEllipse(x, y, width, height, color, 0)

    def drawRectangle(self, x, y, width, height, color=DEFAULT_FOREGROUND, thickness=1):
        pygame.draw.rect(self.screen, colors.lookupColor(color), pygame.Rect(int(x), int(y), int(width), int(height)),
                         int(thickness))

    def fillRectangle(self, x, y, width, height, color=DEFAULT_FOREGROUND):
        self.drawRectangle(x, y, width, height, color, 0)

    def drawPolygon(self, pointlist, color=DEFAULT_FOREGROUND, thickness=1):
        pygame.draw.polygon(self.screen, colors.lookupColor(color), pointlist, int(thickness))

    def fillPolygon(self, pointlist, color=DEFAULT_FOREGROUND):
        self.drawPolygon(pointlist, color, 0)

    # internal only
    def getCachedFont(self, bold, font, italic, size):
        fontSignature = (font, size, bold, italic)
        if fontSignature not in self.fonts:
            self.fonts[fontSignature] = pygame.font.SysFont(font, size, bold, italic)
        return self.fonts[fontSignature]

    def sizeString(self, text, size=30, bold=False, italic=False, font=None):
        font = self.getCachedFont(bold, font, italic, size)
        textimage = font.render(str(text), False, (1, 1, 1))
        return textimage.get_width(), textimage.get_height()

    def drawString(self, text, x, y, size=30, color=DEFAULT_FOREGROUND, bold=False, italic=False, font=None):
        color = colors.lookupColor(color)
        font = self.getCachedFont(bold, font, italic, size)
        textimage = font.render(str(text), False, color)
        self.screen.blit(textimage, (int(x), int(y)))
        return textimage.get_width(), textimage.get_height()

    def drawImage(self, image, x, y, rotate=0, scale=1, flipHorizontal=False, flipVertical=False):
        if flipHorizontal or flipVertical:
            image = pygame.transform.flip(image, flipHorizontal, flipVertical)
        if rotate != 0 or scale != 1:
            image = pygame.transform.rotozoom(image, rotate, scale)
        self.screen.blit(image, (int(x - image.get_width() / 2), int(y - image.get_height() / 2)))

    def getFontList(self):
        return pygame.font.get_fonts()

    def setBackground(self, background):
        self.background = colors.lookupColor(background)

    def setForeground(self, foreground):
        self.foreground = colors.lookupColor(foreground)

    def drawBackground(self):
        if isinstance(self.background, sdl2.SDL_Texture):
            # TODO: does this handle stretching right?
            assert sdl2.SDL_RenderCopy(self.renderer, self.background, None,
                                       None) == 0, "Could not render background: %s" % sdl2.SDL_GetError()
        elif self.background is not None:
            r, g, b = self.background
            assert sdl2.SDL_SetRenderDrawColor(self.renderer, r, g, b,
                                               255) == 0, "Could not set render color: %s" % sdl2.SDL_GetError()
            assert sdl2.SDL_RenderClear(self.renderer) == 0, "Could not set render color: %s" % sdl2.SDL_GetError()

    def getAllScreenSizes(self):
        return pygame.display.list_modes()

    def getScreenSize(self):
        info = pygame.display.Info()
        return info.current_w, info.current_h

    def saveScreen(self, filename):
        pygame.image.save(self.screen, filename)

    def renderWithFunction(self, renderer):
        self.drawBackground()
        renderer()
        sdl2.SDL_RenderPresent(self.renderer)
