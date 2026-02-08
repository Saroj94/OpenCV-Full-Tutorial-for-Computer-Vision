##libraries
import cv2

##image 
img = cv2.imread("tri.png")

if img is not None:
    ##convert into grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ##black and white
    _, thresh = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)

    ## find contours
    contour, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    ##draw contours over the images
    thick = 4
    contour_idx = -1
    color = (0, 0, 255)
    cv2.drawContours(img, contour, contour_idx, color, thickness=thick)

    ##display
    cv2.imshow("Contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

