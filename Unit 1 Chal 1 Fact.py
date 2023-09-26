# Python 3 program to find 
# factorial of given number
  
# Function to find factorial of given number
def factorial(n):
    if(n == 0):
       return 1
    i = n
    fact = 1
      
    while(n / i != n):
        fact = fact * i
        i -= 1
          
    return fact
  
# Driver Code
num = 5;
print("Factorial of", num, "is",
factorial(num))