import cv2
import numpy as np

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

min_val = np.min(img)
max_val = np.max(img)
print("Minimum intensity:", min_val)
print("Maximum intensity:", max_val)

stretched = (img.astype(np.float32) - min_val) * (255.0 / (max_val - min_val))
stretched = np.clip(stretched, 0, 255).astype(np.uint8)

cv2.imwrite("output.png", stretched)
