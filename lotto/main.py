import random

TITLE = """    __          __  __           _   _______            _      __            
   / /   ____  / /_/ /_____     / | / /__  /     ____  (_)____/ /_____  _____
  / /   / __ \/ __/ __/ __ \   /  |/ /  / /     / __ \/ / ___/ //_/ _ \/ ___/
 / /___/ /_/ / /_/ /_/ /_/ /  / /|  /  / /__   / /_/ / / /__/ ,< /  __/ /    
/_____/\____/\__/\__/\____/  /_/ |_/  /____/  / .___/_/\___/_/|_|\___/_/     
                                             /_/                             """

# an automatic lotto number creator

# create a list with numbers 1 to 40
numbers = list(range(1,41))

print(TITLE)
n = int(input("Welcome to lotto. How many lines are you going to play today?: "))


for i in range (n):
    # pick a powerball
    powerball = random.randint(1,10)
    # shuffle the numbers
    random.shuffle(numbers)
    # select a slice of the 6 first numbers
    numbers_selected = numbers[:6]

    # now will be sorted to show them tidier
    numbers_selected = sorted(numbers_selected)
    
    # the selected numbers are going to be shown as '01 - 02 - 03 ...'
    # lambda function to show numbers with a leading 0 if they are lower than 10
    number_string = (' - ').join(map(lambda x: f'{x:02}', numbers_selected))

    print(f"Ticket number {i+1}: {number_string}. Powerball: {powerball}")

print("Good luck!")

# pick powerball