# coding=utf-8

from websocket_server import WebsocketServer
import json

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


def new_client(client, server):
    server.send_message_to_all('hey all,a new client has joined us')


def client_left(client, server):
    print 'one client has left'


def message_received(client, server, message):
    data = json.loads(message)
    print data


def run():
    server = WebsocketServer(8012, "127.0.0.1")
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()


if __name__ == "__main__":
    run()
