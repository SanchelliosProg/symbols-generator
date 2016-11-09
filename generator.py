import string
import random

def string_generator(chars, size):
    return ''.join(random.choice(chars) for _ in range(size))

def string_list_generator(chars):
    r = [8, 16, 32, 64, 128, 256, 512, 1024]
    list = []
    for num in r:
        list.append(string_generator(chars, num))
        num *= 2
    return list

def write_into_file(list):
    file = open('result.txt', 'w')
    for line in list:
        file.write(line+'\n')
    file.close()

include_lowercase = True
include_uppercase = True
include_digits = True
include_punctuation = True
include_space = False

chars = ''
if(include_lowercase):
    chars += string.ascii_lowercase

if(include_uppercase):
    chars += string.ascii_uppercase

if(include_digits):
    chars += string.digits

if(include_punctuation):
    chars += string.punctuation

if(include_space):
    chars += ' '

size = 64

write_into_file(string_list_generator(chars))
