'''
Написать программу, которая запрашивает на ввод целые числа, до тех пор, пока не будет введена пустая строка. 
Затем она выводит: а) введенную последовательность чисел; б) сумму введенных чисел; в) самое большое число из введенных. 
(а), (б) и (в) – это разные варианты одной программы.
...
#a)
'''
ls = []
while True:
    number = input("Введите целое число ")
    if number != "" and number.isdigit():
        ls.append(number)
    elif number != "" and isinstance(number, str):
        continue
    else:
        print("Вы ввели пустое значение")
        break
print(ls)

...
#б)
...
ls = []
while True:
    number = input("Введите целое число ")
    if number != "" and number.isdigit():
        ls.append(int(number))
    elif number != "" and isinstance(number, str):
        continue
    else:
        print("Вы ввели пустое значение")
        break
print("Сумма всех введенных вами чисел = "+str(sum((ls))))


#в)

ls = []
while True:
    number = input("Введите целое число ")
    if number != "" and number.isdigit():
        ls.append(int(number))
    elif number != "" and isinstance(number, str):
        continue
    else:
        print("Вы ввели пустое значение")
        break
print("Максимальное число в списке = "+str(max((ls))))

#И наконец-то я поняла, как можно написать функцию, которая создает список из введенных чисел. 
def list_with_numbers(number, ls = []):
    if number != "" and number.isdigit():
        ls.append(int(number))
        while True:
            number = input("Введите целое число ")
            if number != "" and number.isdigit():
                ls.append(int(number))
            elif number != "" and isinstance(number, str):
                continue
            else:
                print("Вы ввели пустое значение")
                break
        return ls
    else:
        print("Введено некорректное значение")
        list_with_numbers(input("Введите число: "))
        
        
    
list_with_numbers(input("Введите число: "))

print(list_with_numbers(input("Введите число: "))) #выводит просто список
print(sum(list_with_numbers(input("Введите число: ")))) #выводит сумму чисел
print(max(list_with_numbers(input("Введите число: ")))) #выводит максимальное значение


'''
Написать программу, которая запрашивает на ввод произвольную строку текста (написанную с  использованием латинского алфавита). 
Программа выводит: а) эту же строку, но без гласных; б) список использованных гласных; в) количество использованных гласных; 
г) статистику по встречаемости (буква – количество ее вхождений в строку). (а), (б), (в) и (г) – это разные варианты одной программы.
'''


def consonant(s): #a) строка без гласных

    c=[]
    for x in s:
        if x not in 'eyuioaEYUIOA':
            c.append(x)
    new_s=''.join(c)
    print("Ваша строка без гласных :"+new_s)

consonant(input("Введите строку "))

def vowel(s): #б) список использованных гласных

    c=[]
    for x in s:
        if x in 'eyuioaEYUIOA':
            c.append(x)
    new_s=''.join(c)
    print("Список использованных гласных :"+new_s)

vowel(input("Введите строку "))


def counter(s): #в) количество гласных в строке
    result=0
    for x in s:
        if x in 'eyuioaEYUIOA':
            result+=1
    print("Количество гласных в строке равно "+result)

counter(input("Введите строку "))


def vowel_count(s): #г) статистику по встречаемости
    
    c={}
    for x in s:
        if x not in c and x in 'eyuioaEYUIOA':
            c[x]=s.count(x)
    print(c)

vowel_count(input())



def true_func(number):####эта штука пока не работает((((
    devisor=[2, 3, 5, 7, 11]
    result=0

    if number != "" and number.isdigit():

        for i in devisor:
            if int(number) % i==0:
                result+=1

    elif number != "" and isinstance(number, str):
        continue

    else:
        print("Вы ввели пустое значение")
        break
        true_func(input("Введите число: "))

    if result >=1:
        return True
        #else:
        #print("Введено некорректное значение")
        #true_func(input("Введите число: "))

true_func(input("Введите число: "))