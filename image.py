import sdl2, colors


def loadImage(filename, transparentColor=None, rotate=0, scale=1, flipHorizontal=False, flipVertical=False):
    if transparentColor is None:
        image = pygame.image.load(filename).convert_alpha()
    else:
        image = pygame.image.load(filename).convert()
        if transparentColor is not False:
            image.set_colorkey(colors.lookupColor(transparentColor))
    if flipHorizontal or flipVertical:
        image = pygame.transform.flip(image, flipHorizontal, flipVertical)
    if rotate != 0 or scale != 1:
        image = pygame.transform.rotozoom(image, rotate, scale)
    return image


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
