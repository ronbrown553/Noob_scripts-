# This while loop tells the user that this is a loop and ask the questions "do you want this to end". 
# If the answer is anything other than "yes", the loop keeps going. 

while True: 
    print("this is a loop")
    inp = input("do you want this to end? ")
    if inp == "yes":
        break 
