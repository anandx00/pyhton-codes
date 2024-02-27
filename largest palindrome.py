def palindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    return False
def largest(ran):
    for i in ( range(10,100)):
        for k in (range(10,100)):
            if palindrome(i*k)==True:
                return i,k ,i*k
        
largest([10,99])

