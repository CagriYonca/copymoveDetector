from PIL import Image, ImageOps
import numpy as np

def roll(image, horizontal, vertical):
    "Roll an image sideways"

    xsize, ysize = image.size

    horizontal = horizontal % xsize
    if horizontal == 0: 
        return image

    part1 = image.crop((0, 0, horizontal, ysize))
    part2 = image.crop((horizontal, 0, xsize, ysize))
    part1.load()
    part2.load()
    image.paste(part2, (0, 0, xsize - horizontal, ysize))
    image.paste(part1, (xsize - horizontal, 0, xsize, ysize))

    part1 = image.crop((0, 0, xsize, vertical))
    part2 = image.crop((0, vertical, xsize, ysize))
    part1.load()
    part2.load()
    image.paste(part2, (0, 0, xsize, ysize - vertical))
    image.paste(part1, (0, ysize - vertical, xsize, ysize))

    return image

im = Image.open("a.png").resize((400, 400), 0)
im = ImageOps.grayscale(im)

sum1 = 99999999
sizeX, sizeY = im.size
first = np.array(im)
for i in range(0, sizeX, 2):
    for j in range(0, sizeY, 2):
        rolled = np.array(roll(im, i, j))
        fark = np.sum(abs(first - rolled), dtype=np.int32)
        print(fark)
        if fark < sum1:
            similar = rolled
            fark = sum1

similar = Image.fromarray(similar)
similar.show()