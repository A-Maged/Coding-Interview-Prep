# 0 1 1 2 3 5 8 13
def fib(n, memo={}):
    if n in memo:  # is cached
        return memo[n]
    elif n < 1:  # base case
        return 0
    elif n <= 2:  # base case
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(50))
