user_input = input("Введите число x: ")

# Убираем пробелы и проверяем, что в строке только цифры и максимум одна точка
if not user_input.strip() or user_input.count('.') > 1 or not user_input.replace('.', '', 1).isdigit():
    print("Ошибка: введите корректное число!")
else:
    x = float(user_input)
    
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
