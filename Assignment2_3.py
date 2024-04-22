# Problem Statement : Write a program which accept one number from user and return its factorial.

def Factorial(No):
    
    if (No < 0):
        print("Factorial does not exist..")
    elif No == 0:
        print("facorial is 1")
    else:
        Fact = 1
        for i in range(1, No+1):
            Fact = Fact * i
        return Fact

def main():
    print("Enter number : ", end = " ")
    value = int(input())

    Return = Factorial(value)

    print("Factorial is: ",Return)

# Starter    
if __name__ == "__main__":
    main()

# Test cases : 
# input : 5
# Output : 120