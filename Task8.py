# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите размер n: "))
m = int(input("Введите размер m: "))
k = int(input("Введите количество долек k: "))
s = m*n-k
if n+m>k and s%m==0:
    print("Yes")
    if n + m >= k and s%n == 0:
        print("Yes")
else:print("No") 