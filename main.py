from PIL import Image

def Main():
    print("Main")
    im = Image.open("kirillnegrovich.jpg")
    r, g, b = im.split()
    imn = Image.merge("RGB", (g, b, b))
    imn.show()


if __name__ == '__main__':
    print("start")
    Main()