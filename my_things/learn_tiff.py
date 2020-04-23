
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
    
file1 = '../MCF10A/1.tif' # dimensions of this tif file are (3, 2048, 2048), class is numpy.uint16


file1_matrix = tiff.imread(file1)
img = scipy.misc.toimage(file1_matrix)
#plt.imshow(img)
#plt.show()
pages, width, height = file1_matrix.shape

# 1st through 3rd pages of the tiff file
file1_matrix_0 = tiff.imread(file1, key=0)
file1_matrix_1 = tiff.imread(file1, key=1)
file1_matrix_2 = tiff.imread(file1, key=2)

# I remember Prof. Hariharan told me tiff file format is AxBx(number of pages), so the number of pages is at the back rather than the front, when you use imread. I have to write it back shifted to fit the tifffile format
shifted_matrix = np.random.randint(0,2**16, (width,height,pages), type(file1_matrix[0,0,0]))
shifted_matrix[:,:,0] = file1_matrix_0
shifted_matrix[:,:,1] = file1_matrix_1
shifted_matrix[:,:,2] = file1_matrix_2
print(shifted_matrix)
print(shifted_matrix.shape)
tiff.imwrite('file1_blue.tif', file1_matrix_0, photometric='rgb')
plt.imshow(file1_matrix_0)
plt.show()
plt.imshow(file1_matrix_1)
plt.show()
plt.imshow(file1_matrix_2)
plt.show()
