import cv2

image = cv2.imread('data/foto.jpg')
(h, w) = image.shape[:2]

cv2.imshow('Gambar Asli', image)

# informasi piksel
(b, g, r) = image[0,0]
print("Piksel pada (0,0) - Red : {}, Green : {}, Blue : {}".format(r, g, b))

image[0, 0] = (255, 0, 0)
(b, g, r) = image[0,0]
print("Piksel pada (0,0) - Red : {}, Green : {}, Blue : {}".format(r, g, b))

(cX, cY) = (w//2, h//2)
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow('Top Left', tl)
cv2.imshow('Top Right', tr)
cv2.imshow('Bottom Left', bl)
cv2.imshow('Bottom Right', br)

image[0:cY, 0:cX] = (153, 222, 76)
cv2.imshow('Gambar Hasil Manipulasi', image)

cv2.waitKey(0)
