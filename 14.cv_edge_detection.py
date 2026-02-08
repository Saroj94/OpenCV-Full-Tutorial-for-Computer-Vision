##libraries
import cv2

##load image
img = cv2.imread('Rhododendron.jpg', cv2.IMREAD_GRAYSCALE)

if img is not None:
    edges = cv2.Canny(img, threshold1=50, threshold2=150)

    ##display
    cv2.imshow("Original Image", img)
    cv2.imshow('edges image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

