import socket
import datetime as dt
import threading
import Verify as av



questionsAndAns = {
    "I saw a purple Kangaroo yesterday, did you?": "Only after the sun went down",
    "What did Eve say when she ate the fruit?": "Nothing",
    "What do you call a fish wearing a bowtie?": "Sofishticated",
    "What did the ocean say to the beach?": "Nothing, it just waved",
    "Why did God save men but not fallen angels?": "Good Question",
}

# Select an appropriate port number.
PORT = 5000
# Set The Server's IP Address
SERVER_IP = "192.168.100.212"
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

# Add code to initialize the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Write Code to bind Address to the server socket.
server.bind(ADDR)

# This function processes messages that are read through the Socket.


def clientHandler(conn, addr):

    # Write Code that allows the Server to receive a connection code from an Agent.
    """Your Code here"""
    connectionCode = conn.recv(1024).decode(FORMAT)
    print("Message is "+connectionCode)

    # Write Code that allows the Server to check if the connection code received is valid.
    """Your Code here"""

    # Write Code that allows the Server to retrieve a random secret question.
    """Your Code here"""

    # Write Code that allows the Server to send the random secret question to the Client.
    """Your Code here"""

    # Write Code that allows the Server to receive an answer from the Client.
    """Your Code here"""

    # Write Code that allows the Server to check if the answer received is correct.
    """Your Code here"""

    # Write Code that allows the Server to Send Welcome message to agent -> "Welcome Agent X"
    """Your Code here"""


def runServer():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=clientHandler, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")


print("[STRTING] The Server is Starting...")
runServer()
