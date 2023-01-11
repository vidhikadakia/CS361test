
print("Enter the integer for the player to guess. ")
my_num = int(input())
tries = 0
print("Enter your guess.")
num_guess = int(input())

while(num_guess!=my_num):
    tries = tries + 1
    if (num_guess > my_num):
        print("Too high - try again:")
        num_guess = int (input())
    elif (num_guess < my_num):
        print("Too low - try again:")
        num_guess = int (input())
tries = tries + 1
if tries >1:
    print(f"You guessed it in {tries} tries.")
elif tries == 1:
    print("You guessed it in 1 try.")
