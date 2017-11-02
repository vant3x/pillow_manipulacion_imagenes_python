from PIL import Image

try:
    im = Image.open("img/1.jpg")
    copy = im.resize( (500,500))

    im.paste( copy, (500, 500) )
    im.show()
except IOError:
    print("No es posible abrir la imagen")

