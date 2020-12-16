import manager_parent
import shutil
import os
import datetime



INFO_FILES = ['.info.txt', 'manager_parent.py', 'manager.py']
EXAMPLE_FOLDER = 'examples'
EXAMPLE_NAME = 'example'

def number_of_files(extension, path):
    return sum([1 for e in list(os.walk('.'))[0][2] if e.endswith(extension)])


def all_files(path):
    return list(os.walk(path))[0][2]


def add(extension):
    x = number_of_files(extension, '.') + 1
    filename = f'prog{x}.{extension}'
    shutil.copy(
        os.path.join(os.getcwd(), '../..', EXAMPLE_FOLDER, f'{EXAMPLE_NAME}.{extension}'),
        os.path.join('.', filename)
    )
    manager_parent.do_bash(['code', filename])


def work_files(path = '.'):
    result = set(all_files(path))
    for f in INFO_FILES:
        result.remove(f)
    return list(result)


def create_paper(filenames, dest):
    print(filenames)


def send(*emails):
    emails = list(emails)
    if len(emails) == 0:
        emails.append('bryjak1133@gmail.com')
    my_files = work_files('.')
    dest = 'notatki_{}.txt'.format(manager_parent.current_date('%d_%m'))
    create_paper(my_files, dest)



def change_attr(key, value, filename):
    if type(value) != list:
        value = [value]
    d = manager_parent.get_info_dict(filename)
    d[key] = value
    
    open(filename, 'w').write(
        '\n'.join(['{} : {}'.format(key, ', '.join(value)) for key, value in d.items()])
    )
    
    

def done():
    change_attr('TODO', 'False', '.info.txt')


def undone():
    change_attr('TODO', 'True', '.info.txt')


def Help():
    print('jestes w pliku poddrzednym')
    print('* add [extension]')
    print('\t- dodaje rozszerzenie')
    print('* send [email]')
    print('\t- wysyla pliki na maila')
    print('* done')
    print('\t- zaznacza folder jako zakonczony')
    print('* undone')
    print('\t- zaznacza folder jako niedokonczony')
    print('* help')
    print('\t-pokazuje znaczenie funkcji')


def get_command_dict():
    return {
        'add':  add,
        'send':   send,
        'done': done,
        'undone': undone,
        'help': Help
    }


if __name__ == '__main__':
    manager_parent.parsuj(get_command_dict())   