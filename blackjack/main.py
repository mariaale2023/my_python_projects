import random
## HAD TO ADD SEVERAL \\ TO ESCAPE THE \ SYMBOL
TITLE = """ _______   ___            __       ______   __   ___       ___      __       ______   __   ___  
|   _  "\\ |"  |          /""\\     /" _  "\\ |/"| /  ")     |"  |    /""\\     /" _  "\\ |/"| /  ") 
(. |_)  :)||  |         /    \\   (: ( \\___)(: |/   /      ||  |   /    \\   (: ( \\___)(: |/   /  
|:     \\/ |:  |        /' /\\  \\   \\/ \\     |    __/       |:  |  /' /\\  \\   \\/ \\     |    __/   
(|  _  \\\\  \\  |___    //  __'  \\  //  \\ _  (// _  \\    ___|  /  //  __'  \\  //  \\ _  (// _  \\   
|: |_)  :)( \\_|:  \\  /   /  \\\\  \\(:   _) \\ |: | \\  \\  /  :|_/ )/   /  \\\\  \\(:   _) \\ |: | \\  \\  
(_______/  \\_______)(___/    \\___)\\_______)(__|  \\__)(_______/(___/    \\___)\\_______)(__|  \\__) 
                                                                                                """

print(TITLE)

# create the deck of cards
cards = list(range(1, 14))
cards[0] = 11
cards[9:13] = [10] * 4

#default conditions
player_loses = False
house_loses = False
player_cards = []
house_cards = []


# function: draw a card
def draw(list, n=1):
    for i in range (n):
        list.append(cards[random.randint(0,12)])
    return list


def check(list):
    if sum(list) > 21: return True
    else: return False

player_cards= draw(player_cards,2)
# current_score = sum(player_cards)
while sum(player_cards) <= 21:
    # show current cards and ask if wants to draw another
    if sum(player_cards) == 21:
        print("BlackJack! you win")
        break
    choice = str(input (f"your cards {' - '.join(map(str, player_cards))  }: your current: score {sum(player_cards)}. Do you want to [D]raw or [S]tay?: "))
        
    #if draw, append a new card
    if choice.lower() == "d" or choice.lower() == "draw":
        player_cards = draw(player_cards)
        print(player_cards)
        # check 3 conditions: >21, 21, <21
        player_loses = check(player_cards)
        if sum(player_cards) > 21:
            print(f"you lose, your total score was {sum(player_cards)}")
            break
        else:
            continue

    elif choice.lower() == "s" or choice.lower() == "stay":
        print(f"end of your play, your sum is {sum(player_cards)}")
        break

    else:
        print("wrong input. Try again")


# house plays
if not player_loses:
    house_cards = draw(house_cards,2)
    while sum(house_cards) < 16:
        house_cards = draw(house_cards)
        print(f"house cards: {' - '.join(map(str, house_cards))}. the house has: {sum(house_cards)}")
        if sum(house_cards)>21:
            house_loses = True
            print(f"the house loses. House score: {sum(house_cards)}")
            
    print(f"player score: {sum(player_cards)}. House score: {sum(house_cards)}")

#final results just if player and house haven't lose already
if not player_loses and not house_loses:

    if sum(player_cards) == sum(house_cards):
        print(f"tie at {sum(player_cards)} points") 
    elif sum(player_cards) > sum(house_cards):
        print(f"player wins {sum(player_cards)} vs {sum(house_cards)}") 
    else:
        print(f"the house wins {sum(house_cards)} vs {sum(player_cards)}") 


#TODO chance of replacing an ace (11) for 1 in case the sum > 21