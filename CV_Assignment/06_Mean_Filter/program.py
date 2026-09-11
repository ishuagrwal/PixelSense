import cv2

img = cv2.imread("input.jpg")

small_kernel_result = cv2.blur(img, (3, 3))
large_kernel_result = cv2.blur(img, (9, 9))

cv2.imwrite("output.png", large_kernel_result)
