#Домашнее задание по теме "Файлы в операционной системе"
import os
import time

directory = '.' #os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.path.getmtime(file) #os.stat(file).st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
