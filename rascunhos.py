import cv2
import numpy as np
from matplotlib.pyplot import plot


image = cv2.imread("eu.jpg", cv2.IMREAD_REDUCED_COLOR_2)
image_copy = image.copy()

cv2.imshow("imagem",image)
cv2.waitKey(0)
serpia = [
    [0.272,0.534,0.131],
    [0.346,0.686,0.168],
    [0.393,0.769,0.189]
]
kernel = np.array(serpia)
img = cv2.filter2D(image_copy, -1,kernel)
cv2.imshow("imagem",img)
blur_image = cv2.GaussianBlur(image, (27, 27), 0)
cv2.imshow("imagem", blur_image)
cv2.waitKey(0)

"""
    Modo desenho
"""
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inv_gray_img = 255 - gray_image
#cv2.imshow("imagem", inv_gray_img)
blur_image = cv2.GaussianBlur(inv_gray_img, (21, 21), 0, 0)
sketch_image = cv2.divide(gray_image, 255 - blur_image, scale=256)

cv2.imshow("imagem", sketch_image)

cv2.waitKey(0)

"""

        CANNY

"""
image = cv2.imread("5.jpg", cv2.IMREAD_REDUCED_COLOR_2)
blur = cv2.GaussianBlur(image,(9,9),0)
canny_image = cv2.Canny(blur_image,10,11)
cv2.imshow("imagem", canny_image)

cv2.waitKey(0)
