# coding=utf-8
from flask import Flask, jsonify, json, request
from flask_cors import CORS
from database import Account, Groups, Relations, db_session
import tool

app = Flask(__name__)
CORS(app)


# 登陆
@app.route('/login', methods=['POST'])
def login():
    model = request.get_json()
    if 'name' in model:
        username = model['name']
        password = model['password']
        if not username:
            return jsonify({'result': False, 'msg': '用户名为空'})
        if not password:
            return jsonify({'result': False, 'msg': '密码为空'})
        entity = Account.query.filter_by(name=username).first()
        if entity is None:
            return jsonify({'result': False, 'msg': '该用户名没有注册'})
        if entity.password == tool.Md5Encrypt(password):
            return jsonify({'result': True, 'data': entity.id})
        else:
            return jsonify({'result': False, 'msg': '密码错误'})
    return jsonify({'result': False, 'msg': '未通过数据验证'})


# 注册
@app.route('/reg', methods=['POST'])
def reg():
    model = request.get_json()
    if 'name' in model:
        username = model['name']
        password = model['password']
        if not username:
            return jsonify({'result': False, 'msg': '用户名为空'})
        if not password:
            return jsonify({'result': False, 'msg': '密码为空'})
        if Account.query.filter_by(name=username).count() > 0:
            return jsonify({'result': False, 'msg': '该用户名已注册'})
        entity = Account(name=username, password=tool.Md5Encrypt(password))
        db_session.add(entity)
        db_session.commit()
        return jsonify({'result': True})
    return jsonify({'result': False, 'msg': '未通过数据验证'})


# 添加好友
@app.route('/addFriend', methods=['POST'])
def addFriend():
    model = request.get_json()
    if 'friendId' in model:
        userId = model['userId']
        friendId = model['friendId']
        if not userId:
            return jsonify({'result': False, 'msg': '未登录'})
        if (not friendId) or (userId==friendId):
            return jsonify({'result': False, 'msg': '添加好友为空'})
        if Account.query.get(friendId) is None:
            return jsonify({'result': False, 'msg': '添加好友为空'})
        isExist = (Relations.query.filter_by(laccountid=userId, raccountid=friendId).count() > 0
                   or Relations.query.filter_by(laccountid=userId, raccountid=friendId).count() > 0)
        if isExist:
            return jsonify({'result': False, 'msg': '你们已经是好友了'})
        entity = Relations(laccountid=userId, raccountid=friendId)
        db_session.add(entity)
        db_session.commit()
        return jsonify({'result': True})

    return jsonify({'result': False, 'msg': '未通过数据验证'})


# 获取好友列表
@app.route('/getFriends', methods=['POST'])
def getFriends():
    model = request.get_json()
    if 'userId' in model:
        userId = model['userId']
        if not userId:
            return jsonify({'result': False, 'msg': '未登录'})
        lfriends = Relations.query.filter_by(laccountid=userId)
        rfriends = Relations.query.filter_by(raccountid=userId)
        data = []
        if lfriends.count() > 0:
            for l in lfriends:
                account = Account.query.get(l.raccountid)
                data.append({'user': account.id, 'name': account.name})
        if rfriends.count() > 0:
            for r in rfriends:
                account = Account.query.get(r.laccountid)
                data.append({'user': account.id, 'name': account.name})
        return jsonify({'result': True, 'data': data})
    return jsonify({'result': False, 'msg': '未通过数据验证'})


if __name__ == '__main__':
    app.run()
