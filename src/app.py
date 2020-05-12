from flask import Flask, request, jsonify, make_response

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

app = Flask(__name__)

@app.route("/hoge", methods=['GET'])
def getHoge():
    # URLパラメータ
    params = request.args
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
        faceMosaic("my_face.jpg")
    return make_response(jsonify(response))

@app.route("/hoge", methods=['POST'])
def postHoge():
    # ボディ(application/json)パラメータ
    params = request.json
    response = {}
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))
if __name__ == '__main__':
  app.run()