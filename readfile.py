""" Python codes to read file saved as readthis.txt  """ 

example = 'readthis.txt'
# To open a text file, use this command to store an object file_data of class open
file_data = open(example , 'r')

# Now you can use this to know the file name and file mode
print("The file name is ", file_data.name)
print("The file mode is ", file_data.mode)

""" Use the read() method to read the file object as a string. """
file_content_string = file_data.read()
print(file_content_string)

""" Use the readlines() method to read the file object as a list. """
# Remember to comment out the read() method before using this method.
# file_content_list = file_data.readlines()
# print(file_content_list)

# Use this to read only a single line from the text
# file_content_line = file_data.readline()
# print (file_content_line)

# print(file_data.closed)
file_data.close()
# print(file_data.closed)

""" A better way to open files using with command. This automatically closes the file after reading"""
with open(example , 'r') as file_new:
    file_content = file_new.read()
#   print(file_content)
#   print(file_new.closed)
    
# print(file_new.closed)
print(file_content)

# Read first four characters

with open(example, "r") as file1:
    print(file1.read(4))

""" Once the method .read(4) is called the first 4 characters are called.
If we call the method again, the next 4 characters are called and so on """

with open(example, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
    

    






