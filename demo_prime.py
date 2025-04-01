def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter number: "))
    print(n, "is a prime number:", is_prime_number(n))

if __name__ == "__main__":
    main()
