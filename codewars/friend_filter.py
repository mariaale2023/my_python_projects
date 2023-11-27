# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
# if the name is 4 char long, return it in a new string

def friend(x):
    new_list = []
    for i in range(len(x)):
        if len(x[i]) == 4:
            new_list.append(x[i])

    return(new_list)


# testing

print(friend(["Ryan", "Kieran", "Mark",]))
print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]))
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))