fruits = ["apple", "banana", "mango"]

# append
fruits.append("orange")

# insert (position, value)
fruits.insert(1, "grape")

# remove (by value)
fruits.remove("banana")

# pop (removes last or index)
fruits.pop()          # removes last
fruits.pop(0)         # removes first

print(fruits)
print("=============================================")

fruits = ["apple", "banana", "mango", "apple", "lemons"]

# length
print(len(fruits)) 

# count occurrences
print(fruits.count("apple")) 

# sort ascending
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)

# reverse order (not sorting)
fruits.reverse()
print(fruits)