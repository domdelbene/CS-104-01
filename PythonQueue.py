
print("Type 10 names into the bank: ")
names = []
for x in range(10):
    name = input("Enter name: ")
    names.append(name)
print(names)

input("Hit 'Enter' to pop the names out of the bank. ")
for x in range(len(names)):
    print(names.pop(0))
print(names)
    
    


    
