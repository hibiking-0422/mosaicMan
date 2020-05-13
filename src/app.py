from flask import Flask, request, jsonify, make_response
import cv2
from mosaic import mosaic as mosaic
from flask_cors import CORS

import numpy as np
import cv2
from datetime import datetime
import os
import string
import random
import base64

SAVE_DIR = "./images"

def canny(image):
    return cv2.Canny(image, 100, 200)

def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

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
    cv2.imwrite("face-detect2.png", img)

app = Flask(__name__)
CORS(app)

@app.route("/hoge", methods=['GET'])
def getHoge():
    # URLパラメータ
    params = request.args
    response = {'result': 'Success!!'}
    #if 'param' in params:
        #response.setdefault('res', 'param is : ' + params.get('param'))
        #faceMosaic("my_face.jpg")
    return make_response(jsonify(response))

@app.route("/hoge", methods=['POST'])
def postHoge():
    # ボディ(application/json)パラメータ
    print("success!")
    print(request.files['file'])
    stream = request.files['file'].stream
    img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # 変換
    #img = canny(img)

    # 保存
    dt_now = datetime.now().strftime("%Y_%m_%d%_H_%M_%S_") + random_str(5)
    save_path = os.path.join(SAVE_DIR, dt_now + ".png")
    cv2.imwrite(save_path, img)

    print("save", save_path)
    faceMosaic(save_path)

    #response = []
    #with open('face-detect2.png', "rb") as f:
                #img_base64 = base64.b64encode(f.read()).decode('utf-8')

    # レスポンスのjsonに箱詰め
    #response.append(img_base64)
    #@response = {'result': 'Success!!'}
    #if 'param' in params:
        #response.setdefault('res', 'param is : ' + params.get('param'))
    b64 = base64.encodestring(open('face-detect2.png', 'rb').read())
    response = b64
    return make_response(response)
if __name__ == '__main__':
  app.run()