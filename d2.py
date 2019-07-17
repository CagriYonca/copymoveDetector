from PIL import Image
from matplotlib.pyplot import imshow
from scipy.fftpack import dct, idct
import numpy as np

# resizing image
def resize(image="a.png", basewidth = 512):
    image = Image.open(image)
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)

    return image

def slide(image, window_size = 16):
    image = np.array(image)
    sizeX, sizeY, _ = image.shape
    matrixA = np.zeros_like((sizeX, sizeY))
    outputMatrix = np.zeros_like((sizeX, sizeY))

    for i in range(sizeX - window_size + 1):
        for j in range(sizeY - window_size + 1):
            part = image[i : i + window_size, j : j + window_size]
            print(part)
            print(dct(part), 1)
            #matrixA[i, j] = dct(part, 1)
            if np.isin(matrixA[i, j], matrixA[:i - 1, :j - 1]):
                outputMatrix[i, j] = 255
            else:
                outputMatrix[i, j] = 0

    return outputMatrix

elma = resize()
elma = slide(elma)

elma.show()
"""
x = np.array(image.getdata(), dtype=np.uint8)
bloklar = np.empty([x.shape[0] // window_size, x.shape[1] // window_size])
print(x.shape, bloklar.shape)
# divide image to sub blocks
for i in range(0, x.shape[0] - window_size + 1, window_size):
    for j in range(0, x.shape[1] - window_size + 1, window_size):
        bloklar[i, j] = x[i : i + window_size, j : j + window_size]
print(bloklar.shape)
"""