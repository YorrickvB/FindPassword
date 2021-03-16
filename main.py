__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'
import os
import shutil
from os.path import isfile, join

def main():
    if os.path.isfile('data.zip'): #Check if the Data.zip file is in this folder
        print('Data.zip file found')
        file_path = os.getcwd() + '\data.zip'
        cache_path = os.getcwd() + '\cache'
        cache_zip(file_path, cache_path)
        find_password(cached_files())
    else:  #Not found? Than better not mess with any other files
        print('Data.zip not found')

def clean_cache():
    if os.path.isdir('cache'):  #If cache folder already exists, delete everything
        shutil.rmtree('cache')
        os.mkdir('cache')
        print('Cleared cache folder')
    else:  #if it does not exist, create one
        os.mkdir('cache')
        print('Created cache folder')

def cache_zip(file_path, cache_path):
    clean_cache()
    shutil.unpack_archive(file_path, cache_path, 'zip')
    print('Unpacked Data.zip file into cache folder')

def cached_files():
    os.chdir('cache')
    folder = os.getcwd()
    list_files = [f for f in os.listdir(folder) if isfile(join(folder, f))] 
    absolute_list = []
    for f in list_files: #specify in absolute terms
        absolute_list = absolute_list + [os.path.abspath(f)]
    return absolute_list

def find_password(file_list):
    for i in file_list:
        if 'password' in open(i).read():  #find the magic word 'password'
            print('Password found')
            string = open(i)
            password_string = string.read().replace("\n", " ")
            print(f'The password to World Domination is in this string: {password_string}')


if __name__ == '__main__':
    main()