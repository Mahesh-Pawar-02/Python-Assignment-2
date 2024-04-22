# Problem Statement : Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() 
# for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program 
# which call all the functions from Arithmetic module by accepting the parameters from user.  

import Arithmetic as Arithmetic

def main():
    print("Enter first number : ", end = " ")
    value1 = int(input())

    print("Enter second number : ", end = " ")
    value2 = int(input())

    Return1 = Arithmetic.Add(value1, value2)
    Return2 = Arithmetic.Sub(value1, value2)
    Return3 = Arithmetic.Mult(value1, value2)
    Return4 = Arithmetic.Div(value1, value2)

    print("Addition is : ",Return1)
    print("Substraction is : ",Return2)

    print("Multiplication is : ",Return3)
    print("Division is : ",Return4)

# Starter    
if __name__ == "__main__":
    main()

# Test Case: 

# Input : Enter first number : 11
# Input : Enter first number : 21

# Output : Addition is : 32
#          Substraction is : -10 
#          Multiplication is : 231
#          Division is : 0.5238095......