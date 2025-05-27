# 1. Create a list with 5 names and output the 2nd item
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("1. Second item:", people[1])

# 2. Change the value of the first item
people[0] = "Alex"
print("2. After changing first item:", people)

# 3. Add a sixth item to the list
people.append("Frank")
print("3. After adding sixth item:", people)

# 4. Add "Bathel" as the 3rd item
people.insert(2, "Bathel")
print("4. After inserting 'Bathel' as 3rd item:", people)

# 5. Remove the 4th item from the list
people.pop(3)
print("5. After removing 4th item:", people)

# 6. Use negative indexing to print the last item
print("6. Last item (using negative indexing):", people[-1])

# 7. New list with 7 items; print 3rd, 4th and 5th items using range of indexes
new_list = ["a", "b", "c", "d", "e", "f", "g"]
print("7. 3rd, 4th, and 5th items:", new_list[2:5])

# 8. List of countries and make a copy
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print("8. Countries copy:", countries_copy)

# 9. Loop through the list of countries
print("9. Looping through countries:")
for country in countries:
    print(country)

# 10. List of animal names, sort ascending and descending
animals = ["lion", "tiger", "elephant", "zebra", "giraffe"]
animals.sort()
print("10. Animals sorted ascending:", animals)
animals.sort(reverse=True)
print("10. Animals sorted descending:", animals)

# 11. Output only animal names with letter 'a' in them
animals_with_a = [animal for animal in animals if 'a' in animal]
print("11. Animals with 'a':", animals_with_a)

# 12. Two lists (first names and second names), join them
first_names = ["John", "Jane", "Alice"]
second_names = ["Doe", "Smith", "Brown"]
full_names = first_names + second_names
print("12. Joined names:", full_names)
 