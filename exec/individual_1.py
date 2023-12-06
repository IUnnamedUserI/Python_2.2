if __name__ == "__main__":
    kg = int(input("Введите количество килограмм: "))
    pay = 0

    if kg < 0:
        print("Введено неправильное число")
        exit(1)

    if kg < 50:
        pay = kg * 30
    elif kg >= 50 and kg < 75:
        pay = kg * 50
    elif kg >= 75 and kg <= 90:
        pay = kg * 65
    elif kg > 90:
        pay = kg * 70 + 20

    print(f"Студент заработал {pay} копеек")
    