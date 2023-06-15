def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Enter the number of terms: "))
    fibonacci_sequence = []
    for i in range(n):
        fibonacci_sequence.append(fibonacci(i))

    print("The Fibonacci sequence is: ", fibonacci_sequence)

if __name__ == "__main__":
    main()