# Problem Statement : Write a program which accept one number form user and return addition of its factors.
 
def SumFactor(No):
    Sum = 0
    for i in range(1,No):
        if (No % i == 0):
            Sum = Sum + i
    return Sum

def main():
    print("Enter number : ", end = " ")
    value = int(input())

    Return = SumFactor(value)

    print("Addition of Factors is: ",Return)

# Starter    
if __name__ == "__main__":
    main()

# Test Case : 

# Input  : 12
# Output : 16