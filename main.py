#!flask/bin/python
# -- coding: utf-8 --
from flask import Flask, request
import json

from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')

    if username == 'admin' and password == '123456':
        data = {
            'status': 200,
            'message': '登录成功！！！'
        }
        return jsonify(data)
    data = {
            'status': 200,
            'message': '用户名或密码错误！！！'
    }
    res = jsonify(data)
    res.status_code = 500
    return res



@app.route('/api/goods', methods=['GET'])
def goods():
    data = [
        {
            'id': '001',
            'name': 'iphone 13',
            'icon': 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwx2.sinaimg.cn%2Fmw690%2F005JnC28gy1gv29r6vixbj60u90sugmn02.jpg&refer=http%3A%2F%2Fwx2.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1636543502&t=d76bee196a40aaaa1ccad2f1776f0c14',
            'price': 7999
        },
        {
            'id': '002',
            'name': 'iphone 12',
            'icon': 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimgservice.suning.cn%2Fuimg1%2Fb2c%2Fimage%2FgX79QCob9Xsc-m1QKulpKw.png_800w_800h_4e&refer=http%3A%2F%2Fimgservice.suning.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1636543266&t=2cd7386edcb25f99dece44a34e0a08d3',
            'price': 5999
        },
        {
            'id': '003',
            'name': 'iphone 11',
            'icon': 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimage.suning.cn%2Fuimg%2FZR%2Fshare_order%2F161601868603214243.jpg&refer=http%3A%2F%2Fimage.suning.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1636543591&t=2dd249867f03452826633dbd7f06b439',
            'price': 3999
        },
    ]

    return jsonify(data)
    # return json.dumps(data)

@app.route('/api/movies', methods=['GET'])
def movies():
    data = [
        {
            "id": 1,
            "name": "哥斯拉大战刚",
            "revenue": "275000000",
            "vote_average": "7.3",
            "vote_count": 1976
        },
        {
            "id": 2,
            "name": "鬼灭之刃之无限列车",
            "revenue": "190000000",
            "vote_average": "8.7",
            "vote_count": 2365
        },
        {
            "id": 3,
            "name": "尚气与十环传奇",
            "revenue": "320000000",
            "vote_average": "7.5",
            "vote_count": 3768
        },
        {
            "id": 4,
            "name": "真人快打",
            "revenue": "167060000",
            "vote_average": "6.3",
            "vote_count": 1122
        },
        {
            "id": 5,
            "name": "那些希望我死的人",
            "revenue": "131267370",
            "vote_average": "7.1",
            "vote_count": 364
        },
        {
            "id": 6,
            "name": "寂静之地 2",
            "revenue": "180500000",
            "vote_average": "7.4",
            "vote_count": 549
        },
        {
            "id": 7,
            "name": "活死人军团",
            "revenue": "97800000",
            "vote_average": "6.6",
            "vote_count": 1270
        },
        {
            "id": 8,
            "name": "人之怒",
            "revenue": "80437520",
            "vote_average": "7.7",
            "vote_count": 876
        },
        {
            "id": 9,
            "name": "小人物 Nobody",
            "revenue": "46088130",
            "vote_average": "8.5",
            "vote_count": 1796
        },
        {
            "id": 10,
            "name": "黑白魔女库伊拉",
            "revenue": "42600000",
            "vote_average": "8.8",
            "vote_count": 1574
        }
    ]

    return jsonify(data)
    # return json.dumps(data)


@app.route('/api/edit', methods=['POST'])
def edit():
    data1 = {
        'status': 200,
        'message': '修改成功！！！',
        'data': {
            'parameter': {
                'order_id': 'sn12345'
            }
        }
    }
    return jsonify(data1)

@app.route('/api/add', methods=['POST'])
def add():
    data1 = {
        'status': 200,
        'message': '添加成功！！！',
        'data': {
            'parameter': {
                'order_id': 'sn12345'
            }
        }
    }
    return jsonify(data1)

@app.route('/api/del', methods=['DELETE'])
def dele():
    data1 = {
        'status': 200,
        'message': '删除成功！！！',
        'data': {
            'parameter': {
                'order_id': 'sn12345'
            }
        }
    }
    return jsonify(data1)


@app.route('/api/quickbuy', methods=['POST'])
def quick_buy():
    data1 = {
        'status': 200,
        'message': '购买成功！！！',
        'data': {
            'parameter': {
                'order_id': 'sn12345'
            }
        }
    }
    return jsonify(data1)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
