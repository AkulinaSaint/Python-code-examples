# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степерь 2, и выводим 4
x = -1
while not 0 < x < 10:
    x = int(input('Введите число: '))
    if not 0 < x < 10:
        print('Можно ввести число только от 0 до 10. Попробуйте снова.')
    else:
        print('Введеное число в степени 2:', x**2)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
x = int(input('Введите первое значение: '))
y = int(input('Введите второе значение: '))
x = x + y
y = x - y
x = x - y

print(x)
print(y)
