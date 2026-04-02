# 팩토리얼 == 1부터 어떤 양의 정수 n까지를 모두 곱한 것

# 5 * factorial(4)
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * (factorial(1) == 1)

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(1000))