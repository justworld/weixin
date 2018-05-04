# coding=utf-8
import json
import tornado.ioloop
import tornado.web
from database import Account, Relations, db_session
import tool


class Base(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with,content-type')
        self.set_header('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

# 登陆
class Login(Base):
    def post(self):
        model = json.loads(self.request.body)
        if 'name' in model:
            username = model['name']
            password = model['password']
            if not username:
                self.finish({'result': False, 'msg': '用户名为空'})
            if not password:
                self.finish({'result': False, 'msg': '密码为空'})
            entity = Account.query.filter_by(name=username).first()
            if entity is None:
                self.finish({'result': False, 'msg': '该用户名没有注册'})
            if entity.password == tool.Md5Encrypt(password):
                self.finish({'result': True, 'data': entity.id})
            else:
                self.finish({'result': False, 'msg': '密码错误'})
        else:
            self.finish({'result': False, 'msg': '未通过数据验证'})


# 注册
class Reg(Base):
    def post(self):
        model = json.loads(self.request.body)
        if 'name' in model:
            username = model['name']
            password = model['password']
            if not username:
                self.finish({'result': False, 'msg': '用户名为空'})
            if not password:
                self.finish({'result': False, 'msg': '密码为空'})
            if Account.query.filter_by(name=username).count() > 0:
                self.finish({'result': False, 'msg': '该用户名已注册'})
            entity = Account(name=username, password=tool.Md5Encrypt(password))
            db_session.add(entity)
            db_session.commit()
            self.finish({'result': True})
        else:
            self.finish({'result': False, 'msg': '未通过数据验证'})


# 添加好友
class FriendAdd():
    def post(self):
        model = json.loads(self.request.body)
        if 'friendId' in model:
            userId = model['userId']
            friendId = model['friendId']
            if not userId:
                self.finish({'result': False, 'msg': '未登录'})
            if (not friendId) or (userId == friendId):
                self.finish({'result': False, 'msg': '添加好友为空'})
            if Account.query.get(friendId) is None:
                self.finish({'result': False, 'msg': '添加好友为空'})
            isExist = (Relations.query.filter_by(laccountid=userId, raccountid=friendId).count() > 0
                       or Relations.query.filter_by(laccountid=userId, raccountid=friendId).count() > 0)
            if isExist:
                self.finish({'result': False, 'msg': '你们已经是好友了'})
            entity = Relations(laccountid=userId, raccountid=friendId)
            db_session.add(entity)
            db_session.commit()
            self.finish({'result': True})
        else:
            self.finish({'result': False, 'msg': '未通过数据验证'})


# 获取好友列表
class Friends(Base):
    def post(self):
        model = json.loads(self.request.body)
        if 'userId' in model:
            userId = model['userId']
            if not userId:
                self.finish({'result': False, 'msg': '未登录'})
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
            self.finish({'result': True, 'data': data})
        else:
            self.finish({'result': False, 'msg': '未通过数据验证'})


def make_app():
    return tornado.web.Application([
        (r'/login', Login),
        (r'/reg', Reg),
        (r'/addFriend', FriendAdd),
        (r'/getFriends', Friends)
    ])


def run():
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    run()
