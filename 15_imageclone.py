from PIL import Image
image = Image.open("lena.gif")
image.show()
newimage= image.clone()

newimage.show()