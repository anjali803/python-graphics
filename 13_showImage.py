from PIL import Image
image = Image.open("img1.gif")
image.show()
width = image.width()
print("width")