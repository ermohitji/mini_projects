#blackjack is a game of cards
#rules
#1. points are according to cards as cards = {'A':11,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
#2. points greater than 21 player will be brusted and lose the game.
#3. to win in this game you have to accumulate points greater than other.
#4. you think wisely have you put or hand in this game.
#5  'put' means you are openning another cards for increasing your points(remember rule #2)
#6. 'hand' means you don't want to get extra points, you already have good points(remeber rule #3)

import random
cards = {'A':11,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
cardsShow = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
choice = ['put','hand']
computerCards = []
userCards = []
index=0
while index<2:
    computerCards.append(random.choice(cardsShow))
    index+=1
index=0
while index<2:
    userCards.append(random.choice(cardsShow))
    index+=1

computerSum = int(cards[computerCards[0]])+int(cards[computerCards[1]])
userSum = int(cards[userCards[0]])+int(cards[userCards[1]])

print(f"User: {userCards}")
print(f"Computer: [{computerCards[0]},hidden]")
userChoice = input("press 0 for put or press 1 for hand: ")

while True:
    if userChoice == '1':
        print(f'Computer: {computerCards}')
        if computerSum>userSum:
            print("You Lose")
        elif computerSum == userSum:
            computerChoice = random.choice(choice)
            if computerChoice == 'hand':
                print('Draw')
            else:
                computerCards.append(random.choice(cardsShow))
                print(f"Computer: {computerCards}")
                computerSum+=int(cards[computerCards[2]])
                if computerSum>21:
                    print("Computer BRUST: you WIN")
                elif computerSum>userSum:
                    print("You LOSS")
                elif userSum>computerSum:
                    print("You WIN")
                else:
                    print("DRAW")
        elif computerSum < userSum:
            computerChoice = random.choice(choice)
            if computerChoice == 'hand':
                print('Draw')
            else:
                computerCards.append(random.choice(cardsShow))
                print(f"Computer: {computerCards}")
                computerSum += int(cards[computerCards[2]])
                if computerSum > 21:
                    print("Computer BRUST: you WIN")
                elif computerSum > userSum:
                    print("You LOSS")
                elif userSum > computerSum:
                    print("You WIN")
                else:
                    print("DRAW")
        else:
            print("You LOSS")
        break
    elif userChoice == '0':
        print(f'Computer: {computerCards}')
        userCards.append(random.choice(cardsShow))
        userSum += int(cards[userCards[2]])
        print(f"User: {userCards}")
        if userSum>21:
            print("You BRUST, You LOSS")
        elif computerSum == userSum:
            computerChoice = random.choice(choice)
            if computerChoice == 'hand':
                print('Draw')
            else:
                computerCards.append(random.choice(cardsShow))
                print(f"Computer: {computerCards}")
                computerSum += int(cards[computerCards[2]])
                if computerSum > 21:
                    print("Computer BRUST: you WIN")
                elif computerSum > userSum:
                    print("You LOSS")
                elif userSum > computerSum:
                    print("You WIN")
                else:
                    print("DRAW")
        elif computerSum < userSum:
            computerChoice = random.choice(choice)
            if computerChoice == 'hand':
                print('Draw')
            else:
                computerCards.append(random.choice(cardsShow))
                print(f"Computer: {computerCards}")
                computerSum += int(cards[computerCards[2]])
                if computerSum > 21:
                    print("Computer BRUST: you WIN")
                elif computerSum > userSum:
                    print("You LOSS")
                elif userSum > computerSum:
                    print("You WIN")
                else:
                    print("DRAW")
        else:
            print("You Loss")
        break
    else:
        userChoice = input("You entered wrong input, Try again: ")


