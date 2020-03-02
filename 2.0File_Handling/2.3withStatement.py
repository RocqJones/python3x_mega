# 'with' statement helps you write file that closes without writting close() method

with open("write2.txt",'a+') as file:
    # part of with block
    file.seek(0)
    content = file.read()
    file.write("\nLine 5: With statement using 'a+'")