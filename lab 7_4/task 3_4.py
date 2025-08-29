with open("numbers.txt", "r") as f:
    squares = [
        int(n.strip()) ** 2
        for n in f
        if n.strip().isdigit()
    ]

with open("squares.txt", "w") as f2:
    f2.writelines(f"{sq}\n" for sq in squares)

print("squares written")