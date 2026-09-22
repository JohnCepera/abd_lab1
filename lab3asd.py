number = input("Введите число x: ")

if not number.strip() or number.count('.') > 1 or not number.replace('.', '', 1).isdigit():
    print("Ошибка: введите корректное число!")
else:
    x = float(number)
    
    if x < 1:
        print("Чисел нет, так как x меньше 1")
    else:
        res = []

        p3 = 1
        while p3 <= x:
            p5 = 1
            while p3 * p5 <= x:
                p7 = 1
                while p3 * p5 * p7 <= x:
                    res.append(p3 * p5 * p7)
                    p7 *= 7
                p5 *= 5
            p3 *= 3

        res.sort()
        print("Результат:", res)
