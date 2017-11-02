from PIL import Image

try: 
    img = Image.open("img/3.jpg")
    print(img.size)
    # print(img.width)
    # print(img.height)
    # img = img.resize( (400, 800) )

    img = img.resize( (img.width/2, img.height/2) )
    img.show()
except IOError:
    print("No es posible abrir la imagen")