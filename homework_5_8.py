'''Напишите программу в которой создается текстовый файл. Имя файла вводится пользователем.
 Текст для файла вводится пользователем. При записи текста в файл все маленькие буквы заменяются на большие.
'''

filename = input("Введите имя файла: ")
text = input("Введите текст для записи в файл: ")
with open(filename, 'w') as f:
    f.write(text.upper())
print("Текст успешно записан в файл {}.".format(filename))