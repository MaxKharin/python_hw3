# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# num = int(input('Enter your number, please: '))
fib1 = fib2 = 1
num = 8
print(fib1, fib2, end=' ')
for i in range(2, num):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

lis = []
# lis = [1, 2, 3, 4]
# lis.reverse()
# for i in range(len(lis)):
#     lis[i] = lis[i] * -1
#     i += 1
# print(lis)