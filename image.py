from PIL import Image

try:
    img = Image.open("img/1.jpg")
    print(img.mode)
    print(img.getpixel( (100, 200) ) )
    # img.show()
    img = img.convert("L")
    img.save("img/news/pic1.jpg")
    img.show()


except IOError:
    print("No es posible abrir la imagen")

    #http://pillow.readthedocs.io/en/3.4.x/handbook/concepts.html#modes

# 1 (1-bit pixels, black and white, stored with one pixel per byte)
# L (8-bit pixels, black and white)
# P (8-bit pixels, mapped to any other mode using a color palette)
# RGB (3x8-bit pixels, true color)
# RGBA (4x8-bit pixels, true color with transparency mask)
# CMYK (4x8-bit pixels, color separation)
# YCbCr (3x8-bit pixels, color video format)
# Note that this refers to the JPEG, and not the ITU-R BT.2020, standard
# LAB (3x8-bit pixels, the L*a*b color space)
# HSV (3x8-bit pixels, Hue, Saturation, Value color space)
# I (32-bit signed integer pixels)
# F (32-bit floating point pixels)
