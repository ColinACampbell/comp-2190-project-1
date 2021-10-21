import socket

# Select an appropriate port number. 
PORT = 5000
# Set The Server's IP Address
SERVER_IP = "192.168.100.212"
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
RECV_BYTES = 1024

# Add code to initialize the Socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Write Code that will allow the Client (Agent) to send messages to the server. The Function accepts the message as a String (msg) and sends that message to the Server through a connection established.
def send(msg):
    client.send(msg.encode())

# Write code to Prompts the Agent to enter their connection code and returns the code given.
def getConCode():
    return input("What is your connection code secret agent? ")

# Write code to Prompts the Agent to enter an answer and returns the answer given.
def getAnswer(question):
    return input(question)

# Get Connection Code.
connCode = getConCode()

# Send Connection Code to Server.
send(connCode)

# Recive question from server.
question = client.recv(RECV_BYTES).decode(FORMAT)

# Get Answer from Agent.
answer = getAnswer(question)

# Send Answer to Server.
send(answer)

# Recive and print response from the server.
resp = client.recv(RECV_BYTES).decode(FORMAT)
print(resp)