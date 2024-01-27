x = 52633
a = []

for i in range(1, x+1):
    if x % i == 0:
        a.append(i)

print(a)
