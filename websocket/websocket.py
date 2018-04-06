# coding=utf-8

from websocket_server import WebsocketServer
import json
from database import create_session, Chats

'''
数据协议
{
    socket_uid:用户id
    socket_fid:好友id
    socket_gid:群聊id
    socket_isGroup:是否群聊
    socket_msg:数据
}
'''

clientIds = []  # client和userId对应数组


def find_to_client(client):
    for c in clientIds:
        if c['client'] == client:
            return c


def find_to_user(user):
    for u in clientIds:
        if u['user'] == user:
            return u


def new_client(client, server):
    pass


def client_left(client, server):
    handler = find_to_client(client)
    if handler in clientIds:
        clientIds.remove(handler)


def message_received(client, server, message):
    data = json.loads(message)
    print data
    handler = {'client': client, 'user': data['socket_uid']}
    print data
    if handler not in clientIds:
        clientIds.append(handler)
    receiver = find_to_user(data['socket_fid'])
    if receiver is None:  # 暂存至数据库
        pass
    else:
        receData = {  # 发送消息包
            'socket_uid': receiver['user'],
            'socket_fid': data['socket_uid'],
            'socket_gid': '',
            'socket_isGroup': data['socket_isGroup'],
            'socket_msg': message
        }
        server.send_message(client, json.dumps(receData))
    print data


def run():
    server = WebsocketServer(8012, "127.0.0.1")
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()


if __name__ == "__main__":
    # run()
    dbAccessor = create_session()
    list = dbAccessor.query(Chats)
    for i in list.all():
        print i.msg
