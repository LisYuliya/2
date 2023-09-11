# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

num1 = input("Введите первую дробь: ").split('/')
num2 = input("Введите вторую дробь: ").split('/')

numerator1, denominator1 = int(num1[0]), int(num1[1])
numerator2, denominator2 = int(num2[0]), int(num2[1])

common_denominator = 1
for i in range(2, min(denominator1, denominator2) + 1):
    if denominator1 % i == 0 and denominator2 % i == 0:
        common_denominator = i

summ_numerator = (numerator1 * denominator2 + numerator2 * denominator1) // common_denominator
summ_denominator = (denominator1 * denominator2) // common_denominator

multi_numerator = (numerator1 * numerator2) // common_denominator
multi_denominator = (denominator1 * denominator2) // common_denominator

sum_result = [summ_numerator, summ_denominator]
print(f'{numerator1}/{denominator1} + {numerator2}/{denominator2} = {sum_result[0]}/{sum_result[1]}')

multi_result = [multi_numerator, multi_denominator]
print(f'{numerator1}/{denominator1} * {numerator2}/{denominator2} = {multi_result[0]}/{multi_result[1]}')

fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

sum_fraction = fraction1 + fraction2
multi_fraction = fraction1 * fraction2

print(f'С использованием fractions:')
print(f'{fraction1} + {fraction2} = {sum_fraction}')
print(f'{fraction1} * {fraction2} = {multi_fraction}')