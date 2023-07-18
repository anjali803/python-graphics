from PIL import Image   #(PIL)Python Imaging Library
import matplotlib.pyplot as plt

# Load the image
image_path = 'path_to_your_image.jpg'  # Replace with the actual path to your image file
image = Image.open('img.png')
(r,g,b)= Image.getPixel(0,0,0)
# Display the image
plt.imshow(image)
plt.axis('off')
plt.show()


