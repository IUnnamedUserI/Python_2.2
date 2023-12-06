if __name__ == "__main__":
    x = int(input("Введите значение x: "))
    y = int(input("Введите значение y: "))

    if x / y == x // y:
        print(f"{x} делится на {y} целочисленно. {x} / {y} = {x / y}")
    else:
        print(f"{x} не делится на {y} целочисленно. {x} / {y} = {x / y}")
        