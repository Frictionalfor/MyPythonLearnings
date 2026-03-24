file = open("file.txt", "w")
file.write("This is a file handling program in Python") 
file.close()  

file = open("file.txt", "r") 
content = file.read() 
variable = "content"
print(content) 
file.close() 

with open("file.txt", "w") as file:
    file.write("This is a file handling program in Python")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)  

import os
os.remove("file.txt")  