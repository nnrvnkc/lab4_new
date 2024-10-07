def factorial(n):
    if n < 0:
        raise ValueError("Факторіал не визначено для від'ємних чисел")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    while True:
        try:
            num = int(input("Введіть ціле число для обчислення факторіала: "))
            print(f"Факторіал числа {num} дорівнює {factorial(num)}")
        except ValueError as e:
            print(e)

        cont = input("Хочете обчислити ще один факторіал? (так/ні): ").strip().lower()
        if cont != 'так':
            print("Вихід з програми.")
            break

if __name__ == "__main__":
    main()
