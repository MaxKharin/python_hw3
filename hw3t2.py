# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lis = [2, 3, 4, 5, 6]
m_lis = []
for i in range((len(lis) + 1) // 2):
    m_lis.append(lis[i] * lis[len(lis) - 1 - i])
print(m_lis)