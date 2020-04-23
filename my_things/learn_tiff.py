
from PIL import Image
import matplotlib.pyplot as plt
import tifffile as tiff
import numpy as np
import scipy.misc


'''
for x in range(1, 11):
    if (x != 8): # there's problems with MCF10A/9.tif; "bugger is not large enough"
        im = Image.open('../MCF10A/' + str(x) + '.tif')
        im.show()


for x in range(1, 11):
    im = Image.open('../MDA_231/' + str(x) + '.tif')
    im.show()
'''
    
file1 = '../demo_imgs/1.tif' # dimensions of this tif file are (3, 2048, 2048), class is numpy.uint16

file1_matrix = tiff.imread(file1)
pages, width, height = file1_matrix.shape

# 1st through 3rd pages of the tiff file
file1_matrix_0 = tiff.imread(file1, key=0)
file1_matrix_1 = tiff.imread(file1, key=1)
file1_matrix_2 = tiff.imread(file1, key=2)

# I remember Prof. Hariharan told me tiff file format is AxBx(number of pages) rather than (number of pages)xAxB
plt.imshow(file1_matrix_0) # red channel
plt.show()
plt.imshow(file1_matrix_1) # green channel
plt.show()
plt.imshow(file1_matrix_2) # blue channel
plt.show()
