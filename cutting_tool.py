import cv2

img = cv2.imread("20211124_center.tif")

img1 = img[0 : 1023, 0: 1535]
cv2.imwrite("20211124_center_cut.tif", img1)