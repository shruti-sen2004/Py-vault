from typing import List, Dict
from collections import defaultdict
# dictionariees - maps or hashmaps
# has key valye pairs; Key- unique value- may or maynot be unique

my_dict = {}

my_dict["Avishek"] = 30 # insertion with key not index
my_dict["Shruti"] = 35
print(my_dict)

def list_to_dict(words: List[str]) -> Dict[str,int]:
    mew_dict ={}
    for i in range(len(words)):
        w = words[i]
        my_dict[w] = i
    return my_dict
print(list_to_dict(["Shruti","Avishek","Ritu"]))

my_dict = {"a":[1,2],"b":{4,5,6},"c":{1:"Shru",2:"Avi"}} # can have any value
print(my_dict["c"])
my_dict["a"] = 100  # overides the values
print(my_dict)

print("b" in my_dict) # exists or not

myMap = {i:2*i for i in range(3)}
print(myMap)
print()

for key in my_dict: # loop
    value = my_dict[key] 
    print(key,value)

for key,value in my_dict.items(): # short-hand for loop
    print(key,value)

# value = my_dict.get(key, default_value) # better way to check existence
# simplies dictionary lookups with default values

def count_characters(word: str) -> Dict[str, int]: # frequency count
    count= {}
    for char in word:
        if char not in count:  # handle KeyError
            count[char] = 0
        count[char] += 1
    return count
print(count_characters("hello"))

# frequency-count short hand - pythonic code
counts = defaultdict(int) # auto initializes counts to 0
for item in my_dict:
    counts[item] += 1
print(counts)

my_dict.pop("b")
print(my_dict)
#my_dict.pop("d") # raises Keyerror
my_dict.pop("d",0) # handle it; don't throw error just return 0

for value in my_dict.values(): # iterate ver values
    print(value)

# sorted by default arranges in ascending on basis on keys
counts ={'a':1, 'b':3, 'c':2}
res_asc= dict(sorted(counts.items(), key=lambda item: item[1])) # sort on the base of value in ascending
res_dsc = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)) # sort on the base of value in descending
print(res_asc)