from socket import *
import threading
SERVER_ADDRESS = ('0.0.0.0', 5053)
client_list = []


class Server(object):
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(SERVER_ADDRESS)
        self.socket.listen(3)  # The serversock is listening to requests

    def session(self, clientsock):
        global client_list
        while True:
            m = (clientsock.recv(1024))
            for client_sockets in client_list:
                if client_sockets is not clientsock:
                    client_sockets.send(m)

    def run_server(self):
        global clientList
        while 1:
            print("Waiting for connection..")
            clientsock, addr = self.socket.accept()
            client_list.append(clientsock)
            print("Connected from: ", addr)
            l = threading.Thread(target=self.session, args=(clientsock, ))
            l.start()

s = Server()
s.run_server()