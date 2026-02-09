##libraries
import cv2

##image 
img = cv2.imread("tri.png")

if img is not None:
    ##convert into grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ##black and white
    _, thresh = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)

    ## find contours list
    contour, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    ##draw contours over the images
    thick = 4
    contour_idx = -1
    color = (0, 0, 255)
    cv2.drawContours(img, contour, contour_idx, color, thickness=thick)

    ##checking the contours
    for cont in contour:
        approx_shape = cv2.approxPolyDP(cont, 0.01*cv2.arcLength(cont,True), True)

        ##corners
        corners = len(approx_shape)

        if corners==3:
            shape_name = "Triangle"
        elif corners==4:
            shape_name="Rectangle"
        elif corners==5:
            shape_name="Pentagon"
        elif corners>5:
            shape_name="Circle"

        else:
            shape_name="Unknown"
        
        cv2.drawContours(img, [approx_shape], contour_idx, color, thickness=thick)
        ##for text point
        x=approx_shape.ravel()[0]
        y=approx_shape.ravel()[1]-10
        cv2.putText(img, 
                    shape_name,
                    (x,y), 
                    cv2.FONT_HERSHEY_COMPLEX,
                    fontScale=2,
                    color=color,
                    thickness=thick)
         
    ##display
    cv2.imshow("Contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()