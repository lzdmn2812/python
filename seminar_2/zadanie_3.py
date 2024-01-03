
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная 
# оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою 
# очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней 
# длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура
# ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих 
# строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа 
# и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10 
# Output: 2

N = int(input("Введите количество дней: "))
temperatures = []

for i in range(N):
    temperatures.append(int(input("Введите температуру: ")))

count = 0
max_count = 0
i = 0
while i<len(temperatures):
    if temperatures[i]>0:
        count+=1
    else: 
        if max_count<count:
            max_count=count
        count = 0
    i+=1
if max_count<count:
    max_count=count    
print(max_count)
        


# import random

# usernum = int(input("Please input your amount of days: "))
# count = 0
# max_count = 0

# for _ in range(usernum):
#     daytemp = random.randint(-50, 50)
#     print(daytemp, end=', ')

#     if daytemp>0:
#         count+=1
#         if max_count<count:
#             max_count=count
#     else:
#         count=0
# print()
# print(max_count)

# temps = [random.randint(-50, 50) for i in range(int(input("Enter the amount of days: ")))]
# max, count = 0, 0
#
# for day in temps:
#     if day > 0:
#         count += 1
#     else:
#         if max < count:
#             max = count
#         count = 0
#
# if max < count:
#     max = count
# print(temps, '\n', max)