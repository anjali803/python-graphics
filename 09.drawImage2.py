from images import Image
image = Image(150,150)
blue= (0,0,255)
y=image.getHeight()//2
for x in range(image.getWidth()):
    image.setPixel(x,y-1,blue)
    image.setPixel(x,y,blue)
    image.setPixel(x,y+1,blue)
image.draw()

# from PIL import Image

# # Load the image
# image_path = 'path_to_your_image.jpg'  # Replace with the actual path to your image file
# image = Image.open('img.png')

# # Display the image
# image.show()

