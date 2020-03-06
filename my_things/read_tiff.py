
from PIL import Image
import matplotlib.pyplot as plt
import tifffile as tiff

#im = tiff.imread('../demo_imgs/1.tif')

#im = plt.imread('../demo_imgs/1.tif')

for x in range(1, 11):
    if (x != 8): # there's problems with MCF10A/9.tif; "bugger is not large enough"
        im = Image.open('../MCF10A/' + str(x) + '.tif')
        print("MCF10A" + str(x))
        im.show()


for x in range(1, 11):
    im = Image.open('../MDA_231/' + str(x) + '.tif')
    im.show()
