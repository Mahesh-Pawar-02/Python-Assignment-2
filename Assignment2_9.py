# Problem Statement : Write a program which accept number from user and return number of digits in that number. 

def CountDigit(No):
    Cnt = 0
    while No != 0:
        No = No // 10
        Cnt = Cnt + 1
    return Cnt

def main():
    print("Enter number : ", end = " ")
    value = int(input())

    Return = CountDigit(value)

    print("Number of Digit is: ",Return)

# Starter    
if __name__ == "__main__":
    main()

# Test case : 

# Input  : Enter number : 5187934
# Output : Number of Digit is : 7