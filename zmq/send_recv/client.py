import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect (f"tcp://localhost:{port}")

if len(sys.argv) > 2:
    socket.connect (f"tcp://localhost:{port}")




# Subscribe to zipcode, default is NYC, 10001
topicfilter = "10001".encode("utf-8")
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
for update_nbr in range (5):
    string = socket.recv()
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print(topic, messagedata)

print("Average messagedata value for topic {} was {}".format(topicfilter, total_value / update_nbr))