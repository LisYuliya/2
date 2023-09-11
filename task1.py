# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

values = '0123456789abcdef'
number = int(input("Введите число: "))
number2 = number
base = 16
result = ''

while number > 0:
    result = values[number % base] + result
    number //= base

print('После перевода в 16-ную систему счисления число = ' + result)
print('Проверка с помощью "hex": ' + hex(number2)[2:])
