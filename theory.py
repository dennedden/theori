# вертуальное окружение = все допы, и другая фигня(# = коментарие строки)
# ctrl / = онспектирую строку. повторное нажатие уберает #. ctrl shift z вперёд действие
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#print ("hello world")/ ctr shift f10 = альтернатив запуск програмы
# # mmm = 18
# # mmn = 17
# # print(f"ousdhfoiuh",mmm ) # F = модерн строки с использыванием массива
# a = 5 # переменная = (не называть как а,б,в,г,д,е,ё....(чтобы понятно было через год и больше ))
# num_1 = 8 #номер числа
# num_2 = 8
# # print(num_1 + num_2)
#
# print(num_1 + num_2) # сложение числа
# print(num_1 ** num_2) # степень числа
# print(num_1 * num_2) #умножение числа
# print(num_1 / num_2) #деление с остатком
# print(num_1 // num_2) #деление до целого
#print(num_2 % num_1) # кароч если делишь 7 на 3 то там останеться то что ты не можешь поделить на целое и получ 1

#калькулятор вес
# weight = input('введи вес в кг: ')
# height = input('введи рост в м: ')
#
# result = int(weight) / float(height) ** 2
# print(f'ответ: {result:.2f}') # вместе с f мы пишем всесте с массивами

# j = input('введи число: ') # вход
# l = input('введи число №2: ')
# # print(j + l)
#
# # print(5 + 4)
# # print('56' + '9')
# # d='7'; d = int(7) я признал число 7 числом
#
# print(int(j) + int(l)) # я сложил признаные числа между собой
#
# name = 'пррорро6 '
# print(name[-1]) # при -1 идёт с конца
#
# last_neme = "oiashfiu"
# print(name + last_neme) # сочитаю имя и last_neme вместе
# print(name * 9) # увеличиваю количество имени в определёное количество раз
# print(len(name)) # считает количество символов
#input - я могу написать

# age = input("ты кто по масти?")
#
# if int(age) >= 18:
#         print("ты гордый орёл") # 4 пробела это tab (табулирование)
# else:
#     print(" не крут(сегодня без пива)")
##камень,ножницы,бумага
# import random  # работает от начала до конца
#
# player = input("играй")
# print(player.lower())  # lower = все заглав буквы превращять в маленькие
# computer = "камень", "ножницы", "бумага"
#
# comp = random.choice(computer)  # комп выбор 1\3
# print(comp)
#
# if player.lower() == comp:  # сравниваю выбор
#     print("почти")
# elif player == "камень" and comp == "ножницы":
#     print("юху")
# elif player == "нижницы" and comp == "бумага":
#     print("юху")
# elif player == "бумага" and comp == "камень":
#     print("юху")
# elif player == "ножницы" and comp == "камень":  # сложный варик
#     print("нет")
# elif player == "камень" and comp == "бумага":
#     print("нет")
# elif player == "бумага" and comp == "ножницы":
#     print("нет")
# # else:                #ЛЁГКИЙ ВВАРИК
# #     print("HET")


# age = -6
# # если сравнить то == а если не равни то =!
# if age<= 10:
#     print("бэйби")
# elif age>= 11 and age<= 20: # elif (продолжение if) если есть elif тогда при выполнение ранней штуки то оно не будет проверять дальше
#     print("бедолага")
# elif age >=21 and age <=60:
#     print("фуууу иди работай")
# elif age >= 61: # я мог написать else: оно не будет сппрашивать дальше ведь нет смысла
#     print("пенсия")

#купи слона

# exit_variants = ['Аааа',"гг"]
# print('купи слона')
# while True: #бесконечный цыкл
#     tex = input()
#     if tex in exit_variants:
#     #if tex == "ааа":
#         print('ну и ладно')
#         break
#     else:
#         print('все говорят', tex, 'а ты купи')
#     #break#сбрасывает цыкл
# кредит
# money = input('сколько у тебя? \n')#\n перенос ответа пользователя на другую строчку
# money = float(money)
# percent = input('ызшмпр \n')
# percent = float(percent)
# year = input('сколько лет? \n')
# year = int(year)
# count = 0
# while count <= (year):
#     money += ((money)/100)*(percent)
#     count += 1
# print('горе бизнесмен',money)

