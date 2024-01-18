import random
from turtle import clear
def game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #additonal_card= random.choice(cards)
    player = {}
    dealer = {}
    player['card']= random.sample(cards,2)
    player['point']= sum(player['card'])
    dealer_card = random.sample(cards,2)
    dealer={
        'card': dealer_card,
    }
    dealer['point'] = sum(dealer['card'])

    print(f"Your card is {player['card']}, current score : {player['point']}")
    print(f"You computer's first card: {dealer_card[0]}")

    draw_more = True
    while draw_more:
        draw_card= input("Type Y to get another card, type N to to pass:")
        if draw_card == "y":
            player['card'].append(random.choice(cards))
            player['point']= sum(player['card'])
            print(f"Your card is {player['card']}, current score : {player['point']}")
            if player['point'] > 21:
                print("You went over. You lose")
                print(f"Computer's final hand is {dealer['card']}, final score : {dealer['point']}")
                break
        else:
            while dealer['point'] < 17:
                dealer['card'] += [random.choice(cards)]
                dealer['point'] = sum(dealer['card'])

            if dealer['point'] > 21:
                print(f"Computer's final hand is {dealer['card']}, final score : {dealer['point']}")
                print("You win! ")
                break
            else:
                print(f"Computer's final hand is {dealer['card']}, final score : {dealer['point']}")
                if player['point'] > dealer['point']:
                    print("You win! ")
                elif player['point'] < dealer['point']:
                    print("You lose")
                elif player['point'] == dealer['point']:
                    print("Draw")
                break




    # print(f"Your final card is {player['card']}, final  score : {player['point']}")


def play_game():
    while True:
        game()
        play_again= input("Do you want to play again ? Y/N")
        if play_again != "y":
            print("Game end!See you next time!")
            break

play_game()