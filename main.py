# ============================================================
# Python Final Project 2026
# Name: james mcmahon lee
# Date: 5/7/2026
# Project Title: garde calculator
# Description: this program will calulate what a student got in leter grade. after it tell them their grade it will then ask what of assiment it is and tell them the impact.
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""
user = input("whats your name ")


# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome!")
print("are you ready to calculate your grade")



# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.
numerQestions = int(input(print("how many questions are there")))
questionsCorrect = int(input(print("how many questions did you get correct")))
assimentType = str(input(print("is this a quiz,test or homework")))

# Example:
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))

# this is the code for the calculatons
grade = int(questionsCorrect) / int(numerQestions)
print (grade)


# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")

if grade >= 0.9 :
    print("you got an A great job") 
elif grade >= 0.8: 
    print("you got a B your doing great")
elif grade >= 0.7: 
    print ("you got a C keep trying harder every day")
elif grade >= 0.6:
     print ("you got a D dont give up ")
elif grade < .6:
    print("you failed")
else:
    print("you failed")

if assimentType == str("test"):
    print('this will have a major impact')
elif assimentType == str("quiz"):
    print('this will have a medium impact')
else:
    print("this will have a minor impact")




# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

print("i hope your happy with what grade you got and wish you luck until next time")
print("Thanks for using my program!")
