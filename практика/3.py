
# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['ssss', 'sngujn556', 56] -> Yes
# ['56', 'sgnbsb'] -> No

result = False
sp = ('123', '123','32143','42342','sdf')
for item in sp:
    try:
        item.isdigit()
    except:
        result = True
if result: result = "Yes"
else: result = "No"
print(f'{sp} -> {result} ' )


# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# ​
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


a = input()
ins = 0
sp = ['123', '123','32143','42342','sdf' ,'56456','3245' , '464' , 'sdf']
for i in range(sp.__len__()):
    if sp[i]  ==a:
        ins +=1
    if ins ==2:
        print(f'{sp}, индекс второго вхождения = {i}')
        break    
    else:
        continue
else:
    print(f'{sp}, ищем "{a}" --->  нет в списке')


        
