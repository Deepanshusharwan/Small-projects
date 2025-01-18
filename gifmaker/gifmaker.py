import sys
from PIL import Image

images = [] #list in which all the images are stored

for arg in sys.argv[1:]:
    image = Image.open(arg) #opens all the location of files
    images.append(image) #adds images to the empty list called "images"

images[0].save("output.gif", save_all=True, append_images=images[1:], loop=0, duration= 300)