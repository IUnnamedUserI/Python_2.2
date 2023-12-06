if __name__ == "__main__":
    n = int(input("Введите значение N: "))

    print(f"Натуральные делители {n}:")

    for k in range(1, n):
        if n / k == n // k:
            print(f"{n} / {k} = {n // k}")
            k += 1
