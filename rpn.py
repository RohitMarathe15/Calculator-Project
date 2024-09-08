from StackCalc import *
from Queue import *
from numpy import *  # if you need sin, just do sin, etc.
import matplotlib.pyplot as plt


# Menu
print()
print("===============================================")
print("================= Project 1 ===================")
print("===============================================")
print("|                                             |")
print("|         1-Simple  RPN calculator            |")
print("|         2-Fancy   RPN calculator            |")
print("|         3-Fancier RPN calculator            |")
print("|                                             |")
print("===============================================")
print()
choice=input("Your choice: ")


mystack=StackCalc()
myqueue=Queue()


if choice=="1": #////////////// Simple RPN calculator

    print("Welcome to the simple RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        prompt=input(">")    
        if prompt=="quit": break
        mystack.rpnCommand(prompt)



if choice=="2": #////////////// Fancy RPN calculator

    print("Welcome to the fancy RPN calculator (enter 'quit' to quit)");
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        if not myqueue.isEmpty(): #Display both postfix and infix
            print("Postfix: "+str(myqueue))
            print("Infix: ",StackCalc.postfix2infix(myqueue))
        prompt=input(">")    
        if prompt=="quit": break
        mystack.rpnCommand(prompt)
        if prompt!="flush":
            myqueue.enqueue(prompt)
        else:
            myqueue.flush()

        
if choice=="3": #////////////// Fancier RPN calculator

    print("Welcome to the fancier RPN calculator (enter 'quit' to quit)");
    while True:
        print("------------------------------------------------------------")
        if not myqueue.isEmpty():
            print("Postfix: " + str(myqueue))
            print("Infix: ", StackCalc.postfix2infix(myqueue))
        prompt = input(">")
        if prompt == "quit":  # if user quits the function
            break
        elif prompt == "run":   #if user wants to get the results of infix/postfix
            if myqueue.find("x"):   #Checks to see if x is present in the queue (meaning user has entered x)
                x = float(input("Enter x value: "))  #asks for x value from user
            else:
                x = None
            
            infix = None

            if x == None:
                infix = StackCalc.postfix2infix(myqueue)
            else:
                tempInFix = StackCalc.postfix2infix(myqueue)
                infix = tempInFix.replace("x",str(x))
            final = eval(infix)
            print("Solution using infix: ", final)
            postfix = StackCalc.evaluate_postfix(myqueue, x)
            print("Solution using postfix: ", postfix)
        
        elif prompt == "plot":
            if myqueue.find("x"):
                xmin, xmax, nbp = input("Enter values for xmin, xmax, nbp: ").split()
                infix = StackCalc.postfix2infix(myqueue)

                xmin = float(xmin)
                xmax = float(xmax)
                nbp = int(nbp)

                increment = ( xmax - xmin ) / nbp 

                xAxislist = []
                yAxisList = []

                xAxislist.append(xmin)
                yAxisList.append(StackCalc.evaluate_postfix(myqueue, xmin))
                
                temp = xmin
                for i in range(1,nbp):
                    temp = temp + increment 
                    xAxislist.append(temp)
                    yAxisList.append(StackCalc.evaluate_postfix(myqueue, temp))
                
                plt.plot(xAxislist, yAxisList, label='Line 1')
                graph_title = "f(x)= "+ infix
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.title(graph_title)
                plt.show()

                
                    
                
    
        else:
            myqueue.enqueue(prompt)
















print("Thanks for using the RPN calculator")
