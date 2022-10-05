# Алогритм выясняющий является ли число простым числом
def isPrime(n):
    if n in {0, 1,}:
        return False
    if n == 2:
        return True
    if not (n % 2):
        return False
    for i in range(3, round(n **.5 + 1), 2):
        if not (n % i):
            return False
    return True
#Генератор простых чисел для оптимизации памяти
def primes_sieve2(n):
    a = [True] * n
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for k in range(i*i, n, i):
                a[k] = False
# Нахождение Эмирф связки в простых числах
def find_emirp(n):
    emirp_sum = 0
    emirp_max = 0
    emirp_count = 0
    if n < 13:
        return [0, 0, 0]
    for i in primes_sieve2(n):
        if i == int(str(i)[::-1]):
            continue
        if isPrime(int(str(i)[::-1])):
            emirp_max = i
            emirp_sum += i
            emirp_count += 1
    return [emirp_count, emirp_max, emirp_sum]