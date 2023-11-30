import random

#Testing different ways to code my brute force cracker 

#First two are for number only passwords

#can use random to get the cracker to generate random number guesses until it reaches the password



number = int(input("Input a number based password: "))
guess = 0 
while (guess != number):
    guess = random.randint(0,9999999)
    print(guess)
print("Your Password Is " + str(number))

#can create a while loop to go through numbers until it reaches the password

number =int(input("Input a number that is a password: "))
guess = 0 
while (number != guess):
    print(guess)
    guess +=1
print("Your Password is " + str(number))

#Can also do random with numbers and characters
#This takes longer due to how its guessing the legnth of the password

character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)
password = input("Enter Your Password: ")

guess = ""
while(guess != password):
    guess = random.choices(character_list,k=len(password))
    print(guess)

print("The password is " + guess)