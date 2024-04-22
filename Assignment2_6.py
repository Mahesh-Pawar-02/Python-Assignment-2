# Problem Statement : Write a program which accept one number and display below pattern. 

def Pattern(No):
    for i in range(No,0,-1):
        print()
        for j in range(1, i+1):
            print("*", end = "  ")

def main():
    print("Enter number : ", end = " ")
    value = int(input())

    Pattern(value)

# Starter    
if __name__ == "__main__":
    main()

# Test case :
 
# Input : Enter number : 5
# Output :  *  *  *  *  *  
#           *  *  *  *  
#           *  *  *  
#           *  *  
#           *  