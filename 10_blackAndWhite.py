from PIL import Image

def blackAndWhite(image):
    blackpixel = (0, 0, 0)
    whitepixel = (255, 255, 255)
    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))
            avg = (r + g + b) // 3
            if avg < 128:
                image.putpixel((x, y), blackpixel)
            else:
                image.putpixel((x, y), whitepixel)

def main(filename="lena.gif"):
    image = Image.open(filename)
    image.show()
    blackAndWhite(image)
    image.show()
    image.save("lenabw.gif")

if __name__ == '__main__':
    main()
