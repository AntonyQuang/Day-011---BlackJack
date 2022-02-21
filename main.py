############### Blackjack Project #####################

#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import random
#import replit
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(user):
  card = random.choice(cards)
  return user.append(card)

def score(hand):
  if sum(hand) > 21 and 11 in hand:
    hand[hand.index(11)] = 1  
  return sum(hand)

def player_round(player, cpu):
  draw_card(player)
  score(player)
  game_status(player, cpu)

def game_status(player, cpu):
  print(f"\tYour cards: {player}, current score {score(player)}" )
  print(f"\tComputer's first card: {cpu[0]}")

def cpu_round(cpu):
  score(cpu)
  while score(cpu) < 17:
    draw_card(cpu)
    score(cpu)
  return score(cpu)


def final_scores(player, cpu):
  print(f"\tYour final hand: {player}, final score: {score(player)}")
  print(f"\tComputer's final hand: {cpu}, final score: {score(cpu)}")

def compare_scores(player_score, cpu_score):
    if player_score == cpu_score:
      return "It's a draw!"
    elif player_score == 21:
      return "You won with BlackJack! ♠"
    elif cpu_score == 21:
      return "The Computer won with BlackJack! 💀"
    elif player_score > 21:
      return "You went over. You lose! 😣"
    elif cpu_score > 21:
      return "The Computer went over. You win! 😀"
    elif player_score > cpu_score:
      return "You win! 😎"
    elif cpu_score > player_score:
      return "You lose! 😥"


def play_game():
  player = []
  cpu = []
  draw = True
  #replit.clear()
  cls()
  print(art.logo)
  draw_card(player)
  draw_card(cpu)
  player_round(player, cpu)
  while draw == True and score(player) < 22:
    hit = input("Do you want to draw another card? Type 'y' or 'n': ")
    if hit == 'y':
      player_round(player, cpu)
    else:
      draw = False
  cpu_round(cpu)
  final_scores(player, cpu)
  print(compare_scores(score(player), score(cpu)))
    
while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
  play_game()

print("Goodbye!")
      


