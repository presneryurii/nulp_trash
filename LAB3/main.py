print("LAB 3. Presner iurii")
print("Enter your numbers with a space, for example 1 2 3 4 5")
numlist = list(map(int, input().split()))


for a in numlist:
    for b in numlist:
        if a + b == 10:
            print(a , "+" ,b)