import sdl2, sdl2.sdlimage, colors, sdl2.sdlgfx

_disp = None


# TODO: make sure everything gets freed properly, in general
class Image:
    def __init__(self, surface):
        self.surface = surface
        self.renderer = None
        self.texture = None

    def get_texture(self, renderer):
        # TODO: optimize this for the case of multiple renderers
        if renderer != self.renderer:
            assert renderer is not None
            if self.texture is not None:
                sdl2.SDL_DestroyTexture(self.texture)
                self.texture = None
            self.texture = sdl2.SDL_CreateTextureFromSurface(renderer, self.surface)
            assert self.texture is not None, "Could not prepare image for rendering: %s" % sdl2.SDL_GetError()
        else:
            assert self.texture is not None
        return self.texture

    def free(self):
        # TODO: make sure this happens
        sdl2.SDL_DestroyTexture(self.texture)
        self.texture = None
        self.renderer = None
        sdl2.SDL_FreeSurface(self.surface)
        self.surface = None

    def get_size(self):
        return self.surface.w, self.surface.h


def loadImage(filename, transparentColor=None, rotate=0, scale=1, flipHorizontal=False, flipVertical=False):
    freeable_images = []
    image_out = None
    try:
        image_base = sdl2.sdlimage.IMG_Load(filename)
        if image_base is None:
            raise IOError("Could not load image: %s" % sdl2.sdlimage.IMG_GetError())
        freeable_images.append(image_base)

        pf = _disp.getPixelFormat()
        # TODO: do something differently if transparentColor is None versus False?
        image = sdl2.SDL_ConvertSurface(image_base, pf, 0)
        assert image is not None, "Could not convert image: %s" % sdl2.SDL_GetError()
        freeable_images.append(image)

        if transparentColor is not None and transparentColor is not False:
            r, g, b = colors.lookupColor(transparentColor)
            pix = sdl2.SDL_MapRGB(r, g, b)
            assert sdl2.SDL_SetColorKey(image, True, pix) == 0, "Could not set color key: %s" % sdl2.SDL_GetError()

        if rotate != 0 or scale != 1 or flipHorizontal or flipVertical:
            hscale = -scale if flipHorizontal else scale
            vscale = -scale if flipVertical else scale
            image = sdl2.sdlgfx.rotozoomSurfaceXY(image, rotate, hscale, vscale, sdl2.sdlgfx.SMOOTHING_ON)
            assert image is not None, "Could not transform image: %s" % sdl2.SDL_GetError()
            freeable_images.append(image)
        image_out = image
    finally:
        for freeable in freeable_images:
            if freeable is not image_out and freeable is not None:
                sdl2.SDL_FreeSurface(freeable)
    return Image(image_out)


def getImageWidth(image):
    return image.get_size()[0]


def getImageHeight(image):
    return image.get_size()[1]


def getImagePixel(image, x, y):
    assert type(image) == Image
    surf = image.surface
    assert sdl2.SDL_LockSurface(surf) == 0, "Could not lock surface: %s" % sdl2.SDL_GetError()
    try:
        surf.format.BitsPerPixel
    finally:
        sdl2.SDL_UnlockSurface(surf)
    image.surface.
    return image.get_at((int(x), int(y)))


def getImageRegion(image, x, y, width, height):
    return image.subsurface(pygame.Rect(int(x), int(y), int(width), int(height)))


def saveImage(image, filename):
    assert type(image) == Image
    # Always saves images in BMP or PNG, unlike pygame.
    if filename.lower().endswith(".bmp"):
        assert sdl2.SDL_SaveBMP(image.surface, filename) == 0, "Could not save image: %s" % sdl2.SDL_GetError()
    elif filename.lower().endswith(".png"):
        assert sdl2.sdlimage.IMG_SavePNG(image.surface, filename) == 0, "Could not save image: %s" % sdl2.SDL_GetError()
    else:
        raise IOError("Can only save images in BMP or PNG format.")


def setDisplay(display):
    global _disp
    _disp = display


def wrapSurface(surface):
    return Image(surface)
