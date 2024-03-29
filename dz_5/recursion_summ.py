# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
# Пример:
# sum(2, 2)
# # 4

a = 2
b = 2

def sum(a: int, b: int)->int:
    """
    Функция принимает на вход два целых положительных числа и выводит их сумму посредством 
    арифметических операций +1 и -1.
    """
    if a<1:
        return 0
    b += 1
    return b + sum(a-1,b)


    # if a < 1:
    #     a = 0
    # if b < 1:
    #     b = 0
    # print(a,b)
    # sum_numb = 0
    # if a == 0 or b == 0:
    #     return abs(a-b)
    # sum_numb += 1
    # sum_numb += 1
    # print(sum_numb)
    # return sum_numb+sum(a-1, b-1)

print(sum(a, b))