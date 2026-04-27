fruits_tuple = ("apple", "banana", "mango", "apple")

# length
print(len(fruits_tuple))

# count
print(fruits_tuple.count("apple"))

# index
print(fruits_tuple.index("banana"))
print("=============================================")

fruits_set = {"apple", "banana", "mango"}

# add
fruits_set.add("orange")

# remove
fruits_set.remove("banana")

# discard (safe remove)
fruits_set.discard("grape")

print(fruits_set)