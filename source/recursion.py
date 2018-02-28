#!python

def factorial(n):
    """ Returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n """
    if n < 0 or not isinstance(n, int):
        raise ValueError("FACTORIAL MULTIPLICATIVE RANGE IS UNDEFINED FOR n = {}".format(n))
    # return factorial_recursive(n)
    return factorial_iterative(n)



def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    if n == 0 or n == 1:
        return 1
    else:
        iterative_product = 1
        for iterator in range(1, n+1):
            iterative_product *= iterator
        return iterative_product

    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests


def factorial_recursive(n):
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
    #print(factorial_iterative(10))
