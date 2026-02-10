##import libraries
import cv2
##https://github.com/opencv/opencv/tree/master/data/haarcascades

face_cascade=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")

##video web cam access
video = cv2.VideoCapture(0)

##run until users not press any key
while True:
    _, frame = video.read()

    ##convert the each frame into grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ##scan through frame/image and detect object basically a face
    """
    scaleFactor=1.1: zoom scale that is slow and finds face
    minNeighbors=5: wit h 5 ways it will try to detect and become sure in detecting faces
    """
    face = face_cascade.detectMultiScale(gray_frame, 
                                         scaleFactor=1.1,
                                         minNeighbors=5)
    
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

        ##region of interest
        roi_gray = gray_frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        """
        let say
        face = [
        (100, 150, 80, 80) face1
        (250, 120, 90, 90) face2
        ]
        x,y - top left corner
        x+w, y+h = bottom right corner


        x - how far from left
        y - how far from top
        w - width of face
        h - height of face 
        """
        eye=eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eye)>0:
           cv2.putText(frame,"Eye Detected",(x,y-30),
                       cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 3)

        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smile)>0:
           cv2.putText(frame,"Smilling",(x,y-10),
                       cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 3)


        cv2.imshow("Web cam video face detection", frame)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
cv2.release()
cv2.destroyAllWindows()