def sum_to_n():
    n = int(input("Enter a number: "))
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    print(total)

sum_to_n()