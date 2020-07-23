# import cv2
# # import numpy as np
#
# frameWidth = 640
# frameHeight = 480
#
# img = cv2.imread("resource/Profile.jpg")
# # img.set(3, 640)
# # img.set(4, 480)
#
# # kernel = np.ones((5, 5), np.uint8)
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# imgCanny = cv2.Canny(img, 150, 200)
# # imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# # imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
#
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# # imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# # cv2.imshow("Dialation Image", imgDialation)
# # cv2.imshow("Eroded Image", imgEroded)
# cv2.waitKey(0)


import cv2
import numpy as np


img = cv2.imread('resource/Profile.jpg', cv2.IMREAD_UNCHANGED)
scale_percent = 30  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, cv2.INTER_AREA)
imgCanny = cv2.Canny(resized, 150, 200)
kernel = np.ones((0, 0), np.uint8)

imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

cv2.imshow("Dialation Image", imgDialation)

cv2.imshow("Resized image", resized)
cv2.imshow("Canny Image", imgCanny)

cv2.waitKey(0)
cv2.destroyAllWindows()