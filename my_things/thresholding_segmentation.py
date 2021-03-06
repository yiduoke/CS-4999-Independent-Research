from PIL import Image
import matplotlib.pyplot as plt
import tifffile as tiff
import numpy as np
import scipy.misc
import skimage.segmentation as seg
import skimage.filters as filters


# importing the file, converting it into numpy array, etc

# MCF10A directory of images, some aren't listed because they only have like one uncorrupted image
directory_list = ['../MCF10A/', '../MDA_231/', '../MDA_231_2/', '../rep1_PCNT_MCF10A/', '../rep1_PCNT_MDA231/', '../rep2_MCF10A/', '../rep2_MDA231/']
for directory in directory_list:
    for x in range(1, 11):
        try:
            file1 = directory + str(x) + '.tif'
            file1_matrix = tiff.imread(file1)
            pages, width, height = file1_matrix.shape
            # 1st through 3rd pages of the tiff file
            file1_matrix_0 = tiff.imread(file1, key=0)
            file1_matrix_1 = tiff.imread(file1, key=1)
            file1_matrix_2 = tiff.imread(file1, key=2)

            scipy.misc.imsave(directory + str(x) +'_red.png', file1_matrix_0)
            scipy.misc.imsave(directory + str(x) + '_green.png', file1_matrix_1)
            scipy.misc.imsave(directory + str(x) + '_blue.png', file1_matrix_2)
            
            ###### unsupervised segmentation ######

            # isodata thresholding
            isodata_threshold = filters.threshold_isodata(file1_matrix_2)
            binary = np.where(file1_matrix_2 > isodata_threshold, file1_matrix_2, 0)
            scipy.misc.imsave(directory + str(x) + '_isodata.png', binary)
            # really good

            # Li thresholding
            li_threshold = filters.threshold_li(file1_matrix_2)
            binary = np.where(file1_matrix_2 > li_threshold, file1_matrix_2, 0)
            scipy.misc.imsave(directory + str(x) + '_li.png', binary)
            # bad, but groups cells close to each other together

            # local thresholding (smaller block sizes rather than the whole image)
            local_threshold = filters.threshold_local(file1_matrix_2, 15, 'mean')
            binary = np.where(file1_matrix_2 > local_threshold, file1_matrix_2, 0)
            scipy.misc.imsave(directory + str(x) + '_local.png', binary)
            # that looked REALLY cool, but NOT what I want

            # mean thresholding
            mean_threshold = filters.threshold_mean(file1_matrix_2)
            binary = np.where(file1_matrix_2 > mean_threshold, file1_matrix_2, 0)
            scipy.misc.imsave(directory + str(x) + '_mean.png', binary)
            # not helpful, just looks like Li filter (but in a smaller hoop -- just look at the two images)

            # minimum thresholding
            minimum_threshold = filters.threshold_minimum(file1_matrix_2)
            binary = np.where(file1_matrix_2 > minimum_threshold, file1_matrix_2, 0)
            scipy.misc.imsave(directory + str(x) + '_minimum.png', binary)
            # really good, comparable to isodata

            # not gonna try multi otsu because it's not what I want

            # niblack thresholding
            niblack_image = filters.threshold_niblack(file1_matrix_2, window_size=15, k=0.1)
            scipy.misc.imsave(directory + str(x) + '_niblack.png', niblack_image)
            # not helpful; this just looks like a blurring filter

            # otsu thresholding
            otsu_threshold = filters.threshold_otsu(file1_matrix_2)
            binary = np.where(file1_matrix_2 > otsu_threshold, file1_matrix_2, 0)
            scipy.misc.imsave(directory + str(x) + '_otsu.png', binary)
            # just looks like minimum or isodata, pretty good

            # triangle thresholding
            triangle_threshold = filters.threshold_triangle(file1_matrix_2)
            binary = np.where(file1_matrix_2 > triangle_threshold, file1_matrix_2, 0)
            scipy.misc.imsave(directory + str(x) + '_triangle.png', binary)
            # not good, like Li

            # not going to try Yen because it assumes high intensity is forground, and we have the opposite
        except:
            print(directory + str(x) + '.tif either does not exist or is corrupted')

###### should be in the middle of code if we wanna use these two things (histogram of intensities and supervised thresholding segmentation)

# histogram for blue channel
#fig, ax = plt.subplots(1, 1)
#ax.hist(file1_matrix_2.ravel(), bins=32, range=[np.min(file1_matrix_2), np.max(file1_matrix_2)])
#ax.set_xlim(np.min(file1_matrix_2), np.max(file1_matrix_2));
#plt.show()

# tried supervised segmentation using 150 intensity as threshold; rigitidy doesn't work too well

#big_blue = file1_matrix_2 > 150
#plt.imshow(big_blue)
#plt.show()
#big_blue = np.where(file1_matrix_2 > 150, file1_matrix_2, 0)
#scipy.misc.imsave('file1_blue_supervised_threshold.png', big_blue)
