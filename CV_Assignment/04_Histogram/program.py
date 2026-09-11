import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
peak_intensity = int(np.argmax(hist))
print("Intensity value with highest frequency:", peak_intensity)

plt.figure()
plt.title("Intensity Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist)
plt.xlim([0, 256])
plt.savefig("output.png", bbox_inches="tight")
plt.close()
