# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

number_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
number_x = int(input('Введите число Х: '))

distance = abs(number_list[0] - number_x)
element = number_list[0]

for index in range(len(number_list)):
    if abs(number_list[index] - number_x) < distance:
        distance = abs(number_list[index] - number_x)
        element = number_list[index]
print(element)

    
