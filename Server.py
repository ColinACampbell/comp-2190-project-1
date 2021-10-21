import socket
import datetime as dt
import threading
import Verify as av
import random

SECRET_QUESTIONS = {
    "I saw a purple Kangaroo yesterday, did you? ": "Only after the sun went down",
    "What did Eve say when she ate the fruit? ": "Nothing",
    "What do you call a fish wearing a bowtie? ": "Sofishticated",
    "What did the ocean say to the beach? ": "Nothing, it just waved",
    "Why did God save men but not fallen angels? ": "Good Question",
}


AGENTS = {
    "2975" : "Agent A",
    "6144" : "Agent B"
}

PREDEFINED_CHARS = ["AJK78", "KTV90", "NEL55", "DFG28"]

# Select an appropriate port number.
PORT = 5000
# Set The Server's IP Address
SERVER_IP = "192.168.100.212"
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
RECV_BYTES = 1024

# Add code to initialize the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Write Code to bind Address to the server socket.
server.bind(ADDR)

# This function processes messages that are read through the Socket.
def clientHandler(conn, addr):

    # Write Code that allows the Server to receive a connection code from an Agent.
    connectionCode = conn.recv(RECV_BYTES).decode(FORMAT)

    # Write Code that allows the Server to check if the connection code received is valid.
    if (len(connectionCode) < 9) : ## check if the correct number of characters was entered before proceeding
        print("Wrong Code Entered")
        return    
    
    predefChar = connectionCode[:5]
    agentCode = connectionCode[5:9] # I used to to 9 becuase if I don't set boundry, any data from the buffer/memory from previos trans, would be included

    if (not ( (agentCode in AGENTS) and (predefChar in PREDEFINED_CHARS))) :
        print("We have an imposter")
        return
    
    agent = AGENTS[agentCode]
    
    # Write Code that allows the Server to retrieve a random secret question.
    questions = list(SECRET_QUESTIONS.keys())
    randomNum = random.randint(1,len(questions) - 1)

    print("Random = "+ str(randomNum) + " Zero is " + questions[0])
    selectedQuestion = questions[randomNum] ## Incase the agency adds more questions


    # Write Code that allows the Server to send the random secret question to the Client.
    conn.send(selectedQuestion.encode())

    # Write Code that allows the Server to receive an answer from the Client.
    answer = conn.recv(RECV_BYTES).decode(FORMAT)

    # Code that allows the Server to check if the answer received is correct.
    # A Code that allows the Server to Send Welcome message to agent -> "Welcome Agent X"

    print(SECRET_QUESTIONS[selectedQuestion]+ " Ans "+answer)

    """Your Code here"""
    if answer == SECRET_QUESTIONS[selectedQuestion] :
        welcomeMsg = "Welcome " + agent + " Time Logged - "+str(dt.datetime.now())
        conn.send(welcomeMsg.encode())
    else :
        conn.send("You are not welcomed".encode())


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
