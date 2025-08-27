## Itertools - module containing diffrent iterators and function for combining several iterator
## Present in python standard library

import itertools
import operator # for multiply op in accumulate()
### Infinite iterators

## 1. count()
## by default starts at 0, goes up by 1 
## can give start and step (even decimals and negative)
counter = itertools.count(start=5, step=-2.5) 
# print(next(counter))
# print(next(counter))
# print(next(counter))

data = [100,200,300,400]
daily_data = list(zip(itertools.count(),data)) #combines two iterables by pairing each value
# print(daily_data)

## 2.ziplongest()
## works similar to zip but here the function does not stop until the longest iterable is exhausted
data = [100,200,300,400]
# daily_data = list(zip(range(10),data)) # combines until shortest iterable is exhausted
daily_data = list(itertools.zip_longest(range(10),data)) # longest iterable size 10 so when data is exhausted pairs with None
# print(daily_data)

## 3. cycle()
## cycles through iterable infinetly
counter = itertools.cycle((1,2,3,))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) # starts the cycle over 
print(next(counter))

## 4. repeat()
## takes an input and repeats infinetly
counter = itertools.repeat(2, times =3)

squares = map(pow, range(10), itertools.repeat(2)) # iterate constant steams of data until shortest iterable is exhausted
print(list(squares))

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter)) # throws stopIteration Exception
# note: if used if forloop the error does not appear as for loop handles the exception

## 5. starmap()
## similar to map but takes list of tuples as arguments that are already paired
squares = itertools.starmap(pow,[(0,2),(1,2),(2,2)])
print(list(squares))

print('-'*40)

### iterables that will terminate eventually 
## 1. Permutation and combinations
## Different no.of ways to group an item without repetation of items
## Combination - order does not matter; Permtation - order does matter

letters = ['a','b','c','d']
nums= [0,1,2,3,2,1,0]
result = itertools.combinations(letters,2)
result = itertools.permutations(letters,2)

passcode = itertools.product(nums, repeat=4) # cartesian product, allows repeats (permutation with repeats)
passcode = itertools.combinations_with_replacement(nums,4) # combinations but allows repeats

## 2. chain()
## iterate through all the iterables until they are exhausted
combined = itertools.chain(letters,nums)

## 3. islice
## performs slicing in iterators
result = itertools.islice(range(10),1,5,2) # start(can avoid start value), stop, step

## 4. compress
## only return whose iterable items that had a corosponding true value
## similar to filter funcn but this decides true or false from the iterables passed and not func
selectors =[True,False,True,False]
result = itertools.compress(letters,selectors)

## 5. filterfalse()
## returns only those values that corrospond to false 
def l_func(n):
    if n<2:
        return True
    return False
result = itertools.filterfalse(l_func,nums)

## 6. dropwhile()
## drops value until first iterable that corresponds to true ocuurs then continue
result = itertools.dropwhile(l_func,nums)

## 7. takewhile()
## take all value until first iterable that corresponds to false ocuurs 
result = itertools.takewhile(l_func,nums)

## 8. accumualte()
## returns accumulated sums of each iterable that it sees (last value is the total accumulated sum of that list)
## By default addition but can use other operations too
result = itertools.accumulate(nums, operator.mul)
# for i in result:
#     print(i)

## 9. groupby()
## groups values based on a certain key and return a stream of tuples
## a little diffrent from SQL groupby as it needs the dictionary to be pre-sorted
def get_state(person):
    return person['state'] # tells groupby to group by state

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = itertools.groupby(people, get_state)
for key, group in person_group:
    print(key, len(list(group))) # as it is an iterator first cast into list
    # for person in group:
    #     print(person)
    # print()

## 10. tee()
## replicates the iterables
## after creating copies we can only use the copy and not the original iterator to avoid unintened exhaution 
copy1, copy2 = itertools.tee(person_group)
