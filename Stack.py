#class Stack - the main class for Stack seen in lecture 5. 
# Reminder: stack is a private variable
# To complete: *  __str__ method must be included that displays the stack in reverse
# order from the bottom to the top (with index 0 at the bottom)
#             * swap method: two swap the top with top-1 item
#             * copy method: duplicate the top item
#             * flush method: to empty the stack

class Stack:
    #constructor
    def __init__(self):
        self.__stack = []  # create private stack
    #methods
    def pop(self):  #pop the item
        if self.isEmpty(): return None
        return self.__stack.pop()

    def peek(self): #peek the item (no removal)
        if self.isEmpty(): return None
        return self.__stack[len(self.__stack)-1]

    def push(self, item): #push the item
        self.__stack.append(item)

    def getSize(self):           #return stack size
        return len(self.__stack)

    def isEmpty(self): #check if stack empty
        return self.getSize()==0
    
    def __str__(self):  #__str__ function used to display the stack
        display = ""  #initialize display
        size = self.getSize()  #get the size of the stack
        for i in range(size):   
            display = display + str(i) + "\t" + str(self.__stack[i]) + "\n"   #display the index and the corresponding value of that index
        return display.rstrip()  #removes the last blank line that forms due to "\n"
    
    def swap(self):  # swap function used to swap the first two values that appear on the stack/calc
        first_value = self.getSize()-1
        second_value = self.getSize() - 2
        self.__stack[first_value], self.__stack[second_value] = self.__stack[second_value], self.__stack[first_value]

    def copy(self):   # copy fucntion used to copy the top value of the stack
        first_value = self.getSize() - 1
        self.push(self.__stack[first_value])
    
    def flush(self):   #flush function used to delete everything on screen via the pop() method
        size = self.getSize()
        for i in range(size):
            self.pop()




################################
################################

def main():
    mystack=Stack()
    for i in range(1,4): mystack.push(i*10)
    
    print("test __str__")
    print(mystack)

    print("test swap")
    mystack.swap()
    print(mystack)

    print("test copy")
    mystack.copy()
    print(mystack)

    print("test flush")
    mystack.flush()
    mystack.push(11)
    print(mystack)
    

## call the main function if this file is directly executed
if __name__=="__main__":
    main()
