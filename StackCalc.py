#class StackCalc: a class that extends (inherit) the functionalities
# of the class Stack 

from Stack import *
import copy
import numpy as np # if you need sin, just do np.sin, etc.

class StackCalc(Stack):    
    def __init__(self):        
      super().__init__()
    
    def rpnCommand(self, operation):   #function that oversees what user is inputting and then what operation to do 
       str_operation = str(operation)
       operations = str_operation.split()

       for i in operations:    #runs of all the input on screen
          if i == "+":
             self.add()  #if user inputs +, run add function
          elif i == "-":
             self.subtract()    #if user inputs -, run subtract function
          elif i == "*":
             self.multiply()    #if user inputs *, run multiply function
          elif i == "/":
             self.divide()      #if user inputs /, run divide function
          elif i == "^":
             self.power()    #if user inputs*+, run power function
          elif i == "sin":
             self.sin()        #if user inputs sin run sin function
          elif i == "cos":
             self.cos()       #if user inputs cos, run cos function
          elif i == "exp":
             self.exponential()     #if user inputs exp, run exponential function
          elif i == "log":
             self.log()      #if user inputs log, run log function
          elif i == "abs":
             self.absolute_value()     #if user inputs abs, run absolute_value function
          elif i == "sqrt":
             self.square_root()     #if user inputs sqrt, run square_root function
          elif i == "e":
             self.e()     #if user inputs e, run e function
          elif i == "pi":
             self.pi()       #if user inputs pi, run pi function
          elif i == "copy":
             self.copy_method()      #if user inputs copy, run copy_method function
          elif i == "swap":
             self.swap_method()     #if user inputs swap, run swap_method function
          elif i == "flush":
             self.flush()         #if user inputs flush, run flush method
          else:
             self.push(float(operation))    #if user is inputting a number, push that number as a float onto calc screen
            

    def add(self):   #Function that adds the top two values in the Calc/stack
        if self.getSize() >= 2:
          a = self.pop()
          b = self.pop()
          self.push(b+a)    
        else:
           print("Need 2 values to perform addition")
    
    def subtract(self):    #Function that subtracts the top two values in the Calc/stack
      if self.getSize() >= 2:
        a = self.pop()
        b = self.pop()
        self.push(b-a)
      else:
         print("Need at least 2 values to perform subtraction")
    
    def multiply(self):     #Function that multiplies the top two values in the Calc/stack
      if self.getSize() >= 2:
         a = self.pop()
         b = self.pop()
         self.push(b*a)
      else:
         print("Need at least 2 values to perform multiplication")
    
    def divide(self):    #Function that divides the top two values in the Calc/stack
      if self.getSize() >= 2:
         a = self.pop()
         b = self.pop()
         self.push(b/a)
      else:
         print("Need at least 2 values to perform division")
    
    def power(self):    #Function that takes the power of the top two values in the Calc/stack
      if self.getSize() >= 2:
        a = self.pop()
        b = self.pop()
        self.push(b**a)
      else:
         print("Need at least 2 values to perform power")
    
    def sin(self):      #Function gives the sin value of the top value on the stack/calc
       if self.isEmpty():
          print("Need stack to not be empty in order to perform operation")
       else:
          a = self.pop()
          self.push(np.sin(a))
    
    def cos(self):    #Function gives the cosine value of the top value on the stack/calc
       if self.isEmpty():
          print("Need stack to not be empty in order to perform operation")
       else:
          a = self.pop()
          self.push(np.cos(a))
    
    def absolute_value(self):  #Function gives the absolute value of the top value on the stack/calc
       if self.isEmpty():
          print("Need stack to not be empty in order to perform operation")
       else:
          a = self.pop()
          self.push(np.abs(a))

    def square_root(self):  #Function gives the square root  of the top value on the stack/calc
       if self.isEmpty():
          print("Need stack to not be empty in order to perform this operation")
       else:
          a= self.pop()
          self.push(np.sqrt(a))

    def exponential(self):    #Function gives the e^ of the top value on the stack/calc
       if self.isEmpty():
          print("Need stack to not be empty in order to perform operation")
       else:
          a= self.pop()
          self.push(np.exp(a))
    
    def log(self):    #Function gives the log value of the top value on the stack/calc
       if self.isEmpty():
          print("Need stack to not be empty in order to perform operation")
       else:
          a = self.pop()
          self.push(np.log(a))
    
    def copy_method(self):   #Function that copies the top value of stack assuming their is at least one value in stack
       if self.getSize() >= 1:
          self.copy()
       else:
          print("Error, need 1 or more values to perform this")
    
    def swap_method(self):     #Function that swaps the top two values in stack assuming their are atleast 2 values in stack
       if self.getSize() >= 2:
          self.swap()
       else:
          print("Error, need 2 or more values to perform operation")
       
    
    def pi(self):    #Function that push's pi (3.14..) onto the top of the stack
       self.push(np.pi)
    
    def e(self):   #Function that pushes e (2.7...) onto the top of the stack
       self.push(np.e)
    
    @staticmethod
    def postfix2infix(queue):      #staticmethod for fancy calc implementation
       copyqueue = copy.copy(queue)  #makes a copy of queue
       stack = Stack()   #Creates object of class Stack

       while not copyqueue.isEmpty():    #as long as queue isn't empty, proceed
          symbol = copyqueue.dequeue()

          if symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/" or symbol == "^":   #if user inputs +,-,*,/ or ^ that use top two values on stack
             value1 = stack.pop()
             value2 = stack.pop()
             if symbol == "^":
                display = "(" + value2 + "**" + value1 + ")"   # using ** instead of ^
             else:
                display = "(" + value2 + symbol + value1 + ")"   # formatted to show operation using parthethesis and operations
             stack.push(display)  #shows the equation on the calc. screen
          
          elif symbol == "sin" or symbol == "exp" or symbol == "cos" or symbol == "abs" or symbol == "sqrt" or symbol == "log":
             value3 = stack.pop()
             display = symbol+ "(" + value3 + ")"
             stack.push(display)
          
          elif symbol == "copy":
             value4 = stack.pop()
             stack.push(value4)
             stack.push(value4)

          elif symbol == "swap":
             top_value = stack.pop()
             sec_value = stack.pop()
             stack.push(top_value)
             stack.push(sec_value)
          
             
          elif symbol == "pi" or symbol == "e":
             stack.push(symbol)  #shows the equation on the calc. screen
          
          else:
             stack.push(symbol)   #pushes number 
        
       if not stack.isEmpty():   #senario when nothing exists in the stack
          return stack.peek()
       else:
          return ""
    
    @staticmethod
    def evaluate_postfix(queue, x=None):
       copyqueue = copy.copy(queue)
   
       mystack=StackCalc()

       while not copyqueue.isEmpty():
          input1 = copyqueue.dequeue()

          if input1 == "x":
             mystack.rpnCommand(x)
          else:
            mystack.rpnCommand(input1) 

       return mystack.pop()

          
    

