import os 
from PIL import image

# Open the images
image1 = Image.open("images/images1/image1.jpg")
image2 = Image.open("images/images2/image1.jpg")

#Resize the images
image1 = image1.resize((500, 350))
image1_size = image1.size
image2_size = image2.size

# Create a new image
new_image = Image.new('RGB', (2*image1_size[0], image1_size[1]), (250, 250, 250))

# Paste the images
new_image.paste(image1, (0, 0))
new_image.paste(image2, (image1_size[0], 0))

# Save the image
new_image.save("images/merged/merged.jpg")

# Show the image
new_image.show()
