import cv2
import numpy as np

img = cv2.imread("input.jpg")
brightness_value = 60

bright = np.clip(img.astype(np.int16) + brightness_value, 0, 255).astype(np.uint8)

y, x = 100, 100
print("Pixel before enhancement:", img[y, x])
print("Pixel after enhancement:", bright[y, x])

cv2.imwrite("output.png", bright)
