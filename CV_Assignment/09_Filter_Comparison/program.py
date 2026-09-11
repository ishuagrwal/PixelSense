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

mean_result = cv2.blur(noisy, (5, 5))
gaussian_result = cv2.GaussianBlur(noisy, (5, 5), 0)
median_result = cv2.medianBlur(noisy, 5)

cv2.imwrite("output_mean.png", mean_result)
cv2.imwrite("output_gaussian.png", gaussian_result)
cv2.imwrite("output_median.png", median_result)
