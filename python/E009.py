

def is_triplet(a, b, c):
    return a**2 + b**2 == c**2 and a < b < c

def return_triplet_with_sum(num):
    min_c = int(num / 3)    
    
    for c in xrange(min_c, num):
        for b in xrange(c - 1, 0, -1):
            for a in xrange(b - 1, 0, -1):
                sum_nums = a + b + c
                    
                if sum_nums == 1000 and is_triplet(a, b, c):
                    return a, b, c

                if sum_nums < 1000:
                    continue

def solution():
    triplet = return_triplet_with_sum(1000)
    return reduce(lambda x, y: x*y, triplet, 1)