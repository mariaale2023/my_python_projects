### 7 kyu Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

# create a function to remove vowels from a given string

def disemvowel(string_):
    vowels = "aeiou"
    # using list comprehension
    string_ = ''.join(char for char in string_ if char.lower() not in vowels)
    return string_

# testing

print(disemvowel("This website is for losers LOL!"))
print(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))
print(disemvowel("What are you, a communist?"))
print(disemvowel("First fixed test"))
print(disemvowel("Test"))