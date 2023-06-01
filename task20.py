"""
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
""" 

data_1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
value_1 = 1
data_2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
value_2 = 2
data_3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
value_3 = 3
data_4 = ['Й', 'Ы']
value_4 = 4
data_5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
value_5 = 5
data_6 = ['Ш', 'Э', 'Ю']
value_6 = 8
data_7 = ['Ф', 'Щ', 'Ъ']
value_7 = 10

dictionary = {}

dictionary.update({key: value_1 for key in data_1})
dictionary.update({key: value_2 for key in data_2})
dictionary.update({key: value_3 for key in data_3})
dictionary.update({key: value_4 for key in data_4})
dictionary.update({key: value_5 for key in data_5})
dictionary.update({key: value_6 for key in data_6})
dictionary.update({key: value_7 for key in data_7})

#print(dictionary)

word = "НОУТБУК" #input("Введите ваше слово БОЛЬШИМИ БУКВАМИ")
count = 0
for i in word:
    for j in dictionary:
        if(i==j):
            count=count+dictionary[j]

"""for letter in word:
    for key in dictionary:
        if letter == key:
            count += dictionary[key]
"""
print(count)
