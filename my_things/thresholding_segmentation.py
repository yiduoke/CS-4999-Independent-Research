from PIL import Image
import matplotlib.pyplot as plt
import tifffile as tiff
import numpy as np
import scipy.misc


# importing the file, converting it into numpy array, etc
file1 = '../demo_imgs/1.tif'
file1_matrix = tiff.imread(file1)
pages, width, height = file1_matrix.shape
# 1st through 3rd pages of the tiff file
file1_matrix_0 = tiff.imread(file1, key=0)
file1_matrix_1 = tiff.imread(file1, key=1)
file1_matrix_2 = tiff.imread(file1, key=2)

scipy.misc.imsave('file1_red.png', file1_matrix_0)
scipy.misc.imsave('file1_green.png', file1_matrix_1)
scipy.misc.imsave('file1_blue.png', file1_matrix_2)

# histogram for blue channel
fig, ax = plt.subplots(1, 1)
ax.hist(file1_matrix_2.ravel(), bins=32, range=[np.min(file1_matrix_2), np.max(file1_matrix_2)])
ax.set_xlim(np.min(file1_matrix_2), np.max(file1_matrix_2));
plt.show()

big_blue = file1_matrix_2 > 150
plt.imshow(big_blue)
plt.show()
big_blue = np.where(file1_matrix_2 > 150, file1_matrix_2, 0)
scipy.misc.imsave('file1_blue_supervised_threshold.png', big_blue)
