#Manhua Chen and Duoshu Xu

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)
print(f'Play Against: {p2}')

if p1 == p2:
    print('It is a tie!')
elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
    print('Win!')
else:
    print('Lose!')