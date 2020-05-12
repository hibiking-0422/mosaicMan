import cv2
from mosaic import mosaic as mosaic

def faceMosaic(img):
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    img = cv2.imread(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_list = cascade.detectMultiScale(img_gray, minSize=(150, 150))
    if len(face_list) == 0:
        print("失敗")
        quit()

    for (x, y, w, h) in face_list:
        img = mosaic(img, (x, y, x+w, y+h), 10)
    cv2.imwrite("face-detect.png", img)
