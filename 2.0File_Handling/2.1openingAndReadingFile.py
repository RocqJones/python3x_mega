# Open file. 'r' = read and 'w' = write.
file = open("example.txt",'r')
# set file to a variable to read it
content = file.read()
print(content)

# seek method
file.seek(0)
content = file.readlines()
print(content)

# Notes
# w+ -> Opens a file both write and read. Overwrites existing file if exists. 
# r+ -> Opens a file both read and write. The file pointer placed at the beggining of the file.
# a+ -> Opens a file both append and reading. The pointer is at the end of the file.