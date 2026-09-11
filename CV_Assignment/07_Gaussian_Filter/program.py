import cv2
import numpy as np

img = cv2.imread("input.jpg")
noise = np.random.normal(0, 20, img.shape).astype(np.int16)
noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

result = cv2.GaussianBlur(noisy_img, (7, 7), 0)

cv2.imwrite("output.png", result)
