# Найдите сумму цифр трехзначного числа.

n = input("Введите трехзначное число: ")
n = int(n)
 
number1 = n % 10
number2 = n % 100 // 10
number3 = n // 100
 
print("Сумма цифр числа:", number1 + number2 + number3)