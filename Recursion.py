# test 1--sum the digits of a given number
def split(n):
    return n // 10, n % 10

def sum_digit(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digit(all_but_last) + last

result = sum_digit(2013)
print(result)



# test 2--do factorial quesiton
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

ans = factorial(10)
print(ans)
