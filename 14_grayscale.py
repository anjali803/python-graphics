from PIL import Image

def greyscale(image):
    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.putpixel((x, y), (lum, lum, lum))

def main(filename="lena.gif"):
    image = Image.open(filename)
    image.show()
    greyscale(image)
    image.show()
    image.save("lenagreyscale.gif")

if __name__ == '__main__':
    main()

