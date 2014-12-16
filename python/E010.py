import math

def is_prime(prime_array, num):
    num_sqrt = int(math.sqrt(num))
    
    for prime in prime_array:
        if prime > num_sqrt:
            break
        if num % prime == 0:
            return False

    return True

def primes_up_to(max_num):

    prime_array = [2]
    
    for num in xrange(3, max_num + 1, 2):
        if is_prime(prime_array, num):
            prime_array.append(num)
            
    return prime_array


def solution():
    primes = primes_up_to(2000000)
    return reduce(lambda x, y: x + y, primes, 0)
