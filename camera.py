import cv2
import numpy as np
from fer import FER

emo_detector = FER(mtcnn=True)

face_cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)
#カメラの読み込み
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))

#動画終了まで繰り返し
while(cap.isOpened()):
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("frame_orig",gray)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),thickness=5)
            face = frame[y-10:y+h+10, x-10:x+w+10]
            happy_score = emo_detector.detect_emotions(face)[0]['emotions']['happy']
             cv2.putText(frame,
                 text='sample text',
                 org=(x, y),
                 fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                 fontScale=1.0,
                 color=(0, 255, 0),
                 thickness=2,
                 lineType=cv2.LINE_4)
            cv2.imshow("frame_orig",gray)
            cv2.waitKey(10)

    cv2.imshow("Frame",frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    




