from websocket_server import WebsocketServer


def new_client(client, server):
    print client.handler
    server.send_message_to_all('hey all,a new client has joined us')


def client_left(client, server):
    pass


def message_received(client, server, message):
    print message


def run():
    pass
    server = WebsocketServer(8012, "127.0.0.1")
    server.set_fn_new_client(new_client)
    server.run_forever()
