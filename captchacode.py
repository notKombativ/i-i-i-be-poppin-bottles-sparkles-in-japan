"""
captcha
jethughes
"""
import random
import sys 
captchaRng = random.randint(0, 4) 
#firstthing
print("User Captcha:")
print("=============")
print("")
## arrow captcha ##
#generator
direction = None
arrow = ["left", "right", "up", "down"]
direction = arrow[captchaRng - 1] #generates arrow
#visible
print("Please enter which direction the arrow is facing.")
print("")
#directions
if direction == "right":
    print("r")
elif direction == "left":
    print("l")
elif direction == "up":
    print("u")
elif direction == "down":
    print("d")
print("")
captchaOne = input("") == direction #answer
if direction == False:
    sys.exit
##Number Captcha
print("")
print("=============")
print("")
captchaNum = random.randint(100000, 999999)
print("Please input the number shown: " + str(captchaNum))
print("")
captchaTwo = input("") == captchaNum
if captchaTwo == False:
    sys.exit 
## math proficiency thinking captcha ##
print("")
print("=============")
print("")
equation = ["2+3", "5+5", "8+7", "4+16"]
question = equation[captchaRng - 1]
print("What is the answer to: " + question)
print("")
#all answers
if question == "2+3":
    mathQ = input("") == "5"
elif question == "5+5":
    mathQ = input("") == "10"
elif question == "8+7":
    mathQ = input("") == "15"
elif question == "4+16":
    mathQ = input("") == "20"
if mathQ == False:
    sys.exit
#-- 
print("")
print("=============")
print("")
