def fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def print_fib_series(terms: int) -> None:
    if terms <= 0:
        print("Please enter a positive number of terms.")
        return
    series = [str(fib(i)) for i in range(terms)]
    print("Fibonacci series ({} terms):".format(terms))
    print(" ".join(series))

if __name__ == "__main__":
    try:
        n = int(input("Enter no of terms: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        print_fib_series(n)


#write few test cases
