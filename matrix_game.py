"""
What do I WANT to do?
Create and run a function that responds to a yes, no or invalid input in the command line.

What do I NEED to do?
1. import the time() module.
2. define the functions needed.
3. 1 function for positive input. 1 function for negative input. 1 function for an invalid input.
4. create a series of print() outputs based on the time() module
"""
#code start

import time

def enterTheMatrix():
        time.sleep(1)
        print("The Matrix has you ...")
        time.sleep(2)
        print("knock knock Neo ...")
        time.sleep(3)
        print("follow the white rabbit")
        time.sleep(3)
        print("We need guns. Lots of guns!")
        time.sleep(3)
        print("I know jiu jitsu!")
        time.sleep(3)
        print("You are The One!")

def agentSmith():
        time.sleep(1)
        print("Running trace program ...")
        time.sleep(2)
        print("Your location is compromised ...")
        time.sleep(3)
        print("Agents en route to your location ...")
        time.sleep(2)
        print("Danger close ...")
        time.sleep(3)
        print("3")
        time.sleep(2)
        print("2")
        time.sleep(2)
        print("1")
        time.sleep(2)
        print("You are offline")
        time.sleep(2)
        print("Program terminated")

def theArchitect():
        
        print("Program terminated")
        time.sleep(4)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Neo: Who are you?")
        time.sleep(5)
        print('''???: I am the Architect. I created the matrix. I've been waiting for you. You have many questions, and although the process has altered your consciousness, you remain irrevocably human. Ergo, some of my answers you will understand, and some of them you will not. Concordantly, while your first question may be the most pertinent, you may or may not realize it is also irrelevant.''')
        time.sleep(9)
        print("Neo: Why am I here?")
        time.sleep(5)
        print('''???: Your life is the sum of a remainder of an unbalanced equation inherent to the programming of the matrix. You are the eventuality of an anomaly, which despite my sincerest efforts I have been unable to eliminate from what is otherwise a harmony of mathematical precision. While it remains a burden assiduously avoided, it is not unexpected, and thus not beyond a measure of control. Which has led you, inexorably, here.''')
        time.sleep(9)
        print("files deleted")
        time.sleep(2)
        print("no os found")
        time.sleep(2)

def theOne():

    answer = input("will you take the red pill or blue pill?  -> " )
    if answer == ("red"):
            enterTheMatrix()
    elif answer == ("blue"):   
            agentSmith()
    else:
        print("invalid response ...")
        time.sleep(4)
        theArchitect()
        
theOne()