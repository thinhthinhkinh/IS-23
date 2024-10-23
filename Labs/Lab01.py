def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(n):
    # In số 1 trước
    print(1)
    for num in range(2, n + 1):
        if is_prime(num):
            print(num)

# Nhập vào số nguyên n
n = int(input("Nhập vào số nguyên dương n (n > 0): "))
if n > 0:
    print("Các số nguyên từ 1 đến", n, "là:")
    print_primes(n)
else:
    print("Vui lòng nhập số nguyên dương.")
