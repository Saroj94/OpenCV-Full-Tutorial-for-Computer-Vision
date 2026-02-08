##libraries
import cv2

##load images
img = cv2.imread("Rhododendron.jpg", cv2.IMREAD_GRAYSCALE)

if img is not None:
    ret, thresh_edges = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

    ##display
    cv2.imshow("Original Image", img)
    cv2.imshow("Threshold Image", thresh_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
