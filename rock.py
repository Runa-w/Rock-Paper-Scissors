# setup for game by importing the random module and declaring the winner variable
import random

winner = ''

# Here the computer randomly chooses a number between 0 and 2, and each of the three
# numbers is assigned to a string
random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

# Here an imput is created to ask the user for their choice
user_choice = ''
while (user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors'):
    user_choice = input('rock, paper, or scissors? ')

# Here is the logic of the game, where the computer checks to see if the computer won
# and makes the proper change to the winner variable

if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

# Here the winner of the game is announced, along with the computer's choice

if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. The computer chose', computer_choice + '.')
