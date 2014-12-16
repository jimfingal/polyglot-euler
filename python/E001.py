
def set_multiples_to_x(x, multiplier):
    return set(xrange(0, x, multiplier))

def solution():
    threes = set_multiples_to_x(1000, 3)
    fives = set_multiples_to_x(1000, 5)
    threes_and_fives = threes.union(fives)
    return sum(threes_and_fives)