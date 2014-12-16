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

    prime_array = [2, 3]
    
    for num in xrange(3, max_num + 1, 2):
        if is_prime(prime_array, num):
            prime_array.append(num)
            
    return prime_array


def reverse_indexes(length):
    return xrange(length - 1, -1, -1)


def largest_prime_factor(primes, number):

    indexes = reverse_indexes(len(primes))

    for index in indexes:
        prime = primes[index]
        if number % prime == 0:
            return prime

    return None

def solution():

    test = 600851475143
    primes = primes_up_to(int(math.sqrt(test)))
    answer = largest_prime_factor(primes, test)
    return answer