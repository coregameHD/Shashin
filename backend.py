from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImagePalette, ImageFilter, ImageChops
# Importing Image
image = Image.open("test_2.png").convert('RGBA')
print(image.format, image.size, image.mode)

# Font handling
font = ImageFont.truetype('fonts/halfpixfont.ttf', 42)

# Constrast
def imgContrast(inpImg = image, amount = 0.5):
    flt = ImageEnhance.Contrast(inpImg)
    out = flt.enhance(amount)
    return out

# Greyscale
def imgGreyscale(inpImg = image):
    imageGrey = inpImg.convert('L')
    out = imageGrey.convert('RGBA')
    return out

# Palette
def imgPalette(inpImg = image):
    imagePal = inpImg.convert('P', palette=Image.ADAPTIVE, colors=32)
    out = imagePal.convert('RGBA')
    return out

# Beauty
def imgBeauty(inpImg = image):
    fltBeauBlur = ImageFilter.GaussianBlur(3)
    imageBeauBlur = inpImg.filter(fltBeauBlur)
    imageBeauLight = ImageChops.lighter(inpImg, imageBeauBlur)
    fltBeauSharp = ImageEnhance.Sharpness(inpImg)
    imageBeauSharp = fltBeauSharp.enhance(2.0)
    imageBeauBlend = ImageChops.blend(imageBeauSharp, imageBeauLight, 0.7)
    out = imgContrast(imageBeauBlend, 1.2)
    return out

# Frame
def imgFrame(inpImg = image):
    imageFrame = Image.open("frames/frame_50.png").convert('RGBA')
    out = Image.alpha_composite(inpImg, imageFrame)
    return out.show()

# Colour Filter
def imgColourFilter(colour, inpImg = image, amount = 0.5):
    imageFilter = Image.new('RGBA', inpImg.size, colour)
    imageFilterChop = ImageChops.blend(inpImg, imageFilter, 1)
    out = ImageChops.blend(inpImg, imageFilterChop, amount)
    return out.show()

# Tint
def imgTint(colour, inpImg = image, amount = 0.5):
    imageGS = imgGreyscale(inpImg)
    imageFilter = Image.new('RGBA', inpImg.size, colour)
    imageFilterChop = ImageChops.blend(imageGS, imageFilter, 1)
    out = ImageChops.blend(imageGS, imageFilterChop, amount)
    return out.show()

# Image Filter
def imgImgFilter(inpImg = image, amount = 0.5):
    imageFilter = Image.open("filters/filter_ussr.png").convert('RGBA')
    imageFilterChop = ImageChops.blend(inpImg, imageFilter, 1)
    out = ImageChops.blend(inpImg, imageFilterChop, amount)
    return out.show()

# Text
def imgText(inpString, inpImg = image):
    text = Image.new('RGBA', image.size, (255, 255, 255, 0))
    textDraw = ImageDraw.Draw(text)
    textDraw.text((50, 5), inpString, font=font, fill=(255, 0, 0, 255))
    out = Image.alpha_composite(inpImg, text)
    return out
