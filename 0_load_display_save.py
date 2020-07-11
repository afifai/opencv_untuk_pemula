import cv2

filepath = 'data\\logo_ngodingpython.png'
image = cv2.imread(filepath)
# display gambar
cv2.imshow("Gambar Saya", image)
cv2.waitKey(0)
# simpan gambar
output = 'data\\coba_simpan.png'
cv2.imwrite(output, image)
print("[INFO] Gambar telah tersimpan di {}".format(output))
