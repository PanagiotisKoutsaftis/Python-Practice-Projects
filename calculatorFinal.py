import re

def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    
    
    if equation == "quit":
        run = False
        print("Goodbye earthling")
    else:
        #in case user types extra unnecessary characters
        equation = re.sub('[a-zA-Z,.:;^$#@!`~&_=?><]', ' ',equation) 
      
        if previous == 0:
            previous = eval(equation)
            
        else:
            #making the previous variable a string so we can concatenate it with the equation string
            previous = str(previous)
            #concatenating the strings and then evaluating the whole equation
            previous = eval(previous + equation)
           
        
        

previous = 0
run = True
print("Welcome Human. This is a simple calculator, be gentle.")
print("Type 'quit' if you want to exit\n")


while run:
    perform_math()
