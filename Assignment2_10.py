# Problem Statement : Write a program which accept number from user and return addition of digits in that number. 

def CountDigit(No):
    Sum = 0
    Digit = 0
    while No != 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    return Sum

def main():
    print("Enter number : ", end = " ")
    value = int(input())

    Return = CountDigit(value)

    print("Addition of Digit is: ",Return)

# Starter    
if __name__ == "__main__":
    main()

# Test Case :
 
# Input  : Enter number : 5187934
# Output : Addition of Digit is : 37