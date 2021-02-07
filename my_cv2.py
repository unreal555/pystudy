import cv2
import time

try:
    cap = cv2.VideoCapture(0)
    print(cap)
    cap.open(0, cv2.CAP_DSHOW)  #摄像机太老，必须修改打开方式，猜测是directshow的意思
    # face_model = cv2.CascadeClassifier('./face_haarcascade/haarcascade_frontalface_alt.xml')
    face_model = cv2.CascadeClassifier('./face_haarcascade/haarcascade_frontalface_alt.xml')
    print(1)
except Exception as e:
    print(e)
    exit()
n=1
start=time.time()
state=0
while True:
    ret, frame = cap.read()
    print(ret)
    frame=cv2.flip(frame, 180)
    frame=cv2.putText(frame,str(n),(10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.8,(255,0,0), 1)
    # 图片进行灰度处理
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # 人脸检测
    faces = face_model.detectMultiScale(gray,minSize=(24, 24))
    # 标记人脸
    if len(faces)!=state:
        if len(faces)-state>0:
            print('+',len(faces))
        else:
            print('-',len(faces))
        state=len(faces)


    for (x, y, w, h) in faces:
        # 1.原始图片；2坐标点；3.矩形宽
        #高 4.颜色值(RGB)；5.线框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.circle(frame,(int((x+2*w)/2),int((y+h)/2)),int(h/2),(0,255,0),1)
        # cv2.ellipse(frame, (int((x+w/)/2),int((y+h)/2)), (int((h+y)/2),int((x+w)/2)), 0, 0, 360, (255, 255, 255), 3) # 画椭圆
    cv2.imshow('frame',frame)

    n=n+1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
del (face_model)
run_time=time.time()-start
print(run_time)
print(n/run_time)




