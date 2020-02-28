from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import exposure
from skimage.segmentation import random_walker

orig_img = img_as_float(io.imread("demo_imgs/png.png"))
img = orig_img[...,2]
#plt.xlim([0, 0.2]) # magnify the part that actually as things going on
plot = plt.hist(img.flat, bins=80, range=(0,1))
#plt.savefig("plot.png")


#sigma_est = np.mean(estimate_sigma(img, multichannel = True))
#
#patch_kw = dict(patch_size = 5,
#                patch_distance = 6,
#                multichannel = True)
#denoise_img = denoise_nl_means(img , h = 1.15 * sigma_est, fast_mode = False, **patch_kw)

#plt.xlim([0, 1]) #change the x axis back to normal range of [0,1]
eq_img = exposure.equalize_adapthist(img)
plt.imshow(eq_img)
plt.savefig("segmented.png")

markers = np.zeros(img.shape, dtype = np.uint)
markers[eq_img < 0.510] = 1
markers[eq_img >= 0.510] = 2
plt.imshow(markers)
plt.savefig("walk.png")

labels = random_walker(eq_img, markers, beta = 10, mode = 'bf')
plt.imshow(labels)
plt.savefig("random.png")

segm1 = (labels == 1)
segm2 = (labels == 2)

all_segments = np.zeros((eq_img.shape[0], eq_img.shape[1], 3))
all_segments[segm1] = (1,0,0) #segment 1 is red
all_segments[segm2] = (0,1,0) #segment 1 is green
plt.imshow(all_segments)
plt.savefig("all_segments.png")
