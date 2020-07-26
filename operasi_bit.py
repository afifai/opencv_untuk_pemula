import numpy as np
import cv2

persegi = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(persegi, (25, 25), (275, 275), 255, -1)
cv2.imshow("Persegi", persegi)

lingkaran = np.zeros((300, 300), dtype="uint8")
cv2.circle(lingkaran, (150, 150), 150, 255, -1)
cv2.imshow("Lingkaran", lingkaran)
cv2.waitKey(0)

operasi_dan = cv2.bitwise_and(persegi, lingkaran)
cv2.imshow("Dan", operasi_dan)
cv2.waitKey(0)

operasi_atau = cv2.bitwise_or(persegi, lingkaran)
cv2.imshow("Atau", operasi_atau)
cv2.waitKey(0)

operasi_xor = cv2.bitwise_xor(persegi, lingkaran)
cv2.imshow("Xor", operasi_xor)
cv2.waitKey(0)

operasi_not = cv2.bitwise_not(lingkaran)
cv2.imshow("Not", operasi_not)
cv2.waitKey(0)


