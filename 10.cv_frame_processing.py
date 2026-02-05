import cv2

##capturing video
cam = cv2.VideoCapture(0) ## 0 - accessing my own laptop camera

##accessing height and width size of capturing videos
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))

##compression format
# Define codec and create VideoWriter object
codec_format = cv2.VideoWriter.fourcc(*'XVID')  # XVID codec
##output format we get after recording video
output_video = cv2.VideoWriter('Output_video.avi', 
                         codec_format, 
                         fps=30, 
                         frameSize=(frame_width,frame_height))
print("Recording Starting.........\nTo Quit press 'q'.")

while True:
    ret, img_frame = cam.read()

    if not ret:
        print("Error: Failed to read the image frame.")
        break

    ##saving each frame as in the form of video
    output_video.write(image=img_frame)
    cv2.imshow("Recording videos",img_frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cam.release()
output_video.release()
cv2.destroyAllWindows()

