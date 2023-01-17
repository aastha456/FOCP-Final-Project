#FOCP TASK 1
import random

#making list of fruits, colors and animals
FRUITS=['orange','apple','banana','pineapple','kiwi','strawberry','avocado']
COLORS=['red','pink','blue','black','peach','green','yellow']
ANIMALS=['dog','cat','monkey','zebra','camel','squirrel','rabbit']

print("Password Generator")
print("===================")
print("\n")

#condition to put valid integer
while True:
    try:
       no_pwd=int(input("How many passwords are needed?"))
       break
    except ValueError:
        print("Please enter a number.")
        

#condition to print passwords between 1 and 24 
if no_pwd in range(1,25):
    for i in range(no_pwd):
        password = random.choice(FRUITS) + random.choice(COLORS) + random.choice(ANIMALS)
        print('{} --> {}'.format(i + 1, password))
    
else:
    print("The value should be between 1 and 24.")




 
