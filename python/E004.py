def palindrome_gen(max_half):
    for half in xrange(max_half, 0, -1):
        half_str = str(half)
        palindrome = int(half_str + half_str[::-1])
        yield palindrome
    
def get_largest_palindrome(max_palindrome_half, digits):
    
    max_factor = int("9" * digits)
    min_factor = 10 ** (digits-1)
    
    for palindrome in palindrome_gen(max_palindrome_half):
        for factor in xrange(max_factor, min_factor, -1):
            if palindrome % factor == 0:
                other_factor = palindrome / factor
                if other_factor > min_factor and other_factor < max_factor:
                    return palindrome


def solution():
    return get_largest_palindrome(997, 3)
