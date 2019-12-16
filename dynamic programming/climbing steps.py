def climbing_steps():
    cache = {}

    def helper(n):
        if n in cache.keys():
            return cache.get(n)
        if n < 2:
            return 1
        else:
            cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
    return helper


if __name__ == "__main__":
    res = climbing_steps()
    print(res(5))
