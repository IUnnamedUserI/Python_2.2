import math


if __name__ == "__main__":
    x = int(input("Введите значение x: "))
    EULER = 0.5772156649015328606
    Chix, n = 0, 1
    
    while True:
        temp = ((-1) ** n * x ** (2 * n)) / ((2 * n) * math.factorial(2 * n))
        if abs(Chix) < 1e-10:
            break
        
        Chix += temp
        n += 1

    print(f"Chi(x) = {EULER + math.log10(x) + Chix}")