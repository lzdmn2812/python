# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов 
# слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных 
# на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 
# Output: 1 9
from random import randint 

arbuziki = int(input("Введите кол-во арбузов: "))
massa = [randint(1, 10) for i in range(arbuziki)]
print(massa)
# print(min(massa), max(massa))
min_massa, max_massa = massa[0], massa[0]

for elem in massa:
    if elem>max_massa:
        max_massa=elem
    elif elem<min_massa:
        min_massa=elem
        
print(min_massa, max_massa)