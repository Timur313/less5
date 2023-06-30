import sys
import os
import shutil
from distutils.dir_util import copy_tree
from os.path import isfile, join

def create_folder():
    try:
        inp_val = input('Введите название папки: ')
        if not os.path.isdir(inp_val):
            os.mkdir(inp_val)
    except BaseException as e:
        print(f"Ошибка при создании папки: {e}")

def delete_object():
    try:
        inp_val = input('Введите название файла/папки: ')
        if "." in inp_val:
            os.remove(inp_val)
        else:
            shutil.rmtree(inp_val)
    except BaseException as e:
        print(f"Ошибка при удалении: {e}")

def copy_folder():
    try:
        old_val = input('Введите название копируемой папки: ')
        new_val = input('Введите название новой папки: ')
        copy_tree(old_val, new_val)
    except BaseException as e:
        print(f"Ошибка при копировании: {e}")

def print_folder_contents():
    try:
        inp_val = input('Введите название папки: ')
        print(os.listdir(inp_val))
    except BaseException as e:
        print(f"Ошибка при выводе содержимого: {e}")

def print_folder_contents_only_folder():
    try:
        inp_val = input('Введите название папки: ')
        onlyfolder = [f for f in os.listdir(inp_val) if not isfile(join(inp_val, f))]
        print(onlyfolder)
    except BaseException as e:
        print(f"Ошибка при выводе содержимого: {e}")

def print_folder_contents_only_files():
    try:
        inp_val = input('Введите название папки: ')
        onlyfiles = [f for f in os.listdir(inp_val) if isfile(join(inp_val, f))]
        print(onlyfiles)
    except BaseException as e:
        print(f"Ошибка при выводе содержимого: {e}")

def print_platform():
    try:
        print(sys.platform)
    except BaseException as e:
        print(f"Ошибка при получении информации об ОС: {e}")

def print_author():
    print("Timur313")

