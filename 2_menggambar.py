import cv2
import numpy as np

canvas = np.zeros((300,300, 3), dtype='uint8')

hijau = (0, 255, 0)
cv2.line(canvas, (0,0), (300,300), hijau)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

merah = (0, 0, 255)
cv2.line(canvas, (300,0), (0,300), merah ,3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

biru = (255, 0, 0)
cv2.rectangle(canvas, (10,10), (60, 60), biru)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50,200), (200, 225), merah, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (200, 50), (225,125), biru, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


canvas = np.zeros((300,300, 3), dtype='uint8')
centerX, centerY = canvas.shape[1] // 2, canvas.shape[0] // 2
putih = (255,255,255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, putih)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


canvas = np.zeros((300,300, 3), dtype='uint8')
for i in range(0, 25):
    r = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,)).tolist()

    cv2.circle(canvas, tuple(pt), r, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.imwrite('output.jpg', canvas)

cv2.rectangle(canvas, (91, 35), (242,228), (0,255,0), 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

