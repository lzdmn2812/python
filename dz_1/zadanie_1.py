# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# Пример:
# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

n = 123
n = str(n)
res = 0
# while n>0:
#     res=res+n%10
#     n=n/10
# print(res)
i=0
while i<3:
    res = res+int(n[i])
    i+=1
print(res)
