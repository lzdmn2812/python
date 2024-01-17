# # Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
input_str = "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells"
input_str = input_str.replace('.', ' ')
input_list = input_str.split()
print(input_list)
for i in range(len(input_list)):
    input_list[i] = input_list[i].lower()
print(input_list)
print(len(set(input_list)))