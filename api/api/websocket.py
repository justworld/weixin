from websocket_server import WebsocketServer


def new_client(client, server):
    server.send_message_to_all('hey all,a new client has joined us')


def run():
    server = WebsocketServer(8011, "127.0.0.1")
    server.set_fn_new_client(new_client)
    server.run_forever()
