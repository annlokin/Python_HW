# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

num = int(input("Введите номер билета: "))
num = int(num)

left_part = round(num/1000)
print (left_part)
right_part = num%1000
print (right_part)
if (left_part/100+(left_part/10)%10+left_part%10)==(right_part/100+(right_part/10)%10+right_part%10):
  print("Билет счастливый")
else:
  print("Обычный билет")