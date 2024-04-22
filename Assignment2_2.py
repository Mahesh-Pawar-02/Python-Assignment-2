# Problem Statement : Write a program which accept one number and display below pattern.

def Pattern(No):
    for i in range(No):
        print()
        for j in range(No):
            print("*", end = "  ")

def main():
    print("Enter number : ", end = " ")
    value = int(input())

    Pattern(value)

# Starter    
if __name__ == "__main__":
    main()

# Test Cases : 
# Input : 5
# Output :   *  *  *  *  *  
#            *  *  *  *  *  
#            *  *  *  *  *  
#            *  *  *  *  *  
#            *  *  *  *  *