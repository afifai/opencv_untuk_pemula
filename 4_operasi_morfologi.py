import cv2

image = cv2.imread('np_bin.jpg')
cv2.imshow("Original", image)

# erosion
# for i in range(0, 3):
#     eroded = cv2.erode(image.copy(), None, iterations = i + 1)
#     cv2.imshow(f"Erosi {i+1} kali", eroded)
#     cv2.waitKey(0)

# dilation
# for i in range(0, 3):
#     dilated = cv2.dilate(image.copy(), None, iterations = i + 1)
#     cv2.imshow(f"Dilasi {i+1} kali", dilated)
#     cv2.waitKey(0)

kernelSizes = [(3,3), (5,5), (7,7)]
# Opening
# for kernelSize in kernelSizes:
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
#     opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
#     cv2.imshow(f"Opening : ({kernelSize[0]}, {kernelSize[1]}", opening)
#     cv2.waitKey(0)

# Closing
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"Closing : ({kernelSize[0]}, {kernelSize[1]}", opening)
    cv2.waitKey(0)
