
def divide(a,b):
    return a/b
def decorator(fuc):
    def fuct(a,b):
        if a>b:
            a,b=b,a
        return fuc(a,b)
    return fuct
k=decorator(divide)
print(k(4,2))
    