# File handling in python.


# File handling means Creating, Reading, Updating, 
# Deleting(CRUD) operations that we can perform in file Handling


# We have to use open() function to open a file in python.

# W - Writes or Overfides the text

p = open("File-Handling/example.txt",'w') 

p.write("Hello this is demo testing for write function")

p.close()

# a - Appends the text

p = open("File-Handling/example.txt",'a')

p.write("Appending the mode files append more items")

p.close()

# x - Just creates a new file

r = open("File-Handling/ex2.txt",'x')
r.close