##Median blur

import cv2

##image
img = cv2.imread("Temi-Tea Namchi.png")

if img is not None:
    median_blur = cv2.medianBlur(img, 5)
    cv2.imshow("Original Image", img)
    cv2.imshow("blurred image", median_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()