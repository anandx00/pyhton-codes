def sum_of_multiples(limit, multiples):
    m=[]
    for k in multiples:
        for i in range(limit+1):
            if i*k<limit:
                m.append(i*k)

    return sum(list(set(m)))
print(sum_of_multiples(20,[3,5]))