# Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.
import fractions 

s1 = str(input("Введите число: "))
s2 = str(input("Введите число: "))

a1 = int(s1.partition('/')[0])
b1 = int(s1.partition('/')[2])
a2 = int(s2.partition('/')[0])
b2 = int(s2.partition('/')[2])

for i in range(1, a1 + 1):
        if b1 % i == 0 and a1 % i == 0:
            b1 = int(b1 / i)
            a1 = int(a1 / i)
for i in range(1, a2 + 1):
        if b2 % i == 0 and a2 % i == 0:
            b2 = int(b2 / i)
            a2 = int(a2 / i)
            
print(a1,b1,a2,b2)

if b1 == b2:
    a1_sum = a1 + a2
    for i in range(1, a1_sum + 1):
        if a1_sum % i == 0 and b2 % i == 0:
            b2 = int(b2 / i)
            a1_sum = int(a1_sum / i)
    print(f'Сумма!: {str(a1_sum)}/{str(b2)}')
else:
    a2_sum = a1 * b2 + b1 * a2
    b2_sum = b1 * b2
    for i in range(1, a2_sum + 1):
        if b2_sum % i == 0 and a2_sum % i == 0:
            b2_sum = int(b2_sum / i)
            a2_sum = int(a2_sum / i)
    print(f'Сумма!: {str(a2_sum)}/{str(b2_sum)}')

a_mult = a1 * a2
b_mult = b1 * b2
for i in range(1,a_mult + 1):
        if b_mult % i == 0 and a_mult % i == 0:
            b_mult = int(b_mult / i)
            a_mult = int(a_mult / i)
print(f'Произведение: {str(a_mult)}/{str(b_mult)}')

print()
f1 = fractions.Fraction(s1)
f2 = fractions.Fraction(s2)
print(f'Сумма: {f1 + f2}')
print(f'Произведение:{f1 * f2}')
