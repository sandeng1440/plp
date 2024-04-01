f = open("file.txt",'x')

lines = ["First", "Second", "Third","Fourth"]
for i in lines:
    f.write(f'{i}\n')

f.close()

