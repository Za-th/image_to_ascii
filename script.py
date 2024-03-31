from PIL import Image
from math import ceil
def img_to_ascii(image, save_name):
    
    # open image
    img = Image.open(image)
    w,h = img.size
    format = img.format

    # resize so height is 512
    img.resize((int(w*(128/h)), 128)).save("resized.%s" % format, format)

    # open resized image and load image data
    img = Image.open("resized.%s" % format)
    w,h = img.size
    img = list(img.getdata())

    # ascii list
    # ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    # put ascii into grid based on greyscale value of pixel
    grid = []
    for y in range(h):
        grid.append([])
        for x in range(w):
            r,g,b = img[y*w + x]
            # human eye doesn't see colours equally
            grey_scale = 0.21*r + 0.72*g + 0.07*b
            char = ascii_chars[ceil((len(ascii_chars)-1) * grey_scale / 255)]
            grid[y].append(char)

    # save file
    art = open(save_name, "w")
    for row in grid:
        art.write("".join(row)+"\n")
    art.close
    
img_to_ascii("MonaLisa.jpg", "ML_ascii.txt")
img_to_ascii("cat.jpg", "cat_ascii.txt")