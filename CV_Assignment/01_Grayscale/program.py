import cv2

img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("Original image shape:", img.shape)
print("Grayscale image shape:", gray.shape)
print("Height:", gray.shape[0])
print("Width:", gray.shape[1])

cv2.imwrite("output.png", gray)
