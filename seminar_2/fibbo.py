# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# A = int(input())
# pre = 1
# recent = 2
# temp = pre
# i = 4
# while recent <= A:
#     if recent == A:
#         print(f'Номер числа Фибоначчи: {i}')
#         break
#     temp = pre
#     pre = recent
#     recent = recent + temp 
#     i+=1
# else:
#     print(f'Номер числа Фибоначчи: {-1}')

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377

# МОЕ
A = int(input("Введите число: "))
firstNumber = 0
secondNumber = 1
summ=0

i = 2
while summ <= A:
    if summ==A:
        print("")
        print(f"Номер числа Фибоначчи: {i}")
        break
    summ=firstNumber+secondNumber
    firstNumber=secondNumber
    secondNumber=summ
    i+=1
    print(summ)
else:
    print("")
    print(" -1")


# number_a = int(input('Enter a number: '))
# fib_number, fib_number_one = 0, 1
# counter = 3
# while fib_number + fib_number_one < number_a:
#     fib_number, fib_number_one = fib_number_one, fib_number + fib_number_one
#     counter += 1
# if number_a == 0:
#     print(1)
# elif number_a == 1:
#     print('It can be either 2 or 3')
# elif fib_number + fib_number_one == number_a:
#     print(counter)
# else:
#     print(-1)