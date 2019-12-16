
cal = 0
cal2 = 0
cal3 = 0


def fibonacci(n):
    global cal
    cal = cal+1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_memoization():
    cache = {}

    def fib(n):
        global cal2
        global cal3
        if n in cache.keys():
            cal3+=1
            return cache.get(n)
        cal2 += 1
        if n < 2:
            return n
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib


if __name__ == "__main__":
    print(fibonacci(7))
    print("cal ", cal)
    print("After")
    print(fibonacci_memoization()(7))
    print(cal2)
    print(cal3)
