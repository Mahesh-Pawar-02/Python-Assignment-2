# Problem Statement : Write a program which accept one number and display below pattern.

def Pattern(No):
    for i in range(No):
        print()
        for j in range(1,No+1):
            print(j, end = "  ")

def main():
    print("Enter number : ", end = " ")
    value = int(input())

    Pattern(value)

# Starter    
if __name__ == "__main__":
    main()

# Test Case :

# Input : Enter number : 5
# Output :  1  2  3  4  5  
#           1  2  3  4  5  
#           1  2  3  4  5  
#           1  2  3  4  5  
#           1  2  3  4  5  