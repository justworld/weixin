from websocket_server import WebsocketServer


def new_client(client, server):
    try:
        print client.handler
        server.send_message_to_all('hey all,a new client has joined us')
    except BaseException,a:
        print a



def client_left(client, server):
    print 'one client has left'


def message_received(client, server, message):
    print message


def run():
    server = WebsocketServer(8013, "127.0.0.1")
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()
