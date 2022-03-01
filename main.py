from flask import Flask, request
import base64
from PIL import Image
import requests
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/upload', methods=['POST'])
def upload():
    token = request.values.get('token')
    blob = request.values.get('blob')
    webptopng(blob)
    data = imageai(token)
    return jsonify(data)

def webptopng(blob): 
    with open('imageToSave.webp', 'wb') as fh: 
        # deleting "data:image/png;base64," 
        data = blob.split(',')[1] 
        fh.write(base64.b64decode(data))
        fh.close()
    
    img = Image.open('imageToSave.webp')
    img.load()
    img.save("tmp.png")

def imageai(token):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    # 二进制方式打开图片文件
    f = open('tmp.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
#     access_token = '24.b9bf4569d9e9e667a6af2c3e5499d486.2592000.1648196112.282335-25652959'
    request_url = request_url + "?access_token=" + token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    return response.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
