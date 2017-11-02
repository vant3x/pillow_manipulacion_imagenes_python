from PIL import Image

try: 
    img = Image.open("img/5.jpg")
    box = (100, 300, 1000, 1500)
    img = img.crop(box)
    img.show()
except IOError:
    print("No es posible abrir la imagen!")


    # """
    # - - - - - - -
    # - - - - - - -
    # - - - - - - -
    # - - - - - - -
    # - - - - - - -
    # - - - - - - -
