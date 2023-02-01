import os

with open('test.txt', 'r') as file:
    context = file.read()

    filter__ = context.replace('з', 'Z')
    my_file = open("createfile.txt", "w+")
    my_file.close()
with open('createfile.txt', 'w') as file:
    file.write(filter__)

fileCreate = 'createfile.txt'
with open('createfile.txt', 'r') as file:
    print(file.read())

os.remove(fileCreate)