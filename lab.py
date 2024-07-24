
#1)Declare a div() function with two parameters. Then call the function and pass two
#numbers and display their division
def div( n1, n2):
    if(n2==0):
        return "division is not possible"
    else:
        return n1/n2;
result=div(10,2)
print("division of 10 & 2 is",result)

# 2)Declare a square() function with one parameter.Then call the function and pass
#one number and display the square of that numbe

def square(num):
    return num*num
result=square(4)
print("sqaure of number is",result)

#3)Using max() and min() functions display the maximum and minimum of 5 random
#numbers.
import random

# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the random numbers
print("Random numbers:", random_numbers)

# Find the maximum and minimum values
max_value = max(random_numbers)
min_value = min(random_numbers)

# Display the maximum and minimum values
print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")

#4) Accept a name from the user and display that in lower case using lower()function
string=input("enter the name")
string2=string.lower()
print(string2)

