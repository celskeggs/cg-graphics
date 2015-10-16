import sdl2, colors

DEFAULT_BACKGROUND = (255, 255, 255)
DEFAULT_FOREGROUND = (0, 0, 0)


class Display:
    def __init__(self):
        self.windowWidth, self.windowHeight = 0, 0
        self.background = DEFAULT_BACKGROUND
        self.foreground = DEFAULT_FOREGROUND
        self.screen = None
        self.fonts = {}

    def setGraphicsMode(self, width, height, fullscreen=False):
        self.windowWidth, self.windowHeight = width, height
        flags = 0
        if fullscreen:
            flags |= sdl2.SDL_WINDOW_FULLSCREEN
            # TODO: pygame.DOUBLEBUF or pygame.HWSURFACE?
        self.screen = pygame.display.set_mode((width, height), flags)

    def getWindowWidth(self):
        return self.windowWidth

    def getWindowHeight(self):
        return self.windowHeight

    def setWindowTitle(self, title):
        pygame.display.set_caption(str(title))

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
        if isinstance(self.background, pygame.Surface):
            self.screen.blit(self.background, (0, 0))
        elif self.background is not None:
            self.screen.fill(self.background)

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
        pygame.display.flip()
