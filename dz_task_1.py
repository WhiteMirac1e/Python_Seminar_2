# Напишите программу, которая получает целое число и возвращает
#  его шестнадцатеричное строковое представление.
#  Функцию hex используйте для проверки своего результата.

number = int(input("Введите число: "))
BASE = 16
original_number = number
result_number = ''
while number:
    if number%BASE < 10:
        result_number =str(number%BASE) + result_number
    elif number%BASE == 10: result_number ='A' + result_number
    elif number%BASE == 11: result_number ='B' + result_number
    elif number%BASE == 12: result_number ='C' + result_number
    elif number%BASE == 13: result_number ='D' + result_number
    elif number%BASE == 14: result_number ='E' + result_number
    elif number%BASE == 15: result_number ='F' + result_number
    elif number%BASE == 16: result_number ='G' + result_number
    number //= BASE
print(f'Число {original_number} В {BASE}-ичной системе счисления будет {result_number}')
print(hex(original_number))
