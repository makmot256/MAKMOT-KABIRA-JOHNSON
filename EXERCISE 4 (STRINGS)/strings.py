# 1. Declare two variables, an integer and a string, and concatenate them correctly
num = 42
text = " is the answer."
# Convert integer to string before concatenation
result = str(num) + text
print("1.", result)

# 2. Remove spaces at the beginning, middle, and end of the string
txt = "      Hello,       Uganda!       "
# Remove spaces at beginning and end using strip()
txt_stripped = txt.strip()
# Remove all spaces including in the middle using replace()
txt_no_spaces = txt_stripped.replace(" ", "")
print("2. Without spaces at beginning, middle, and end:", txt_no_spaces)

# 3. Convert txt to uppercase
txt_upper = txt.upper()
print("3. Uppercase:", txt_upper)

# 4. Replace character 'U' with 'V' in txt
txt_replaced = txt.replace("U", "V")
print("4. Replace 'U' with 'V':", txt_replaced)

# 5. Return a range of characters in 2nd, 3rd and 4th position of y
y = "I am proudly Ugandan"
# Indexing starts at 0, so 2nd, 3rd, 4th positions correspond to indexes 1,2,3
substring = y[1:4]
print("5. Characters in 2nd, 3rd and 4th positions:", substring)

# 6. Fix the syntax error in the string with quotes inside
# Original: x = “All “Data Scientists” are cool!” 
# Fix by using single quotes outside or escaping inner quotes
x = 'All "Data Scientists" are cool!'
print("6.", x)
