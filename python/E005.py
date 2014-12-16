def all_factors_divide(number, factors):
    for factor in factors:
        if number % factor != 0:
            return False
    return True


def get_solution_six(highest):
    current = highest
    factors = range(highest - 1, 0, -1)
    while True:
        if all_factors_divide(current, factors):
            return current
        else:
            current += highest

def solution():
    highest = 20
    current = highest
    factors = range(highest - 1, 0, -1)
    while True:
        if all_factors_divide(current, factors):
            return current
        else:
            current += highest
