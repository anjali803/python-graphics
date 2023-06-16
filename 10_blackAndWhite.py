from functools import reduce

# Example: Computing the sum of a list of numbers using reduce()
numbers = [1, 2, 3, 4, 5]
def p(val):
    print(val)
sum_result = reduce(p, numbers)
print(sum_result) 



# from PIL import Image

# # Load the image
# image_path = 'path_to_your_image.jpg'  # Replace with the actual path to your image file
# image = Image.open('img.png')

# # Convert the image to grayscale
# gray_image = image.convert('L')

# # Save the grayscale image
# gray_image.save('path_to_save_grayscale_image.jpg')  # Replace with the path to save the grayscale image
