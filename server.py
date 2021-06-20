from socket import socket
import argparse
from threading import Thread

class ClientTh(Thread):

  def __ini__(self, sock):
    Thread.__init__(self)
    self.sock = sock

  def run(self):
    while True:
      data = self.sock.recv(4096)
      print(data)

parser = argparse.ArgumentParser()
parser.add_argument("host", default = '')
parser.add_argument("port", default = 50007, type = integer)
args = parser.parse_args()

sock = socket()
sock.bind((args.host, args.port))
sock.listen()
while True:
	conn, addr = sock.accept()
  print(addr)
  clientTh = ClientTh(conn)
  clientTh.start()