from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImagePalette, ImageFilter, ImageChops

# Importing Image
original = Image.open("input.png").convert('RGBA')
original = original.resize((800,600))

# Font handling
font = ImageFont.truetype('fonts/halfpixfont.ttf', 42)

# Initialisation
original.save("./temp.png")
image = Image.open("temp.png").convert('RGBA')
print("Program start")
print("Image Format = " + str(image.format))
print("Image Size = " + str(image.size))
print("Image Mode = " + str(image.mode))
print()

# Contrast
def imgContrast(amount = 0.5):
    image = Image.open("temp.png").convert('RGBA')
    flt = ImageEnhance.Contrast(image)
    out = flt.enhance(amount)
    out.save("./temp.png")
    return out

# Brightness
def imgBrightness(amount = 0.5):
    image = Image.open("temp.png").convert('RGBA')
    flt = ImageEnhance.Brightness(image)
    out = flt.enhance(amount)
    out.save("./temp.png")
    return out

# Greyscale
def imgGreyscale():
    image = Image.open("temp.png").convert('RGBA')
    imageGrey = image.convert('L')
    out = imageGrey.convert('RGBA')
    return out

# Palette
def imgPalette():
    image = Image.open("temp.png").convert('RGBA')
    imagePal = image.convert('P', palette=Image.ADAPTIVE, colors=32)
    out = imagePal.convert('RGBA')
    return out

# Beauty
def imgBeauty():
    image = Image.open("temp.png").convert('RGBA')
    fltBeauBlur = ImageFilter.GaussianBlur(3)
    imageBeauBlur = image.filter(fltBeauBlur)
    imageBeauLight = ImageChops.lighter(image, imageBeauBlur)
    fltBeauSharp = ImageEnhance.Sharpness(image)
    imageBeauSharp = fltBeauSharp.enhance(2.0)
    imageBeauBlend = ImageChops.blend(imageBeauSharp, imageBeauLight, 0.7)
    flt = ImageEnhance.Contrast(imageBeauBlend)
    out = flt.enhance(1.2)
    out.save("./temp.png")
    return out

# Frame
def imgFrame(filepath):
    image = Image.open("temp.png").convert('RGBA')
    imageFrame = Image.open(filepath).convert('RGBA')
    imageFrame = imageFrame.resize((800,600))
    out = Image.alpha_composite(image, imageFrame)
    out.save("./temp.png")
    return out

# Text
def imgSticker(filepath, position):
    image = Image.open("temp.png").convert('RGBA')
    sticker = Image.open(filepath).convert('RGBA')
    sticker = sticker.resize((160,160))
    image.paste(sticker,position,sticker)
    image.save("./temp.png")
    return image

# Colour Filter
def imgColourFilter(colour):
    image = Image.open("temp.png").convert('RGBA')
    imageFilter = Image.new('RGBA', image.size, colour)
    out = ImageChops.screen(image, imageFilter)
    out.save("./temp.png")
    return out

# Tint
def imgTint(colour):
    image = Image.open("temp.png").convert('RGBA')
    imageGS = imgGreyscale()
    imageFilter = Image.new('RGBA', image.size, colour)
    out = ImageChops.screen(imageGS, imageFilter)
    out.save("./temp.png")
    return out

# Image Filter
def imgImgFilter(amount = 0.5):
    image = Image.open("temp.png").convert('RGBA')
    imageFilter = Image.open("filters/filter_ussr.png").convert('RGBA')
    imageFilterChop = ImageChops.blend(image, imageFilter, 1)
    out = ImageChops.blend(image, imageFilterChop, amount)
    return out

# Text
def imgText(inpString):
    image = Image.open("temp.png").convert('RGBA')
    text = Image.new('RGBA', image.size, (255, 255, 255, 0))
    textDraw = ImageDraw.Draw(text)
    textDraw.text((50, 5), inpString, font=font, fill=(255, 0, 0, 255))
    out = Image.alpha_composite(image, text)
    return out
