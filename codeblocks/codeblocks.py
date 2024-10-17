"""
pre-written code snippets to help during competition

trying to make these concise and generalized for plug and play like usage
- name
- tag
- codeblock



INPUT

!!! Function Setup to Take in User Input (input, functions)

res_list = []

while True:
    res = ""

    # handle input
    line = input()
    # line = int(input()) # cast to an int for example
    if line == "quit" or line == "" or line == "EOF": break

    if line == "implement logic":
        res = "logic done"
    
    res_list.append(res)

for r in res_list: print(r)

HASHMAPS

!!! Looping through a Hashmap Accessing Keys and Values (hashmap, looping)

hashmap = {"a": 0, "b": 1, "c": 2, "d": 3}

for key, value in hashmap.items():
    print(key, value)

!!! Checking if key or value is in hashmap (hashmap)

hashmap = {"a": 0, "b": 1, "c": 2, "d": 3}

# can also use variable
if "a" in hashmap:
    print("a found keys")

value_to_check = 2
if value_to_check in hashmap.values():
    print("2 found in values")

!!! Creating a hashmap with keys as characters and values as the characters' frequencies (hashmap, looping, counting)

can also use defaultdict(int) to make the hashmap values be ints
from collections import defaultdict

given_string = "Lebron James is the goat"

hashmap = {}
for c in given_string:
    if c in hashmap:
        hashmap[c] += 1
    else:
        hashmap[c] = 1

print(hashmap)

TUPLES 

!!! Sorting a tuple (in place of a hashmap) by their values (tuple, hashmap, sorting, list)

tuple_list = [("lebron", 999), ("david", 4), ("alex", 7), ("michael", 99), ("dylan", 10000)]

tuple_list.sort(key=lambda pair: pair[1], reverse=True) # edit the existing list, reverse parameter to make it ascending/descending
# sorted_list = sorted(tuple_list, key=lambda pair: pair[1]) # make a new list (not change the current one)

print(tuple_list)
print(tuple_list[0])
print(tuple_list[-1])

LISTS

!!! Compare Adjacent Elements in a List (i and i +1) (list)

ls = [-1, 2, -3, 1]

for curr, nxt in zip(ls, ls[1:]):
    print(curr, nxt)

!!! Sort a List (list, sorting)

ls = [-1, 2, -3, 1]

sorted_list = sorted(ls, reverse=True) # not modify list
ls.sort() # modify list

print(sorted_list)
print(ls)

!!! List/String Splitting (list, string)

ls = [-1, 2, -3, 1]
given_string = "Dairy Cow is Pretty Cool"

print(ls[:2]) # everything in the list from index 2 to the start (inclusive)
print(ls[1:]) # everything in the list from index 1 and on
print(ls[::-1]) # reversed the list
print(ls[-1]) # last element of the list

print(given_string[2]) # character at element 2
print(given_string[6:])
print(given_string[:9])
print(given_string[::-1])
print(given_string[-1])

STRING


"""




