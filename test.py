def fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    try:
        n = int(input("Enter no of terms: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        print_fib_series(n)
        
