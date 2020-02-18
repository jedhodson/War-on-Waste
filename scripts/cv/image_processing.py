import cv2 as cv
import numpy as np

# Base path of images
base_path = "C:\Users\jedho\Documents\Code\War-on-Waste\images\multi-spectral\proc"

# Path of each raw image
b765_img = base_path+"\multispectral_B765.png"
c830_img = base_path+"\multispectral_C830.png"
d870_img = base_path+"\multispectral_D870.png"
e890_img = base_path+"\multispectral_E890.png"
f935_img = base_path+"\multispectral_F935.png"
g950_img = base_path+"\multispectral_G950.png"

# Open with openCV. Commented out shows how to crop an image
b = cv.imread(b765_img, cv.IMREAD_GRAYSCALE)#[50:720, 300:800]
c = cv.imread(c830_img, cv.IMREAD_GRAYSCALE)#[50:720, 300:800]
d = cv.imread(d870_img, cv.IMREAD_GRAYSCALE)#[50:720, 300:800]
e = cv.imread(e890_img, cv.IMREAD_GRAYSCALE)#[50:720, 300:800]
f = cv.imread(f935_img, cv.IMREAD_GRAYSCALE)#[50:720, 300:800]
g = cv.imread(g950_img, cv.IMREAD_GRAYSCALE)#[50:720, 300:800]

# pre-processing
kernel_size = 50
r = 2

#(r, g, b) = cv.split(img)

#nf = r + g + b
mergedImg = cv.merge([c, e, f])

mergedImg = cv.blur(mergedImg, (kernel_size, kernel_size))

normalizedImg = np.zeros((670, 500))
normalizedImg = cv.normalize(mergedImg,  normalizedImg, 0, 255, cv.NORM_MINMAX)

#cv.imshow("Normalized", normalizedImg)
cv.imshow("MS", mergedImg)
cv.waitKey(0)
cv.destroyAllWindows()

#cv.imwrite(base_path+"\multispectral_CEF.png", merged)