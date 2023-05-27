class Math:
    def __init__(self, n):
        self.n = n

    def fact(n):
        if n == 0:
            return 1
        else:
            return n * Math.fact(n-1)


n = 10
factorial = Math.fact(n)
print(factorial)


