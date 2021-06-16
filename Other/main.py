def dig_pow(n, p):
    n_list = list(str(n))
    N = sum([int(n_list[i - p]) ** i for i in range(p, len(n_list) + p)])
    if N % n == 0:
        return N // n
    else:
        return -1


print(dig_pow(46288, 3))