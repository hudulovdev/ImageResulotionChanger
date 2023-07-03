from PIL import Image

image = Image.open('input_image.jpg')

new_width = 800  # Replace with the desired width in pixels
new_height = 600  # Replace with the desired height in pixels

resized_image = image.resize((new_width, new_height))

resized_image.save('output_image.jpg')
