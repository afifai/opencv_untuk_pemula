import numpy as np
import cv2
import imutils

image = cv2.imread('data/foto.jpg')
cv2.imshow('Gambar Asli', image)

# TRANSLATION
X, Y = -150, 50
shifted = imutils.translate(image, X, Y)
# cv2.imshow("Shifted", shifted)
# cv2.waitKey(0)

# ROTATION
angle = 180
rotated = imutils.rotate(image , angle)
# cv2.imshow("Rotated", rotated)
# cv2.waitKey(0)

# RESIZE
# methods = [
#     ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
#     ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
#     ("cv2.INTER_AREA", cv2.INTER_AREA),
#     ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
#     ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

height , width = 150, 700
resize_cv = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
resize_im = imutils.resize(image, width=width)
# cv2.imshow("Resized", resize_im)
# cv2.waitKey(0)

# FLIP
flip_hor = cv2.flip(image, 1)
flip_ver = cv2.flip(image, 0)
flip_verhor = cv2.flip(image, -1)
# cv2.imshow("flip_hor", flip_hor)
# cv2.imshow("flip_ver", flip_ver)
# cv2.imshow("flip_verhor", flip_verhor)
# cv2.waitKey(0)

# CROPPING
kepala = image[48:225, 90:240]
badan = image[227:384, 80:376]
# cv2.imshow("Kepala", kepala)
# cv2.imshow("Badan", badan)
# cv2.waitKey(0)

# ARITMATIKA CITRA

M = np.ones(image.shape, dtype="uint8") * 50
added = cv2.add(image, M)
# cv2.imshow("Added", added)

subtracted = cv2.subtract(image, M)
# cv2.imshow("Subsctracted", subtracted)
# cv2.waitKey(0)

#MASKING
mask = np.zeros(image.shape[:2], dtype='uint8')
cv2.rectangle(mask, (90, 48), (240, 225), 225, -1)
# cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
# cv2.imshow("Mask Diimplementasikan", masked)
# cv2.waitKey(0)

# SPLIT CHANNEL
(B, G, R) = cv2.split(image)

cv2.imshow('R', R)
cv2.imshow('G', G)
cv2.imshow('B', B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros(image.shape[:2], dtype='uint8')
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)
