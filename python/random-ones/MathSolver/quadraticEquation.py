def quadEquation(a, b, c):
    first, second = 1, 1
    first = (-b + (b * b - 4 * (a * c)) ** (1 / 2)) / 2 * a
    second = (-b - (b * b - 4 * (a * c)) ** (1 / 2)) / 2 * a

    return (first, second)


a = float(input("Value of A: "))
b = float(input("Value of B: "))
c = float(input("Value of C: "))

print(quadEquation(a, b, c))
