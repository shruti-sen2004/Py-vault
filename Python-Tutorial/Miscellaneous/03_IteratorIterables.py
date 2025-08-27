## iterable - can be iterated over for loop, has __iter__ method
## iterator - an object that remembers its stage during iteration also knows how to get its next value
## iterator can go forever without an end value but it always fetch one next value each iteration

nums = [1,2,3] # iterable-has __iter__, not iterable - lacks __next__
print(dir(nums))

i_nums = iter(nums) # same as nums.__iter___()
print(dir(i_nums)) # iterators are also iterables
print(next(i_nums))  
print(next(i_nums)) # remembers its stage hence prints the next element

# working of for loop but only moving forward
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

## class that behaves like in-buit range function
class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current    
nums = MyRange(1,10)
for num in nums:
    print(num)

def my_range(start,end): # generator - more readable
    current = start
    while current < end:
        yield current
        current += 1
nums = MyRange(1,10)
for num in nums:
    print(num)