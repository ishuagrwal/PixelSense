import cv2
import numpy as np

img = cv2.imread("input.jpg")

noisy = img.copy()
h, w, c = noisy.shape
num_pixels = int(0.02 * h * w)

for _ in range(num_pixels):
    y = np.random.randint(0, h)
    x = np.random.randint(0, w)
    noisy[y, x] = 255

for _ in range(num_pixels):
    y = np.random.randint(0, h)
    x = np.random.randint(0, w)
    noisy[y, x] = 0

cv2.imwrite("input.jpg", noisy)

result = cv2.medianBlur(noisy, 5)
cv2.imwrite("output.png", result)
