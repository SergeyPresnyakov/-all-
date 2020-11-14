"""Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""
my_list = []
while True:
    el = input("Введите элемент (число, слово, символ и т.п.) или завершите ввод, написав слово 'Ok': ")
    if el == str("Ok"):
        break
    else:
        my_list.append(el)
        continue
print("Исходный список:    ", my_list)

if len(my_list) % 2 == 0:
    for num_el in range(len(my_list)):
        if num_el % 2 == 0:
            my_list[num_el], my_list[num_el + 1] = my_list[num_el + 1], my_list[num_el]

else:
    for num_el in range(len(my_list) - 1):
        if num_el % 2 == 0:
            my_list[num_el], my_list[num_el + 1] = my_list[num_el + 1], my_list[num_el]

print("Переделанный список:", my_list)
