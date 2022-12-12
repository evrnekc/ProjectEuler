def is_prime(num):
    """ Check if the given number is prime """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    # check only odd numbers to make the algorithm more efficient
    # so that bigO is logn for while loop otherwise it would be n
    while i < num ** (1/2) + 1:
        if num % i == 0:
            return False
        i += 2
    return True

    
# Read the number of test cases
t = int(input().strip())
# Loop over the test cases
for a0 in range(t):
    # Read the given number
    n = int(input().strip())
    for i in range(1, n):
        # Since question ask largest prime we need to start from number itself to finds its prime factor
        # so algorithm will be faster
        # starting from number itself(as every number is factor of itself) we check if it is prime
        # if so we done.
        #  otherwise, check if it is divisible by 2 (possible largest factor) so check if it is prime
        # if so we done
        # otherwise check if it is ivisible by 3 (possible largest factor)....
        #
        # if (is_factor) and (is_prime)
        # since i starts from 1 we firs
        if n % i == 0 and is_prime(n/i):
            print(int(n/i))
            break