# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

d_num = int(input('Enter your number, please: '))
b_num = ''
while d_num > 0:
    b_num = str(d_num % 2) + b_num
    d_num = d_num // 2
print(b_num)