#игра в угадайку
# import random
#
# print('я загадал от 0...100')
# j = random.randint(0,100)
# count = 1
# while True:
#     try:
#         k = int(input())
#     except:#исключение
#         print('глупец')
#         k = int(input())
#     if j==k:
#         print('хорош')
#         break
#     elif j < k:
#         print('ниже')
#     elif j > k:
#         print('выше')
#     count += 1
# print('апапаппап',count)
#
# print('ты вода')
#
# d = 50
# while True: #!= не равно
#
#     print(d)
#     l = input()
#     if l == 'больше':
#         d+= d//2
#     if l == "HeT":
#         d -= d//2
#
# print("ypa")
#монетка
# print('готов?')
# import random
# while True:
#     player_chois = input('opel (0) ili peшka (1):')
#     toss_result = random.randint(0,1)
#
#     if player_chois == str(toss_result):
#         print('fdf')
#     else:
#         print("olih")

#почти кости
# import random
#
# win = 0
# lose = 0
# nobodys = 0
#
# while True:
#     input("кидай")
#     comp_dice_1 = random.randint(1, 6)
#     comp_dice_2 = random.randint(1, 6)
#     comp_dice_3 = random.randint(1, 6)
#     comp_dice_4 = random.randint(1, 6)
#     comp_dice_5 = random.randint(1, 6)
#
#     player_dice_1 = random.randint(1, 6)
#     player_dice_2 = random.randint(1, 6)
#     player_dice_3 = random.randint(1, 6)
#     player_dice_4 = random.randint(1, 6)
#     player_dice_5 = random.randint(1, 6)
#
#     comp_total = comp_dice_2 + comp_dice_1 + comp_dice_3 + comp_dice_4 + comp_dice_5
#     player_total = player_dice_4 + player_dice_5 + player_dice_3 + player_dice_2 + player_dice_1
#     print(f'у тебя: {player_dice_4}  {player_dice_5}  {player_dice_3}  {player_dice_2}  {player_dice_1}= {player_total}' )
#     print(f"у меня {comp_dice_1}  {comp_dice_2}  {comp_dice_3}  {comp_dice_4}  {comp_dice_5}= {comp_total}")
#     if player_total == comp_total:
#         print("ничья это победа для слабых")
#         nobodys += 1
#     elif player_total > comp_total:
#         print("победа это наше всё")
#         win += 1
#     elif player_total < comp_total:
#         print("имперя не потерпит поражение")
#         lose += 1
#     print(f'побед', win, "проигреш", lose, "нечья", nobodys)
# #итэрированый обьект = масив с несколько чисел
#
#CПИСКИ !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# a  = 1,2,3,4,5,6,7,8,9
#
# for i in range(1, 100): # перечисл/range от ** до ** только в бескон не в print и послеждний элемент не учит
#     print(i ** 10)

