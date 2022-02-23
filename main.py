class stack:
    def __init__(self,length,stack): 
      self.length = length
      self.stack = stack

    def pop(self):
     if self.is_empty():
         del self.stack[-1]
     else:  #More error handling-------
         print("Stack under flow error --------------")
    def is_empty(self):
     return (len(self.stack) > 0) #Using the python in-built function len to act as a pointer

    def peek(self):
     return self.stack[-1]

    def push(self,item):   
      if (self.is_empty()) and (self.is_full()):
         (self.stack).append(item)
      elif not(self.is_empty()):  #More error handling-------
         print("Stack under flow error --------------")  
      elif not(self.is_full()):
         print("Stack over flow error --------------")

    def is_full(self):
      return (len(self.stack) < self.length)
    
    def describe_stack(self):
        return self.stack

#Class over
length = int(input("Enter length of stack:")) #Relevant data------
listy = input("Enter stack seperated by spaces:").split()
if not(length<=len(listy)):  #Error handling
#Testing methods required to use a stack effectively
 stack1 = stack(length,listy)
 stack1.pop()
 print(stack1.describe_stack())
 stack1.push(input("Enter something to add:"))
 print(stack1.peek())
