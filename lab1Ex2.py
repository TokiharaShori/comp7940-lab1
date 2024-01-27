def print_factor(x):
    factors = []

    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)

    for factor in factors:
        print(factor)

print_factor(52633)
