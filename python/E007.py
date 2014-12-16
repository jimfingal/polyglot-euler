import math

def infinite_range(start, step):
    current = start

    while True:
        yield current
        current += step

def is_prime(prime_array, num):
    num_sqrt = int(math.sqrt(num))
    
    for prime in prime_array:
        if prime > num_sqrt:
            break
        if num % prime == 0:
            return False

    return True


def n_primes(n):

    prime_array = [2]
    
    for num in infinite_range(3, 2):
        
        if is_prime(prime_array, num):
            prime_array.append(num)
            
        if len(prime_array) == n:
            return prime_array
    

def solution():
    primes = n_primes(10001)
    return primes[-1]