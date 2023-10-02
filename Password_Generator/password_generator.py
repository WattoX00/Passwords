'''
    Password Generator

    Author: WattoX00
    Date:   02/01/2023
'''

import random
num_password=int(input("How much password would you like to generate? "))
#generator
for _ in range(num_password):
    #variables
    password: str = str()
    count: int = int()
    length: int = random.randint(12,20)
    for i in range(length):
        #!special chracter off
        excluded_numbers = list(range(58, 68)) + list(range(91, 97))
        x = random.choice([i for i in range(48, 123) if i not in excluded_numbers])
        x: str =chr(x) #number to string
        password += x
    print("\n""The passwors is: ""\n"+str(password))