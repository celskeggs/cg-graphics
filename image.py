import sdl2, sdl2.sdlimage, colors

# TODO: make sure everything gets freed properly, in general
class Image:
    def get_texture(self):
        pass
    def get_surface(self):
        pass
    def get_size(self):
        pass


def loadImage(filename, transparentColor=None, rotate=0, scale=1, flipHorizontal=False, flipVertical=False):
    if transparentColor is None:
        image_base = sdl2.sdlimage.IMG_Load(filename)
        assert image is not None, "Could not load image: %s" % sdl2.sdlimage.IMG_GetError()
        image = sdl2.SDL_DisplayFormatAlpha(image)
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
    if isinstance(image, Image):
        image = image.get_surface()
    pygame.image.save(image, filename)
