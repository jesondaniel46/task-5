input_string = "Guvi Geeks Network Private Limited"

# Convert the input string to lowercase to make it case-insensitive
input_string = input_string.lower()

# Initialize counts for each vowel
total_vowels = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Iterate through the string and count each vowel
for char in input_string:
    if char in "aeiou":
        total_vowels += 1
        if char == 'a':
            count_a += 1
        elif char == 'e':
            count_e += 1
        elif char == 'i':
            count_i += 1
        elif char == 'o':
            count_o += 1
        elif char == 'u':
            count_u += 1

# Display the results
print("Total number of vowels:", total_vowels)
print("Count of A:", count_a)
print("Count of E:", count_e)
print("Count of I:", count_i)
print("Count of O:", count_o)
print("Count of U:", count_u)
