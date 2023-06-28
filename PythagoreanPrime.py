# The Purpose of this program is to use:
# Pythagorean theorem to find a Prime number

# Prime function
def isPrime(n) :
    # Corner cases
    if(n <= 1) :
        return False
    if(n <= 3) :
        return True

    # Negate the middle five numbers to be skipped.
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if(n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

# Number 5, 13, 17,29,37,41,53,61,73,89, 97
n = 29

# Check if prime
if(isPrime(n) and (n % 4 == 1)):

    print("YES")
else:
    print("NO")

# Prime Range
def isPrimeRange(n):
    if(n <= 1):
        return False
    if(n <= 3):
        return True

    # Negate the middle five numbers
    if(n % 2 == 0 or n % 3 == 0):
        return False

    # number
    i = 5
    while(i * i <= n):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

# Check Primes
def checkPrimes(start, end):
    for i in range(start, end + 1):
        if(isPrime(i) and (i % 4 == 1)):
            print(i, end=" ")

# Check for a range of numbers
start = 1
end = 300
checkPrimes(start, end)


