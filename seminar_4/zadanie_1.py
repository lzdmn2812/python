# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
user_string = 'aaabcaadcdd'
list_ = user_string.split()

dict_count = {}
for i in range(len(list_)):
    if dict_count.get(list_[i]) is None:
        dict_count[list_[i]]=0
    else:
        dict_count[list_[i]] += 1
        list_[i] = f"({list_[i]}_{dict_count[list[i]]})"
print(dict_count)

print(list_)
print(" ".join(list_))