def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    for i in reversed(range(min_factor,max_factor)):
        for k in reversed(range(min_factor,max_factor)):
            if str(i*k)==str(i*k)[::-1]:
                m=(i*k,[i,k])
                break
        break
    return min_factor
    # return m,print('alfasdg')
largest(10,20)