from PIL import Image
from PIL import ImageFilter

def Main():
    print("Main")
    filepath = input("Input path to file you want to become a black person>>")
    im = Image.open(filepath)
    r, g, b = im.split()
    ba = b.filter(ImageFilter.MaxFilter)
    brown_overlay = Image.new("RGB", ba.size, (139, 69, 19))

    image_rgb = ba.convert("RGB")

    brown_image = Image.blend(image_rgb, brown_overlay, alpha=0.1)

    brown_image_l = brown_image.convert("L")

    # Show or save the final image
    #brown_image_l.show()
    #b.show()
    imn = Image.merge("RGB", (g, brown_image_l, brown_image_l))
    imn.show()
    name = input("Type file name to save for example blackperson.png:")
    print(name)
    print(name.find(".png"))
    try:
        if name.find(".png") > 0 or name.find(".jpg") > 0 or name.find(".jpeg") > 0 or name.find(".svg") > 0 or name.find(".avif") > 0 or name.find(".webp") > 0:
            imn.save(name)
    except:
        print("something went wrong")


if __name__ == '__main__':
    print("start")
    Main()

    #E:\hz\ря2\Onegritel3000\main.py
    #"C:\Users\Asus\Downloads\smiley-man-wearing-white-shirt-medium-shot.jpg""C:\Users\Asus\Downloads\smiley-man-wearing-white-shirt-medium-shot.jpg"
