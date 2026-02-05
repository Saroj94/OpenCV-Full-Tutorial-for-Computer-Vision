##importing libraries
import cv2

##capture video
cap_video = cv2.VideoCapture(0) ## 0 means taking picture from my own laptop, 1 is webcam

##run this video until users don't press any cancel key
while True:
    ##returns bolean result, frame of the video
    ret, frame = cap_video.read() ##ret: True/False, frame: Images

    if not ret:
        print("Could not read frames.")
        break

    cv2.imshow("Webcam video", frame)

    if cv2.waitKey(1) & 0xFF==ord("q"): ##key(1) is checking "q" keyword in every 1 millisecond 
        print("Quitting frame")
        break
cap_video.release()
cv2.destroyAllWindows()
