#  user guessing the number

import random
def guess_number():
    return random.randint(1,100)

target_number  = guess_number()
attempts = 0
while True:
    user_guess = int(input("guess the number : "))
    attempts += 1
    
    if user_guess == target_number:
        print("congratulation, you guessed the number in ", attempts ,"attempts")
        
    elif user_guess<target_number:
        print("guess a higher number")
        
    else:
        print("guess a lower number.")