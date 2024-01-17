# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

my_list = [1, 2, 3, 4, 5]
new_list = []
k = int(input('Введите число: '))
for i in range(len(my_list)):
    pos = (i+k)%len(my_list)
    # while pos>=len(my_list):
    #     pos = abs(len(my_list)-pos)
    new_list.insert(pos, my_list[i])
print(new_list)




# lst = [1, 2, 3, 4, 5]
# lst_shifted = []
# sfifted = 3
# for i in range(len(lst)):
#     lst_shifted.append(lst[(i + sfifted) % len(lst)])
# print(lst_shifted)




# list_1 = [1, 2, 3, 4, 5]
# k = 4
# list_2 = list_1.copy()

# # решение 1
# for i in range(len(list_1)):
#     list_2[i] = list_1[(k+i-1)%len(list_1)]
# print(list_2)

# решение 2
# for i in range(k):
#     temp = list_1.pop()
#     list_1.insert(0, temp)
# print(list_1)

# решение 3
# print(list_1[-k:]+list_1[:-k])