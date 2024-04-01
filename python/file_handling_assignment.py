filename = "my_file.txt"

firString = "Hello, I hope you are well."
secString = "Greetings from a universe far, far away."
nums = [3,2,1]
strings: list[str] = ["Philanthropy","Mustang","Sustainability"]

try:
    f = open(filename,"w")
except(PermissionError):
    print("Error opening file")
else:
    for i in nums:
        f.writelines(f'{i}\n')
    f.write(f'{firString}\n')
    f.write(f'{secString}\n')
finally:
    f.close()

try:
    f = open(filename,"r")
except(FileNotFoundError):
    print(f'File ./{filename} was not found')
else:
    while(line := f.readline()):
        print(line.rstrip())
finally:
    f.close()

try:
    f = open(filename,"a") 
except(PermissionError,FileNotFoundError):
    print(f'There were issues opening this file: ./{filename}')
else:
    for i in strings:
        f.writelines(f'{i}\n')
finally:
    f.close()
