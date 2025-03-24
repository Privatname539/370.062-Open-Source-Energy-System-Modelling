# This program will check if a given number is a prime number

n = int(input("Enter number: "))            # Enter number to be checked

is_prime = True                             # Define flag for prime and set it to True

if n <= 0:                                  # Check if number is negative, 0 or 1
    is_prime = False                        # Set flag to false because negative numbers, 0 and 1 are not prime numbers
else:
    for i in range(2, n):                   # For-loop with index i from 2 to n
        if (n % i) == 0:                    # Check if n modulo i returns 0 as remainder
            is_prime = False                # Set flag to false because the number can be divided without remainder 
            break                           # - therefore not a prime number

print(n, "is a prime number:", is_prime)    # Return result of checking if number is prime or not