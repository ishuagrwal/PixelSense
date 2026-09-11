import cv2
import numpy as np

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
img_float = np.float32(img)

dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
radius = 40

mask = np.zeros((rows, cols, 2), np.uint8)
cv2.circle(mask, (ccol, crow), radius, (1, 1), -1)

filtered_shift = dft_shift * mask
filtered_ishift = np.fft.ifftshift(filtered_shift)
result = cv2.idft(filtered_ishift)
result = cv2.magnitude(result[:, :, 0], result[:, :, 1])
result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)

cv2.imwrite("output.png", result.astype(np.uint8))
