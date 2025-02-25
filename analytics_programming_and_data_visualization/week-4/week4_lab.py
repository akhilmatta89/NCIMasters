import re

import numpy as np

# # Create a text file and manually add some data to the file
# def create_a_text_file(filename, createmode):
#     file = None
#     try:
#         file = open(filename, createmode)
#         return "file opened successfully"
#     except Exception as ex:
#         print("some error occurred")
#         return ex
#     finally:
#         file.close()
#
#
# def write_content_into_file(filename, content):
#     file = None
#     try:
#         file = open(filename, "a")
#         file.write(content)
#         return "file has been written with some data"
#     except Exception as ex:
#         return ex
#     finally:
#         file.close()
#
#
# # Note: Will fail if you run multiple files without deleting file
# print(create_a_text_file("samplefile.txt", "x"))
# print(write_content_into_file("samplefile.txt", "This is line 1\n"))
# print(write_content_into_file("samplefile.txt", "This is line 2\n"))
#
#
# # Write Python code to
# # • open the file for write only access
# # • attempt to read the contents of the file
#
# def open_file_in_write_mode_and_write_some_content(filename):
#     try:
#         with open(filename, "w") as f:
#             f.write(f"Hello All iam inside file {filename}")
#             f.close()
#             return "file has been written in write mode with some data"
#     except Exception as ex:
#         print("some error occurred")
#         return ex
#
#
# def read_the_content_from_the_file(filename):
#     try:
#         with open(filename, "w") as f:
#             f.read()  # Returns UnsupportedOperation
#     except Exception as ex:
#         print(f"some error occurred with exception {type(ex).__name__} - {ex}")
#         return ex
#
#
# print(open_file_in_write_mode_and_write_some_content("samplefile_2.txt"))
# print(read_the_content_from_the_file("samplefile_2.txt"))
#
#
# # Modify your code to
# # • use a try / except / finally construct that will catch the exception, print a
# # user-friendly error message, and clean up the file resource
#
# def read_file_print_error_if_any(filename):
#     try:
#         with open(filename, "w") as f:
#             f.read()  # Returns UnsupportedOperation
#     except Exception as ex:
#         print(f"some error occurred while reading content from mode where file is in write mode "
#               f"with exception {type(ex).__name__} - {ex}")
#         f.close()
#
#
# read_file_print_error_if_any("samplefile_2.txt")
#
#
# # Investigate how you would create your own Exception class. Then createyour
# # own Exception class and use it in your code from the previous exercise.
#
# class MyOwnException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
#
# def checkMyOwnException(filename):
#     try:
#         with open(filename, "w") as f:
#             f.read()  # Returns UnsupportedOperation
#     except Exception as ex:
#         f.close()
#         raise MyOwnException("some error occurred while reading content")
#
#
# try:
#     print(checkMyOwnException("samplefile_2.txt"))
# except MyOwnException as ex:
#     print(f"some error occured {type(ex).__name__} - {ex}")
#
#
# # Sometimes we have to define explicit exceptions to indicate that something goes
# # wrong. Use a combination of built in and user-defined exceptions to effectively
# # support and provide feedback for the following statements
#
# class NotEvenException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
#
# class NotInRangeException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
#
# def check_even_or_not(a, b):
#     if a % 2 != 0 or b % 2 != 0:
#         raise NotEvenException("This is not even number")
#
#
# def range_btw_0_and_10(a, b):
#     if a not in range(0,11) or b not in range(0,11):
#         raise NotInRangeException("Not in range of 0 and 10")
#
#
# def userdefined_and_builtin_function():
#     try:
#         a = int(input("enter A value in between [0 to 10]\n"))
#         b = int(input("enter B value in between [0 to 10]\n"))
#         range_btw_0_and_10(a, b)
#         check_even_or_not(a, b)
#
#         print(a / b)
#
#     except NotEvenException as ne:
#         print("entered value is not even number", ne)
#     except NotInRangeException as nir:
#         print("Not in specified range", nir)
#     except ZeroDivisionError as ze:
#         print("zero is not divisble", ze)
#     except Exception as ex:
#         print(ex)
#
# userdefined_and_builtin_function()

"""***************************************************************************************************************"""
# Create an array with the arrange function and reshape the array as follows:
# b = arange(24).reshape(2,3,4)

myarr = np.arange(24).reshape(2, 3, 4)
print(myarr)
# Using indexing and slicing perform the following tasks:
# i) Choose the first set of 3 rows and 4 columns of data
# ii) Choose the second row of data from the second set of 3 rows of data
# iii) Choose all the data from the second column for both the first and second
# sets of rows and columns of data
print("@@@@@@@@@@@@@@@@@@@@@@@@")
print(myarr[0][0:])
print("@@@@@@@@@@@@@@@@@@@@@@@@")
print(myarr[1][1])
print("@@@@@@@@@@@@@@@@@@@@@@@@")
# print(myarr[0:],1)
print(myarr[:, :, 1])

