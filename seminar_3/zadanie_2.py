# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_1 = [1, 2, 3, 4, 5]
k = 3
list_2 = list_1.copy()

# решение 1
# for i in range(len(list_1)):
#     list_2[i] = list_1[(k+i-1)%len(list_1)]
# print(list_2)

# решение 2
# for i in range(k):
#     temp = list_1.pop(0)
#     list_1.append(temp)
# print(list_1)

# решение 3
# print(list_1[k:]+list_1[:k])