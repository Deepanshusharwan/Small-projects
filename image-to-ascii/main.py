import sys
from PIL import Image

def convert_to_ascii(image, downscale, output_name):
    type = image.split(".")[-1] #image extension
    image_name = image.removesuffix(f".{type}") 

    downscale = int(downscale)
    img = Image.open(image)
    w,h = img.size

    #resize big images
    img.resize((h//downscale,w//downscale)).save(f"{image_name}_downscale.{type}")
    ascii_grid = []
    ascii_chars = "@%#*+=-:. "

    w,h = img.size
    pix = img.load()

    for y in range(h):
        row = ""
        for x in range(w):
            r, g, b = pix[x, y]
            brightness = (r + g + b) / 3
            index = int((brightness / 255) * (len(ascii_chars) - 1))
            row += ascii_chars[index]
        ascii_grid.append(row)
                
    with open(output_name,'w') as o:
        o.write("\n".join(ascii_grid))

if __name__ == "__main__":

    if len(sys.argv) == 1:
        image = input("The image you want to input (path): ")
        output_name = input("Save output as? (for default) ")
        downscale = input("if you want to downscale (leave blank otherwise) ")

        if output_name.strip() == "":
            output_name = "ascii_image.txt"
        if downscale.strip() == "":
            downscale = 1
        print(output_name,downscale)

    elif len(sys.argv) == 2:
        image = sys.argv[1]
        output_name = "ascii_image.txt"
        downscale = 1

    elif len(sys.argv) == 3:
        image = sys.argv[1]
        output_name == sys.argv[2]
        downscale = 1

    elif len(sys.argv) == 4:
        image = sys.argv[1]
        output_name == sys.argv[2]
        downscale = sys.argv[3]

    convert_to_ascii(image,downscale,output_name)
    print(f"saved the file in {output_name}")
