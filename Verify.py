import random

#from Agent import RECV_BYTES

#from Server import AGENTS

AgentA_codes = []
AgentB_codes = []

predefined = ["AJK78", "KTV90", "NEL55", "DFG28"]

AgentA = "2975"
AgentB = "6144"

# Write code that will Generate all possible connection codes for the Agents and store them in their respective arrays. 
for pre in predefined:
    agentACode = pre+AgentA
    agentBCode = pre+AgentB
    AgentA_codes.append(agentACode)
    AgentB_codes.append(agentBCode)


questions = [("I saw a purple Kangaroo yesterday, did you?", "Only after the sun went down"),
             ("What did Eve say when she ate the fruit?", "Nothing"),
             ("What do you call a fish wearing a bowtie?", "Sofishticated"),
             ("What did the ocean say to the beach?", "Nothing it just waved"),
             ("Why did God save men but not fallen angels?", "Good Question")]

#This function should return a random instance from the questions array. 
def getSecretQuestion():
    randomNum = random.randint(1,len(questions) - 1)
    return questions[randomNum]

#This function must check the connection code given by the client (Agent) and return the name of the Agent (Agent A or B). If the code is invalid the function should return -1.
def check_conn_codes(connCode):
    print(AgentA_codes)
    print(AgentB_codes)
    print(connCode in AgentA_codes)
    print(connCode in AgentB_codes)
    if (connCode in AgentA_codes) : # Check if code is in either agent a or agent b
        return "Agent A"
    elif (connCode in AgentB_codes) :
        return "Agent B"
    else :
        return -1



    
