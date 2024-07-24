#question1 
# Define the div function
def div(a, b):
    return a / b

# Call the function and display the result
num1 = 10
num2 = 2
result = div(num1, num2)
print(f"The division of {num1} by {num2} is: {result}")
print("------------------------------------------------------------------")     
  #question2 
'''Declare a square() function with one parameter.Then call the function and pass
one number and display the square of that number .'''
def square(a):
    return a**2
num=2
result=square(num)
print("square",result)
print("-------------------------------------------------------------------------")

#question3
'''Using max() and min() functions display the maximum and minimum of 5 random
numbers.'''
import random

# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated random numbers
print("Generated random numbers:", random_numbers)

# Find and display the maximum and minimum of the random numbers
max_num = max(random_numbers)
min_num = min(random_numbers)

print("Maximum number:", max_num)
print("Minimum number:", min_num)
print("---------------------------------------------------------------")

#question4
'''Accept a name from the user and display that in lower case using lower()
function'''
# Accept a name from the user
name = input("Enter a name: ")

# Convert the name to lowercase using lower() function
lowercase_name = name.lower()

# Display the lowercase name
print(f"The name in lowercase is: {lowercase_name}")
print("--------------------------------------------------------------------")
#assingment part2
#question1
'''. Write a Python program to Count all letters, digits, and special
symbols from the given string
Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 2 Symbol = 3'''
def count_chars_digits_symbols(input_string):
    chars = 0
    digits = 0
    symbols = 0
    
    for char in input_string:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1
    
    return chars, digits, symbols

# Example usage:
input_string = "P@#yn26at^&i5ve"
chars, digits, symbols = count_chars_digits_symbols(input_string)

print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")

print("--------------------------------------------------------------------------------")
#question2
 '''
  Write a Python program to remove duplicate characters of a given
string.
Input = “String and String Function”
Output: String and Function'''
def remove_duplicates(input_string):
    seen = set()
    output = []
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            output.append(char)
    
    return ''.join(output)

# Example usage:
input_string = "String and String Function"
output_string = remove_duplicates(input_string)

print(f"Input: {input_string}")
print(f"Output: {output_string}")
print("----------------------------------------------------------------------------------------------")
#question3
'''3. Write a Python program to count Uppercase, Lowercase, special
character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
Output:
UpperCase : 5
LowerCase : 18
NumberCase : 5
SpecialCase : 11'''
def count_cases(input_string):
    upper_count = 0
    lower_count = 0
    number_count = 0
    special_count = 0
    
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            number_count += 1
        else:
            special_count += 1
    
    return upper_count, lower_count, number_count, special_count

# Example usage:
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper_count, lower_count, number_count, special_count = count_cases(input_string)

print(f"UpperCase : {upper_count}")
print(f"LowerCase : {lower_count}")
print(f"NumberCase : {number_count}")
print(f"SpecialCase : {special_count}")

print("---------------------------------------------------------------")
#question4
'''Write a Python Count vowels in a string
input= “Welcome to Python Assignment”
Output: Total vowels are: 8'''
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Example usage:
input_string = "Welcome to Python Assignment"
vowel_count = count_vowels(input_string)

print(f"Total vowels are: {vowel_count}")


