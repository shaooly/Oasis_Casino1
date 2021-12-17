from socket import *
import threading
import datetime

HOST = '127.0.0.1'
PORT = 5053
ADDR = (HOST, PORT)
name = input("please enter your name")

class MyClient(object):
    def __init__(self):
        self.sock = socket()

    def get_connection(self):
        self.sock.connect(ADDR)

    def sessiom_with_server(self):
        sending = SendClass(self.sock)
        sending.start()
        reciving = RecvClass(self.sock)
        reciving.start()


class RecvClass(threading.Thread):


    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    def run(self):
        while True:
            m = self.sock.recv(1024).decode()
            print(m)

class SendClass(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    def run(self):
        global name
        while True:
            mess = input()
            x = datetime.datetime.now()
            to_send = x.strftime("%X") + " " + name + " says: " + mess
            self.sock.send(to_send.encode())


c = MyClient()
c.get_connection()
c.sessiom_with_server()
