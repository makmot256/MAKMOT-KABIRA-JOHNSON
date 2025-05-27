# 1. Use the set() constructor to create a set of 3 of your favorite beverages
beverages = set(["coffee", "tea", "juice"])
print("1. Beverages set:", beverages)

# 2. Use the correct method to add 2 more items to the beverages set
beverages.add("water")   # Add one item
beverages.add("soda")    # Add another item
print("2. Beverages set after adding 2 items:", beverages)

# 3. Given the set below, check if "microwave" is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
is_microwave_present = "microwave" in mySet
print("3. Is 'microwave' present?", is_microwave_present)

# 4. Write a program to remove "kettle" from the set
mySet.remove("kettle")  # remove() will raise error if item not present
print("4. Set after removing 'kettle':", mySet)

# 5. Loop through the set and print each item
print("5. Looping through the set:")
for appliance in mySet:
    print(appliance)

# 6. Write a set of 4 items and a list of 2 items. Add elements in the list to the set
my_set = {"apple", "banana", "cherry", "date"}
my_list = ["elderberry", "fig"]
my_set.update(my_list)  # update() adds multiple elements
print("6. Set after adding list elements:", my_set)

# 7. Write two sets, one with ages and one with first names. Join the two sets
ages = {25, 30, 35}
first_names = {"Alice", "Bob", "Charlie"}
joined_set = ages.union(first_names)
print("7. Joined set (ages and first names):", joined_set)
