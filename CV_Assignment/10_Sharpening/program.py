import cv2
import numpy as np

img = cv2.imread("input.jpg")

kernel = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

sharpened = cv2.filter2D(img, -1, kernel)

cv2.imwrite("output.png", sharpened)
