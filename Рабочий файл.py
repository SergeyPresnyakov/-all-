def fact(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
    yield factorial


n = input("Введите число, факториал которого нужно посчитать: ")

for el in range(int(n) + 1):
    g = fact(el)
    print(f"Факториал {el} = {next(g)}")
