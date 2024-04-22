# Problem Statement : Write a program which accept one number for user and check whether number is prime or not.

def CheckPrime(No):
    Flag = False

    if No <= 0 or No == 1:
        return Flag
    
    for i in range(2,No):
        
        if (No % 2 == 0):
            return Flag           
        else:
            Flag = True
            return Flag

def main():
    print("Enter number : ", end = " ")
    value = int(input())

    bFlag = False

    bFlag = CheckPrime(value)

    if bFlag == False:
        print("is not a prime number")
    else:
        print("is a prime number")

# Starter    
if __name__ == "__main__":
    main()

# Test Cases : 

# Input  : Enter number : 5
# Output : is a prime number

# Input  : Enter number : -5
# Output : is not a prime number

# Input  : Enter number : 4
# Output : is not a prime number  
