import cv2
#load the pre-trained Haar cascade classifier
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#start video capture from default webcam(0)
cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("error: couldn't open camera")
    exit()
while True:
    #capture frame by frame
    ret, frame=cap.read()
    #ret is a boolean value, if frame is read correctly, ret will be True
    if not ret:
        print("error: failed to capture image.")
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detect faces in grayscale
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    #draw rects around faces
    for (x,y,w,h) in faces:
        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            (255,0,0),
            2
        )
    #display resulting frame    
    cv2.imshow("face detection-press q to Quit",frame)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
#relaease the capture and close any open windows 
cap.release()
cv2.destroyAllWindows()    
