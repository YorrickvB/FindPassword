__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'
import os
import shutil
from os.path import isfile, join

def clean_cache():
    shutil.rmtree('cache') if os.path.isdir('cache') == True else False
    os.mkdir('cache')

def cache_zip(file_path, cache_path):
    path = cache_path[0:cache_path.rfind('\cache')]
    os.mkdir(path) if os.path.isdir(path) == False else True
    os.chdir(path)
    clean_cache()
    shutil.unpack_archive(file_path, cache_path, 'zip')

def cached_files():
    os.chdir('cache')
    folder = os.getcwd()
    list_files = [f for f in os.listdir(folder) if isfile(join(folder, f))]
    absolute_list = []
    for f in list_files:
        absolute_list = absolute_list + [os.path.abspath(f)]
    return absolute_list

def find_password(file_list):
    for i in file_list:
       if 'password' in open(i).read():
           string = open(i)
           password_string = string.read().replace("\n", " ")
           return f'password_string'
        