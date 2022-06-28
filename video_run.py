import cv2
from fer import FER
import numpy as np

emo_detector = FER(mtcnn=True)

face_cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)


camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))

def gen_frames():
    while True:
        #frameが読み込んだ画像
        #successにはうまくカメラが機能すればTrue、ダメだったらFalseが返ってくる
        success, frame = camera.read()
        if not success:
           break
        else:
            #フレームデータをjpgに圧縮
            #buffer（メモリバッファ）に保存
            #bufferはnumpyのndarray型
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #cv2.imshow("frame_orig",gray)
            faces = face_cascade.detectMultiScale(gray)
            for (x,y,w,h) in faces:
               cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),thickness=5)
               face = frame[y-10:y+h+10, x-10:x+w+10]
               happy_score = emo_detector.detect_emotions(face)[0]['emotions']['happy']
               

            

            #yield(buffer)
            # ndarrayをバイナリデータに直す
            ret, buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            #whileの処理ごとに戻り値を与えている
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
