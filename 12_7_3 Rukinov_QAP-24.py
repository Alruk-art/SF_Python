print('ЗАДАНИЕ 12.7.3')
print ("Дано: 'Банк' : процент по вкладу.")
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print (per_cent)
sbank=(per_cent.keys()) #Считываем наименования банков
print("Банки : ",list(map(str,sbank)))
sbank_list=list(map(str,sbank)) # Получаем список банков
sproc=per_cent.values()  #Считываем значения процентов
pproc=(list(map(float,sproc))) # Переводим значения в список с плавающей точкой
lenproc=len(pproc) # Узнаём длину списка
print ("Проценты :", pproc,)
money = int(input("Внесите деньги : "))
dep_list=[] # Создаём список
for i in range(lenproc):
        dep=(float( "%0.1f" % (money / 100 * pproc[i]))) # Считаем процент по всем банкам
                                                        # с точностью один знак после запятой
                                                        # При маленьком вкладе это важно.
        dep_list.append(dep) # Добавляем в список.
dohod_list=[] # Создаём полный список из банков и дохода
for i in range(lenproc):
        dohod_list.append((sbank_list[i])) # Добавляем банк в список.
        dohod_list.append(dep_list[i])  # Добавляем процент в список.
print("Доход в каждом банке")
print (dohod_list)
print ("Ваш вклад=", money, "Максимальный доход =",(max(dep_list))) #



