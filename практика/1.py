# print('hello')
# a = 123
# b = 1.23
# print(type(a))
# print(b)

###################################################
# вывести квадрат числа

# a = int(input())
# print(f"квадрат числа = {a**2}")

#################################################

# Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

# a = int(input())
# b = int(input())




# if a ==b**2 or a**2 == b:
#     print(f"число {a} квадрат {b}")
# else:
#     print(f"число {b} не квадрат {a}")

##############################################

# введите 5 чисел и найдите максимальное

# max= int(input())

# for i in range(4):
#     b = int(input())
#     if b > max:
#         max = b
# print(max)


###


# a = list(map(int, input().split()))
# print(max(a))

#########################################

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:*    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


# n = input('Введите число N - ')
# print('диапозон -N до N')
# print(f'{n} -> {list(range(-int(n),(int(n)+1)))}')


########################################################################
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.   
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3



# n = (input().split(".")[1][0])
# print(n)



#############################################################################
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# number3 = int(input('число - '))

# if ((number3 % 5 == 0) and (number3 % 10 == 0) or (number3 % 15 == 0)):
#     if number3 % 30 == 0:
#         print(False)
#     else: print(True)
