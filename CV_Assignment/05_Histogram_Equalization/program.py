import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
equalized = cv2.equalizeHist(img)

cv2.imwrite("output.png", equalized)

hist_before = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_after = cv2.calcHist([equalized], [0], None, [256], [0, 256])

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Before Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist_before)

plt.subplot(1, 2, 2)
plt.title("After Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist_after)

plt.savefig("histogram_comparison.png", bbox_inches="tight")
plt.close()
