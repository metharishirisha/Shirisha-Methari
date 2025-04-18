def conditional_odd_series(n):
    limit = n if n % 2 != 0 else n - 1
    result = [i for i in range(1, limit + 1, 2)]
    print("Output:", ", ".join(map(str, result)))

# Example
a = int(input("Enter a number: "))
conditional_odd_series(a)
