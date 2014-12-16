def solution_fancy(n):
    def sum_squares_to_n(n):
        return reduce(lambda x, y: x + y ** 2, xrange(1, n + 1), 0)
        
    def square_of_sums_to_n(n):
        return reduce(lambda x, y: x + y, xrange(1, n + 1), 0) ** 2

    return square_of_sums_to_n(n) - sum_squares_to_n(n)


def solution():

    n = 100

    sum_square = 0
    square_sum_add = 0
 
    for num in xrange(1, n + 1):
        sum_square = sum_square + num * num
        square_sum_add += num

    return square_sum_add * square_sum_add - sum_square
