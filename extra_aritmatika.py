import numpy as np
import cv2

a = np.uint8([100])
b = np.uint8([200])

# Aritmatika NumPy
add_np = a + b
sub_np = a - b

# Aritmatika OpenCV
add_cv = cv2.add(a,b)
sub_cv = cv2.subtract(a,b)

# Tampilkan Hasil
print(f'Hasil {a} + {b} NumPy: {add_np}, OpenCV: {add_cv}')
print(f'Hasil {a} - {b} NumPy: {sub_np}, OpenCV: {sub_cv}')
