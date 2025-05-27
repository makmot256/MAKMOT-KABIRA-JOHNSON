# 1. Consider the tuple below:
x = ("samsung", "iphone", "tecno", "redmi")

# Output your favorite phone brand (example: "iphone")
favorite_phone = "iphone"
print("1. My favorite phone brand is:", favorite_phone)

# 2. Use negative indexing to print the 2nd last item in your tuple.
second_last = x[-2]
print("2. The 2nd last item in the tuple is:", second_last)

# 3. Using the phones tuple above, update "iphone" to "itel"
# Tuples are immutable, so convert to list first, update, then convert back to tuple
phones_list = list(x)
index_iphone = phones_list.index("iphone")
phones_list[index_iphone] = "itel"
x = tuple(phones_list)
print("3. Updated tuple:", x)

# 4. Add "Huawei" to your tuple
# Again, tuples are immutable, so create a new tuple with the added element
x = x + ("Huawei",)
print("4. Tuple after adding 'Huawei':", x)

# 5. Loop through the tuple and print each item
print("5. Looping through the tuple:")
for phone in x:
    print(phone)

# 6. Remove/delete the first item in your tuple
# Create a new tuple excluding the first item
x = x[1:]
print("6. Tuple after removing the first item:", x)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda
cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu"])
print("7. Tuple of cities in Uganda:", cities)

# 8. Unpack your tuple (cities)
city1, city2, city3, city4 = cities
print("8. Unpacked cities:", city1, city2, city3, city4)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities
print("9. 2nd, 3rd and 4th cities:", cities[1:4])

# 10. Write two tuples, one with first names and one with second names, then join them
first_names = ("John", "Jane", "Alice")
second_names = ("Doe", "Smith", "Brown")
full_names = first_names + second_names
print("10. Joined tuples:", full_names)

# 11. Create a tuple of colors and multiply it by 3
colors = ("red", "green", "blue")
colors_multiplied = colors * 3
print("11. Colors tuple multiplied by 3:", colors_multiplied)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("12. Number of times 8 appears:", count_8)
