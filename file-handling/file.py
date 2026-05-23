import os
# HOW TO READ FILE IN PYTHON
# file=open("./file-handling/data.txt","r")
lines=["Hello, Good Morning","\nHow are you Rahul ?" ,"\nAI is evolving "]
# with open("./file-handling/data.txt","r") as file:
    # print(file.read())
    # print(file.readlines())
    # file.writelines(lines)
    # file.seek(6)
    # print(file.read())
 
 
# HOW TO CREATE FILE IN PYTHON
# resume=open("./file-handling/resume.txt","w")

# open("./file-handling/data.txt","a","HELLO MIS")
# os.remove("./file-handling/resume.txt")
# if os.path.exists("./file-handling/data.txt"):
#     print("File EXISTS")
# else:
#     print("Not exists")


# STORE USER NOTE
note=input("Enter your note \n")
print(note)

# with open("note.txt","w") as file:
#     file.write(note)

# EXCEPTION HANDLING IN PYTHON

try:
    os.remove('note.tsx')
    # with open("note.tsx","w") as file:
    #     file.write(note)
except FileNotFoundError:
    print("File Does not exists")