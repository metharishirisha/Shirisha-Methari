def generate_odd_numbers(n):
    result = [2*i + 1 for i in range(n)]
    print("Output:", ", ".join(map(str, result)))

# Example
a = int(input("Enter a number: "))
generate_odd_numbers(a)
