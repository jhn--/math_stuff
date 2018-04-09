def get_pf(num):
    """
    get prime factors of a number.
    pf = prime factors
    pm = prime numbers
    ""'
    pm = [2,3,5,7,11,13,17,19]
    pf = []
    if num == 1 or num in pm:
        pf.append(num)
        return pf
    while num != 1:
        print(num)
        for i in pm:
            if num % i == 0:
                pf.append(i)
                num = num / i
    return sorted(pf)

print(get_pf(100))
print(get_pf(504))
