# def convert_euro_to_cents(eurovalue):
#     centvalue = eurovalue * 100
#     print("The cent value for given euro is", centvalue)
#
# if __name__ == "__main__":
#     eurovalue = float(input("enter the euro value: "))
#     convert_euro_to_cents(eurovalue)
import random

# Create a list to store the range of values between 10 and 25, assign it to a variable called
# my_list.

my_list = list(range(10,25))

# Print the contents my_list
print(my_list)

# Print the contents of my_list in reverse using index slicing.
print(my_list[::-1])

# Print the contents of my_list in reverse using a loop.
for i in my_list[::-1]:
    print(i)

# Append the following list [11, 19, 26] to my_list. Note the difference between the extend
# and append methods.
othr_list = [11, 19, 26]
my_list.append(othr_list)
print(my_list)
my_list.extend(othr_list)
print(my_list)
# Append adds the list directly to the list at the end where we will have list inside list
# Extend add the objects inside the list to the list where we will have only one list


# Extend my_list with 10 random integers.
my_list.extend(random.sample(range(1, 101), 10))
print(my_list)

# Store the last number in the list in a variable called last_val and remove that value from
# my_list.

last_var = my_list[-1]
print(last_var)

my_list.remove(last_var)

print(my_list)


# Convert my_list to a set named my_set. Try to extract the second element in the set using
# indexing. Does it work? If not, why not?


"""
--------------------------------------------------
my_set = set(my_list)
print(my_set)
---------------------------------------------------
 - we cannot convert because firstly list allows duplicates and set doesnt
 - set cannot contain mutable elements 
 - if we want to convert first ourlist should have unique elements then we should convert to tuple then after that we 
        can convert into set
"""

my_list2 = [1,2,3,4]
my_tup = tuple(my_list2)
myset = set(my_tup)
print(myset)

# Convert my_list to a tuple named my_tuple. Assign the value 5 to the fourth element in the
# tuple? Does it work? If not, why not?
my_tup = tuple(my_list)
print(my_tup)

"""
my_tup[4] = 5
print(my_tup)
- No it doesnt work because tuple doesnt support item assignment
- Because it is immutable, once added cannot be changed
"""


"""
*************************************************************************************
Task 2 - Dictionaries
**************************************************************************************
"""

# Create an empty dictionary object called my_dict.
my_dict = {}

# Using a loop construct, add an entry to my_dict for each value in my_list. The keys for
# entries in my_dict should be the English-language representation of integer values in my_-
# list.
# Note: to convert numbers to their English-language representation, you will need to install
# a module named inflect. You can do this by adding the following code to a cell in your
# notebook:

print(my_list)
import inflect
del my_list[15]

def return_infelct_elements_for_list(my_list):
    my_dict = {}
    p = inflect.engine()

    for value in my_list:
        key = p.number_to_words(value)
        my_dict[key] = value

    return my_dict

print(return_infelct_elements_for_list(my_list))


"""
*************************************************************************************
Task 3 - Loops
**************************************************************************************
"""

# Without accessing one of the Python implementations available on the web, write a piece
# of code to generate the first 8 rows of Pascal’s triangle.

def create_pascal_triangle(row_count):
    print(f"*************************printing {row_count} rows pascal triangle ******************************** ")
    triangle = [[1]]

    for i in range(1, (row_count)):
        prev_row = triangle[-1]
        newrow = [1]

        for j in range(1, len(prev_row)):
            newrow.append(prev_row[j-1]+prev_row[j])

        newrow.append(1)
        triangle.append(newrow)
    return triangle


for i in (create_pascal_triangle(8)):
    print("\t".join(map(str, i)))

print("****************************completed***********************************")


"""
*************************************************************************************
Task 4 - Functions
**************************************************************************************
"""
# 2. Create a function that takes one argument, the length of a password to generate.
# 3. Your function should generate and return a password of the required length, ensuring that
# you use only characters with decimal values between 33 and 126 in the ASCII table . Note
# that some characters in the table are non-printing!


def password_generator(len_of_password):
    randomchars = [random.randint(33,126) for _ in range(len_of_password)]
    password=""
    for i in randomchars:
        password = password+chr(i)
    return password

print(password_generator(10))





