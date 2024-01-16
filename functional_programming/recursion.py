def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))


n = 8
if n <= 0:
    print("enter a positive integer")
else:
    print("Fibonacci sequence:")
for i in range(n):
    print(fib(i))


def prime(i, n):
    if n == i:
        return 0
    else:
        if (n % i == 0):
            return 1
        else:
            return prime(i + 1, n)


n = 9
print("Prime Number are: ")
for i in range(2, n + 1):
    if (prime(2, i) == 0):
        print(i, end=" ")

# Prime Number are:
# 2 3 5 7
