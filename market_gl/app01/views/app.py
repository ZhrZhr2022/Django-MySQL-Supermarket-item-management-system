import cv2
import numpy as np
import os
from app01 import models
from django.shortcuts import render, redirect

from app01.views.login1 import LoginForm


def load_data():
    listdir = os.listdir(r'C:/Users/Administrator/Desktop/market_gl/app01/views/faces')
    names = [d for d in listdir if not d.startswith('.')]
    faces = []
    target = [i for i in range(len(names))] * 30
    target.sort()
    for dir1 in names:
        for i in range(1, 31):
            gray = cv2.imread(r'C:/Users/Administrator/Desktop/market_gl/app01/views/faces/%s/%d.jpg' % (dir1, i))
            gray_ = gray[:, :, 0]
            gray_ = cv2.equalizeHist(gray_)  # 图片均衡化处理
            faces.append(gray_)
    faces = np.asarray(faces)
    target = np.asarray(target)
    return faces, target, names


def dynamic_recognizer_face(face_recognizer1, names1):
    name = 'names1'
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    face_detector = cv2.CascadeClassifier(r'C:\Users\Administrator\Desktop\market_gl\app01\views\haarcascade\haarcascade_frontalface_alt.xml')
    while True:
        flag, frame = cap.read()
        if not flag:
            break
        gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
        faces1 = face_detector.detectMultiScale(gray, minNeighbors=10)
        for x, y, w, h in faces1:
            face = gray[y:y + h, x:x + w]
            face = cv2.resize(face, dsize=(64, 64))
            face = cv2.equalizeHist(face)
            y_, confidence = face_recognizer1.predict(face)
            label = names1[y_]
            name = label
            cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255], thickness=2)
            cv2.putText(frame, text=label, org=(x, y - 10),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1.5, color=[0, 0, 255], thickness=1)
        cv2.imshow('face', frame)
        key = cv2.waitKey(1000 // 24)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()
    return name


def jiazai(request):
    # 加载数据
    faces, target, names = load_data()
    # 加载算法
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 算法训练
    face_recognizer.train(faces, target)
    # 动态加载数据
    name = dynamic_recognizer_face(face_recognizer, names)

    admin_object = models.Account.objects.filter(username=name).first()
    if admin_object:
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username, 'ident': admin_object.identity}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/account/list/")
    return redirect("/login/")
