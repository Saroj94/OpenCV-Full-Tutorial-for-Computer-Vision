##libraries
import cv2
import numpy as np

"""
1. 2-images combine
2. cut out images
3. Flip/Remove
---------------

1-cv2.bitwise_and(img1,img2)
2-cv2.bitwise_or(img1,img2)
3-cv2.bitwise_not(img1)
"""

img1 = np.zeros((300, 300),dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

if img1 is not None and img2 is not None:
    cen_pnt = (150,150)
    cr_rad = 100
    colors = 255
    thick = -1
    cv2.circle(img1, center=cen_pnt,radius=cr_rad, color=colors, thickness=thick)

    ##rectangle
    pnt1 = (100,100)
    pnt2 = (250,250)

    cv2.rectangle(img2,pnt1,pnt2, color=colors, thickness=thick)

    ##bitwise operation
    bitwise_and = cv2.bitwise_and(img1, img2)
    bitwise_or = cv2.bitwise_or(img1, img2)
    bitwise_not = cv2.bitwise_not(img1)

    ##display
    cv2.imshow("Circle Image", img1)
    cv2.imshow("Rectangle Image", img2)
    cv2.imshow("AND", bitwise_and)
    cv2.imshow("OR",bitwise_or)
    cv2.imshow("NOT",bitwise_not)
    cv2.waitKey(0)
    cv2.destroyAllWindows()