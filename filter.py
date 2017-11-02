from PIL import Image
from PIL import ImageFilter


try:
    # img = Image.open("img/6.jpg")
    img = Image.open("img/3.jpg")
    # img = img.filter(ImageFilter.SMOOTH_MORE)
    # img = img.filter(ImageFilter.CONTOUR)
    # img = img.filter(ImageFilter.BLUR)
    # img = img.filter(ImageFilter.DETAIL)
    # img = img.filter(ImageFilter.EDGE_ENHANCE)
    # img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    # img = img.filter(ImageFilter.EMBOSS)
    img = img.filter(ImageFilter.FIND_EDGES)
    # img = img.filter(ImageFilter.SMOOTH)
    # img = img.filter(ImageFilter.SHARPEN)
    img.show()
except  IOError:
    print("No es posible abrir la imagen!")