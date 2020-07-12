import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:{port}")

while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    # print(topic, messagedata)
    socket.send( "{} {}".format(topic, messagedata).encode('utf-8'))
    time.sleep(1)