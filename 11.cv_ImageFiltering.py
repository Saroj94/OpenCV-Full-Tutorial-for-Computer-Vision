##Image enhancer using Image filtering technique of opencv
 ##gaussian blur : It is used to remove the noise and smoothen the image
##median blur
##sharpening
 
##GAUSSIAN BLUR
import cv2

img = cv2.imread("Temi-Tea Namchi.png")
if img is not None:
    blurred_img = cv2.GaussianBlur(img,(9,9), 3)
    cv2.imshow("Orginal image", img)
    cv2.imshow("Blurred Image",blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()