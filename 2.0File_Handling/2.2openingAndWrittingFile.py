# if a file does not exist open() methode creates it.
file = open("write1.txt",'w')
# write a string
file.write("Line 1: Hey there\n")
file.write("Line 2: I love py")
file.close()

# Another file with loops and lists.
file = open("write2.txt",'w')
l = ["Line 1", "Line 2", "Line 3"]
for items in l:
    file.write(items+"\n")

file.close()

# append
file = open("write2.txt",'a')
file.write("Line 4: I've appended this")
file.close()