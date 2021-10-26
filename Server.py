import socket
import datetime as dt
import threading
import Verify as av

# Select an appropriate port number.
PORT = 5000
# Set The Server's IP Address
SERVER_IP = "192.168.100.212"
# Set up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'
RECV_BYTES = 1024

# Create server 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Handle client requests
def clientHandler(conn, addr):

    file = open("Server Log File.txt",'a')

    file.write("Open new connection\n")

    connectionCode = conn.recv(RECV_BYTES).decode(FORMAT)

    file.write("Recieved connection code: " + connectionCode+"\n")

    if (len(connectionCode) < 9) : ## check if the correct number of characters was entered before proceeding
        print("Wrong Code Entered\n")
        file.write("Wrong Code Entered: wrong length detected\n")
        return    
    
    agent = ""
    if (av.check_conn_codes(connectionCode) != -1) :
        agent = av.check_conn_codes(connectionCode);
    else:
        print("Wrong Connection Code")
        file.write("Wrong code entered\n")
        conn.send("Wrong connection code".encode())
        return
    
    file.write("Agent detected, agent " +agent +"\n")
    
    question, correctAns = av.getSecretQuestion()

    print("Selected question is "+question)

    file.write("Selected question is " + question + "\n")

    conn.send(question.encode())
    file.write("Asked question... awaiting reply\n")
    
    answer = conn.recv(RECV_BYTES).decode(FORMAT)
    file.write("Answer is "+ answer+"\n")

    print(question+ " Ans "+answer)

    if answer == correctAns :
        print("Question was answered correctly: " +answer+"\n")
        welcomeMsg = "Welcome " + agent + " Time Logged - "+str(dt.datetime.now())
        file.write("Welcome message: "+welcomeMsg+"\n")
        conn.send(welcomeMsg.encode())
    else :
        conn.send("You are not welcomed".encode())
        file.write("Our 'Secret Agent' got the question incorrect "+answer+"\n")

    file.close()

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
