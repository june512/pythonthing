print ("Take this simple test to find out your IQ")
print ("jk")
print ("take this simple test \n")
print ("Who is the best person alive?")

isWrong = True

while isWrong:
    userChoice = input("Your Choice: ")
    if userChoice == "June":
        print ("correct")
        isWrong = False
    elif userChoice == "Jay":
        print ("half credit")
        isWrong = False
        
    else:
        print ("incorrect, try again")
        isWrong = True;
    
print ("Who was our first president?")
isWrong = True

while isWrong:
    userChoice = input("Your Choice:")
    if userChoice == "George Washington":
        print ("correct, good job")
        isWrong = False
    else:
        print ("how do you not know this honestly, try again")
        isWrong = True;
        
print ("What is your name?")

isWrong = True

while isWrong:
    userChoice = input("Your Name: ")
    if userChoice == "June":
        print ("that's my name, not yours!")
        isWrong = True;

    else:
        print ("thats a nice name you have there")
        isWrong = False
print ("thank you for taking this short little quiz")
