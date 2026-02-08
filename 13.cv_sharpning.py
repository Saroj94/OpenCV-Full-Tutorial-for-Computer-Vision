##sharper image
import cv2
import numpy as np

##image
img = cv2.imread("Temi-Tea Namchi.png")

sharp_filter = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

if img is not None:
    sharpenend_img = cv2.filter2D(img, ddepth= -1, kernel=sharp_filter)
    cv2.imshow("Original Image", img)
    cv2.imshow("Sharp image", sharpenend_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()