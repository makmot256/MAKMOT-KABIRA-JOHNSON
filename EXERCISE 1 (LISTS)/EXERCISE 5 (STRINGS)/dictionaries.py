# 1. Dictionary Shoes
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the value of shoe size
print("1. Shoe size:", Shoes["size"])

# 2. Change "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("2. Changed brand:", Shoes["brand"])

# 3. Add a key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("3. Dictionary after adding 'type':", Shoes)

# 4. Return a list of all keys
keys = list(Shoes.keys())
print("4. Keys in the dictionary:", keys)

# 5. Return a list of all values
values = list(Shoes.values())
print("5. Values in the dictionary:", values)

# 6. Check if the key "size" exists
has_size = "size" in Shoes
print("6. Does 'size' key exist?:", has_size)

# 7. Loop through the dictionary and print key:value
print("7. Looping through the dictionary:")
for key, value in Shoes.items():
    print(f"{key}: {value}")

# 8. Remove "color" from the dictionary
Shoes.pop("color", None)  # pop with default to avoid error if key doesn't exist
print("8. Dictionary after removing 'color':", Shoes)

# 9. Empty the dictionary
Shoes.clear()
print("9. Dictionary after emptying:", Shoes)

# 10. Create a dictionary and make a copy
my_dict = {"name": "Alice", "age": 25}
my_dict_copy = my_dict.copy()
print("10. Original dictionary:", my_dict)
print("10. Copy of dictionary:", my_dict_copy)

# 11. Nested dictionaries example
nested_dict = {
    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Jane", "age": 25}
}
print("11. Nested dictionary:")
for person, info in nested_dict.items():
    print(f"{person}:")
    for key, val in info.items():
        print(f"  {key}: {val}")
