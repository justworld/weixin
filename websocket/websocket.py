# coding=utf-8

from websocket_server import WebsocketServer
import json
from database import Chats, Relations, insert_chat, create_session

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

    if data['socket_isGroup']:
        #群聊不保存至数据库
        '''chat = Chats(sendid=data['socket_uid'], recid=data['socket_fid'],
                     msg=data['socket_msg'], isread=False, isgroup=True)
        insert_chat(chat)'''
        sendClients = []
        accessor = create_session()
        groupAccounts = accessor.query(Relations).filter(laccountid=data['socket_fid']).all()
        for a in groupAccounts:
            client = find_to_user(a.id)
            if client is not None:
                sendClients.append(client)
        accessor.close()
        if sendClients.count() > 0:
            for s in sendClients:
                server.send_message(s, message)
    else:
        receiver = find_to_user(data['socket_fid'])
        # 暂存至数据库
        if receiver is None:
            chat = Chats(sendid=data['socket_uid'], recid=data['socket_fid'],
                         msg=data['socket_msg'], isread=False, isgroup=False)
            insert_chat(chat)
        else:
            # 直接转发
            server.send_message(receiver['client'], message)
    print data


def run():
    server = WebsocketServer(8012, "127.0.0.1")
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()


if __name__ == "__main__":
    run()
