# dictionary_1 = {"V344LDA":2000,
#                 "J245DWE":6350,
#                 "K265QWS":500}

# print("\n\n The value of the car registracion of V344LDA is", dictionary_1["V344LDA"])


# # create a mapping of state to abbreviation
# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }

# # create a basic set of states and some cities in them

# cities = {
#   "CA" : 'San Fancisco',
#   'MI': 'Detroit',
#   'FL': 'Jacksonville' 
# }

# # add some citys
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# print('_' * 10)
# print("NY startes has: ", cities['NY'])
# print("OR startes has: ", cities['OR'])


#   # print every state abbreviation
# print ('-' * 10)
# for key, value in states.items():
#     print("{0} is abbreviated {1}".format(key, value))

# print ('-' * 10)
# name = "Alice"
# age = 30

# formatted_string = "My name is {0} and I am {1} years old {2}.".format(name, age, ". But I am still young")

# print(formatted_string)

# # do it by using the state then cities dict
# print ('-' * 10)
# print('Mitchigan has: ', cities[states['Michigan']])

# print ('-' * 10)
# # safely get a abbreviation by state that might not be there

# # Use get() method => 
#   #   value = dictionary.get(key, default_value)
# state = states.get('Texas')
# if not state:
#     print ("Sorry, no Texas.")

# state_Texas = states.get('Texas', "Sorry, no Texas state")
# print (state_Texas)

# print ('-' * 10)
# states['Chile'] = "Santiago"
# print(states)

# print ('-' * 10)
# more_states = {"arg": "Buenos Aires" , "Brasil" : "Brasilia"}
# states.update(more_states)
# print(states)

# # loop dictonary
# print ('-' * 10)
# for key in states:
#     print(key, states[key])

# print ('-' * 10)
# for key in states.keys():
#     print(key)

# print ('-' * 10)
# for value in states.values():
#     print(value)

# print ('-' * 10)
# for key, value in states.items():
#     print(value, "is in ", key)

# # Comprehension
# print ('-' * 10)

# square = []
# for i in range(10):
#     square.append(i**2)
# print(square)

# print ('-' * 10)
# print (4+10)




# square3 = [i**2 for i in range(15) if i % 3 == 0]
# print(square3) 

# print('-' * 10)
# square3 = [i**2 for i in range(30) if i % 3 == 0]
# print(square3) 

# print('-' * 10)
# square4 = {i : i**2 for i in range(30) if i % 3 == 0}
# print(square4) 
# print('-' * 10)
# for key, value in square4.items():
#   print(f'{key}: {value}')
