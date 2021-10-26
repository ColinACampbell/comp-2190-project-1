import socket

# Select an appropriate port number. 
PORT = 5000
# Set The Server's IP Address
SERVER_IP = "192.168.100.212"
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
RECV_BYTES = 1024

file = open("Agent Chat Log.txt","a")
file.write("----Chat initiated----\n")

# Open TCP socket connections
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

file.write("----Connected to server----")

def send(msg):
    file.write("Sent: "+msg+"\n")
    client.send(msg.encode()) # encode to bytes

def getConCode():
    return input("What is your connection code secret agent? ")

def getAnswer(question):
    return input(question)

connCode = getConCode()

send(connCode)

question = client.recv(RECV_BYTES).decode(FORMAT)
file.write("Recieved question: "+question+"\n")

answer = getAnswer(question)

send(answer)

# Recive and print response from the server.
resp = client.recv(RECV_BYTES).decode(FORMAT)
print(resp)