# my_list = [1, 2, 3, 4, 5]
# print(my_list)
#
# my_list.append(8)#append = абовляет в канец списка что-то
# print(my_list)
#
# print(my_list[-1])
# name = ['санта', 'fff', 'не я']
# print(name[-2])
#
# name.insert(0, "kjuitjk")#insert = вставка на определённую позицию
# print(name)
#
# del name[-1]#del name = удаление элемента по индексу
# print(name)
#
# name.pop(-1)#name.pop = тоже самое но только сохраняет удалённое
# print(name)
#
# deleted = name.pop(-1)
# print(name)
# print(deleted)
#
# name.remove("kjuitjk")#name.remove = удолят не по индексу а по соответсвию название
# print(name)
# #name.sort = сартирует по алфовту, заглавным и др. на постоянной основе
#
# name = ['Санта', 'fff', 'не я', '777', 'ab', '999', 'аб']
# #name.sort()
# sorted_name = sorted(name)#sorted_name = sorted(name) = временная сартировка
# print(name)
# print(sorted_name)
#
# name.reverse()#name.reverse = разварот списка
# print(name)
#
# print(len(name))#len(name) показывает сколько элементов
#
# #def calculate_expenses(expenses: list):
#     total_expenses = sum(expenses)
#
#     max_expenses = max(expenses)
#     min_expenses = min(expenses)
#
#     average_expenses = total_expenses / len(expenses)
#     print(f"oBo {total_expenses}")
#     print(f"miн {min_expenses}")
#     print(f"max {max_expenses}")
#     print(f"средн {average_expenses:.2f}")#:.1f = округлил до десятых
# expenses = [10, 76, 98754, 764, 79]
# calculate_expenses(expenses=expenses)
# marks = [1, 7, 8, 8, 9]
#
# min_mark = min(marks)
# max_mark = max(marks)
#
# print(f'maxi {max_mark}')
# print(f'mini {min_mark}')
#
# marks_sum = sum(marks)#sum = общее число
# count_marks = len(marks)# len = количество оценок
# print(count_marks)
# print(f"kyug {marks_sum / count_marks:.1f}")#:.1f = округлил до десятых
# def hello():
#     print("hello world")
#     print('Саюз не рушимый')
# #hello()#вызов функции
#
# def get_user(name, age):
#     print(f"kjyf, {name}")
#     print(f"kjyfk, {age}")
#     if age >= 18:
#         print(f"jiyg{name}")
#     else:
#         print(f"kjyfhjdtf{name}")
#
# get_user(name="kjiyfhjgd", age= 7 )
# def chek_user(username, status="user"):
#     if status == "admin":
#         print(f'{username} админ')
#     else:
#         print(f'{username} не админ')
# chek_user(username= "лопотиша")
# chek_user(username= "щщщщщщщщщ", status= 'admin')
#
#словори
# my_dict = {
#     'name': 'denis',#name и др. это ключ и он не повторяется
#     'age' : 15,# 15 и др это значение и оно может повторятьса
#     "city" : "Samara"# элемент это ключ + значение и  он уникален
# }
# my_dict1 = {'name': 'denisn', 'age' : 155}
#
# print(my_dict ['name'])#я обратился к элементу и вывел имя
# print(my_dict ['age'])
#
# my_dict['citi'] = "homel"# я изменил значение
# print(my_dict)
# #+ элемент
# my_dict['status'] = 'admin'
# print(my_dict['status'])
# print(my_dict.keys())#keys вывод ключей
#
# print(my_dict.values())#вывод значение
# #print(my_dict.clear())#удаляет весь словарь
# print(my_dict.copy())#копирует словарь
# print(my_dict.items())#вывод всех элементов
# for i in my_dict:
#     print(i)
# for key, value in my_dict.items():
#     print(f"ключ: {key}, начение: {value}")
#
#магазин
# assortment_good = {
#     'car' : 12,
#     'tractor' : 77,
#     'microwave' : 86,
#     'monument to leninin' : 64
# }
#
# def sell_good(item: str, quantity: int):#"""""" строки документации, уменьш количств товара при продаже
#     """
#
#     :param item:
#     :param quantity:
#     :return:
#     """
#     if item in assortment_good.keys() and quantity <= assortment_good[item]:
#       assortment_good[item] -= quantity
#       print(f'продано {quantity} товар {item}')
#       print(f' товар{item} осталось {assortment_good[item]}')
#     else:
#         print('бан')
# sell_good(item='car', quantity=11)
#ошибка
# user_age = input('введите свой возрост:')
#
# try:#try - пытаться(ловим ошибки и делаем их норм для глаз)
#     if int(user_age) >= 18:
#         print('норм')
#     elif int(user_age) <= 18 and int(user_age) >= 0:
#         print('бэйби')
#     elif int(user_age) <= -1:
#         print('не верю')
# except ValueError:#поймал на ошибке‍🐱‍👤
#     print('нет')
# except excepting as ex:
#     print('dfregv')
# file = open('files/test.txt', 'r', encoding='utf-8')#encoding = кодировка
# # r - read - чтение всего файла
# print(file.read())#чтение всего файла
# file.close()
#я не знаю что это
# with open('files/test.txt', 'r', encoding='utf-8') as file:
#     #print(file.read())
#     #print(file.readline(5))#чтение одной строки
#     print(file.readlines())
# # with open('files/test.txt', 'w', encoding='utf-8') as file:#w - write стерает и пишит другое
# #     print('a?')
# with open('files/new.txt', 'a', encoding='utf-8') as file:#a - дабавляет и не стирает прошлое
#     print('a?')
#методы функций python - функция, которая принадлежит к конкретному классу и не может быть использована отдельно от него. Например,
# методы строк ( count() , replace() , split() и др.) применяются только к объектам класса str (тип данных str это объекты класса str ),
# но не могут применяться к объектам других классов.
#класс - чертёж объекта
#метод в нутри класса
#денег неть!!!!!!!!!!!!!!!!!!!!!!!!!
# import sys
# import tkinter
# import random
# from tkinter import messagebox
#
#
# class App:
#     def __init__(self):
#         self.root = tkinter.#tkinter - Tk()Позволяет показывать, редактировать и форматировать текст с использованием различных стилей,
#         а также внедрять в текст рисунки и окна.
#
#         self.windows_settings()
#         self.set_label()
#         self.set_button_yes()
#         self.set_button_no()
#         self.set_button_sos()
#
#
#         self.root.mainloop()
#
#     def windows_settings(self):#вызов окна
#         self.root.title('Опрос')
#         self.root.geometry('800x600')#размер окна
#         self.root.resizable(False,False)#resizable - изменяемость размера.Метод resizable() используется, чтобы позволить корневому окну Tkinter изменять свой размер в соответствии с потребностями пользователя,
#     # а также мы можем запретить изменение размера окна Tkinter. Итак, по сути, если пользователь хочет создать окно фиксированного размера, можно использовать этот метод. Как использовать:
# # -> импортировать ткинтер
# # -> корень = Тк()
# # -> root.resizable (высота = нет, ширина = нет)
# # Аргументы, которые необходимо передать:
# # -> В методе resizable() пользователь может передать либо положительное целое число, либо True, чтобы изменить размер окна. -> Чтобы сделать окно неизменяемым, пользователь может передать 0 или False.
#         #self.root['bg'] = 'black'#задний фон
#     def set_label(self):
#         question = tkinter.Label(self.root, text='Вы хотите увеличить зарплату?', font=('Arial', 20))
#         question.place(relx=0.5, rely=0.1, anchor='center')#relx\rely = отступ по х или у
#
#     def set_button_yes(self):
#         self.btn_yes = tkinter.Button(self.root, text='yes', font=("Beer money", 20))#btn - книпка
#         self.btn_yes.place(relx=0.3, rely=0.6, anchor='center')
#         self.btn_yes.bind('<Enter>', self.motion_bbutton_yes)
#
#
#     def motion_bbutton_yes(self, *args):
#         self.btn_yes.place(x=random.randint(0,400), y=random.randint(0,200))
#
#     def set_button_no(self):#btn = спец функция позволяет выполнять дейсвие при определёном условии
#         btn_no = tkinter.Button(self.root, text='no', font=("Beer money", 20), command=self.button_no_click)#btn - книпка
#         btn_no.place(relx=0.7, rely=0.6, anchor='center')
#
#     @staticmethod# = диткоратор вызов через @ обертка для функции
#     def button_no_click():
#         tkinter.messagebox.showinfo('ответ', 'ваше мнение не влияет на компанию')
#         sys.exit()#закрывает вкладку после ответа
#     def set_button_sos(self):
#         btn_sos = tkinter.Button(self.root, text='sos', font=("Beer money", 20), command=self.button_no_click)  # command=self = задает действие rybgrt
#         btn_sos.place(relx=0.5, rely=0.6, anchor='center')
#
# app = App()
# from googletrans import Translator  # Googletrans = дополнение гугл переводчик# row = строка# column = столб# pad = отступ