# Use the ravel function to flatten the data. What’s the difference between ravel
# and flatten?
print("@@@@@@@@@@@@@@@@@@@@@@@@")
print(myarr.ravel())
print(myarr)
"""differe between ravel and flatten 
- with ravel we can effect the original copy by flattening it or we can create a seperate copy
- with flatten separate copy will be created"""
print("@@@@@@@@@@@@@@@@@@@@@@@@")
myarr2 = np.arange(24).reshape(2, 3, 4)
print(myarr2.flatten())
print(myarr2)
print("@@@@@@@@@@@@@@@@@@@@@@@@")

# Reshape the data so that there are 6 rows of 4 columns per row.
newarr = myarr.reshape(6, 4)
print(newarr)
print("@@@@@@@@@@@@@@@@@@@@@@@@")
# Get the transpose of the new data structure.
print(newarr.transpose())
print("@@@@@@@@@@@@@@@@@@@@@@@@")
# Restack the rows of the transposed data structure in reverse order (hint: look at
# the row_stack function).
# Note row stack is deprecated so we can use vstack
restacked = np.vstack(newarr)
print(restacked)
print("@@@@@@@@@@@@@@@@@@@@@@@@")

# Split the resulting data structure horizontally (hint: look at the hsplit function).
h_split_data = np.hsplit(restacked, 2)
print(h_split_data)
print("@@@@@@@@@@@@@@@@@@@@@@@@")
"""***************************************************************************************************************"""
# Use the loadtxt command to load data from AAPL.csv from columns 5 and 7 (i.e.,
# the close price and the volume).
npframe = np.loadtxt(
    "/Users/akhilmatta/Desktop/NCI/NCIMasters/analytics_programming_and_data_visualization/week-4/data_for_tutorials/AAPL.csv",
    delimiter=",", usecols=[4, 6], skiprows=1)
print(npframe)

# Based on the data provided, calculate the volume weighted average price for the
# stock (i.e., calculate the average price using the volume as weight values).
print(np.average(npframe,axis=0)[1])

mean_columns = np.mean(npframe, axis=0)
print(mean_columns[1])

# Calculate the median value of the closing prices (hint: use the median function).
mean_columns = np.median(npframe, axis=0)
print(mean_columns[0])

# Calculate the variance value of the closing prices.
var_val = np.var(npframe, axis=0)
print(var_val[0])

# Again, use the loadtxt command to load data from columns 3 and 4 (i.e., the high
# prices and the low prices).

npframe2 = np.loadtxt("/Users/akhilmatta/Desktop/NCI/NCIMasters/analytics_programming_and_data_visualization/week-4/data_for_tutorials/AAPL.csv",
   delimiter=",", usecols=[2,3],skiprows=1)
print(npframe2)

# Use the max and min functions to get the highest high and the lowest low value.
# Compute column-wise means (axis=0 for column-wise operation)
max_column_2 = np.max(npframe2[:, 0])  # Mean of the first column (2nd in the file)
min_column_3 = np.min(npframe2[:, 1])  # Mean of the second column (3rd in the file)

print("high highest value: ", max_column_2)
print("low lowest value: ", min_column_3)

# Load data from column 5 of AAPL.csv. Also, load data from column 5 of MSFT.csv
aapl_col_5_data = np.loadtxt("/Users/akhilmatta/Desktop/NCI/NCIMasters/analytics_programming_and_data_visualization/week-4/data_for_tutorials/AAPL.csv",
   delimiter=",", usecols=[4],skiprows=1)
msft_col_5_data = np.loadtxt("/Users/akhilmatta/Desktop/NCI/NCIMasters/analytics_programming_and_data_visualization/week-4/data_for_tutorials/MSFT.csv",
   delimiter=",", usecols=[4],skiprows=1)

# Calculate the covariance matrix of the closing prices of AAPL and MSFT (hint: use
# the cov function)
cov_matrix = np.cov(aapl_col_5_data, msft_col_5_data)

# Extract diagonal values (variances)
diagonal_values = np.diagonal(cov_matrix)

# Display the diagonal values
print("Diagonal Values (Variances):")
print(diagonal_values)

# Calculate the correlation coefficient of the closing prices of AAPL and MSFT (hint:
# corrcoef).

corrcoeff = np.corrcoef(aapl_col_5_data, msft_col_5_data)
print(corrcoeff)

"""***************************************************************************************************************"""
# Write Python program to search the numbers (0-9) of length between 1 to 3 in
# a given string.

def match_numbers_of_length_btwn_1_3(text):
    pattern = r'\b[0-9]{1,3}\b' # we can also use r'\b\d{1,3}\b'
    return re.findall(pattern,text)

print(match_numbers_of_length_btwn_1_3("iam akhil with age 29, and have 161 cms "
                                       "height and spent 44500 minutes in studying will do it every 1 week"))

# Write a Python program to remove leading zeros from an IP address
def remove_leading_zeros_from_ip_address(ip):
    #172.16.254.1
    pattern = r'\b[1-9]{1,3}.[1-9]{1,3}.[1-9]{1,3}.[1-9]{1,3}\b'
    return re.findall(pattern, ip)

print(remove_leading_zeros_from_ip_address("192.168.01.1"))
