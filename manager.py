import os
import random
import datetime
import argparse
import sys
import difflib
import subprocess


DEFAULT_DAYS     = 7
FOLDER_ZADANIA   = 'zadania'
FOLDER_MATERIALY =  'materialy'
FOLDER_SLOWA     = '.funny_words.txt'
DATE_PATTERN     = "%d/%m (%H-%M-%S)"


def current_date():
    return datetime.datetime.now().strftime(DATE_PATTERN)


def get_info_dict(filename = 'info.txt'):
    return dict([[line.split(':')[0].strip(), [e.strip() for e in line.split(':')[1].split(',')]] for line in open(filename).read().split('\n') if ':' in line])


def all_folders_names(filename = FOLDER_ZADANIA):
    try:
        return list(os.walk(filename))[0][1]
    except IndexError:
        return []


def all_folders_paths(filename = FOLDER_ZADANIA):
    return [os.path.join(filename, e) for e in all_folders_names()]


def all_names():
    if not os.path.exists(FOLDER_ZADANIA):
        return []
    return list(os.walk(FOLDER_ZADANIA))[0][1]


def all_available_names_number(filename = FOLDER_SLOWA):
    d = get_info_dict(filename)
    result = 1
    if len(d) == 0:
        return 0
    for key, l in d.items():
        result *= len(l)
    return result


def random_name(filename = FOLDER_SLOWA):
    d = get_info_dict(filename)
    result = ''
    for key, l in d.items():
        if result != '':
            result += '_'
        result += random.choice(l)
    return result


def new_random_name():
    if len(all_names()) >= all_available_names_number():
        print('brak dostepnych nazw folderow!')
        exit(0)
    
    while True:
        name = random_name()
        if name not in all_names():
            return name


def get_seconds():
    return int(datetime.datetime.now().timestamp())


def init_new_folder(path, _format = 'normal'):
    p = open(os.path.join(path, '.info.txt'), 'w+')
    p.write('TODO : ' + ('True\n' if _format == 'project' else 'False\n'))
    p.write('message : Just a ' + _format + '\n')
    p.write('dates : ' + current_date() + '\n')
    p.write('seconds : ' + str(get_seconds()) + '\n')


def add_smth(_format):
    name = new_random_name()
    path = os.path.join(FOLDER_ZADANIA, name)
    if os.path.exists(path):
        raise FileExistsError
    os.makedirs(path)
    init_new_folder(path, _format)


def add_normal():
    add_smth('normal')


def add_project():
    add_smth('project')


def get_file_info(path, filename):
    d = get_info_dict(os.path.join(path, '.info.txt'))
    return (
        filename  + '\n\t' +  
        ' '.join('[{}]'.format(e) for e in d['message']) + 
        '\n| created {} | last open {}'.format(d['dates'][0], d['dates'][-1]) + ' |\n'
    )           

def show_info_list(info_list, comment):
    print('{} # {} things'.format(comment, len(info_list)))
    for i, e in enumerate(info_list):
        print('{}. {}\n'.format(i + 1, e))


def show_todo():
    todo_list = []
    for path, filename in zip(all_folders_paths(), all_folders_names()):
        d = get_info_dict(os.path.join(path, '.info.txt'))
        if d['TODO'][0] == 'False':
            continue
        todo_list.append(get_file_info(path, filename))
      
    show_info_list(todo_list, 'TODO')
    

def status():
    show_todo()
    show_recent()


def days_passed(pre_second):
    second = get_seconds()
    return (second - int(pre_second)) / 3600 / 24


def show_recent(days = DEFAULT_DAYS):
    recent_list = []
    for path, filename in zip(all_folders_paths(), all_folders_names()):
        d = get_info_dict(os.path.join(path, '.info.txt'))
        if days_passed(d['seconds'][-1]) > days:
            continue
        recent_list.append(get_file_info(path, filename))
    show_info_list(recent_list, 'RECENT')



def Help():
    print('jestes w pliku nadrzednym')
    print('* add_normal')
    print('\t- dodaje zwykly folder')
    print('* add_project')
    print('\t- dodaje projekt')
    print('* show_todo')
    print('\t- pokazuje projekty do zrobienia')
    print('* show_recent [days]')
    print('\t- pokazuje projekty otwarte do {} dni'.format(DEFAULT_DAYS))
    print('\t  opcjonalnie mozna podac liczbe dni')
    print('* status')
    print('\t- pokazuje info ogolne')
    print('* help')
    print('\t- pokazuje znaczenie funkcji')
    print('* open <name>')
    print('\t- otwiera dany folder i modyfikuje flagi')
    print('* update_git')
    print('\t- updatuje gita')
    

def do_bash(bash_cmd = ['ls', '.']):
    process = subprocess.Popen(bash_cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    # print('bash command [output: {}] [error: {}]'.format(output, error))
    return error != None



def Open(name):
    subprocess.Popen()


def update_git(message = 'just an update'):
    error = False
    error |= do_bash(['git', 'add', '.'])
    error |= do_bash(['git', 'commit', '-m', '\"{}\"'.format(message)])
    error |= do_bash(['git', 'push'])
    if error:
        print('something went wrong with git..')


def parsuj():
    for arg in sys.argv[1:]:
        cur_arg = arg
        if cur_arg not in get_command_dict():
            cur_arg = difflib.get_close_matches(cur_arg, list(get_command_dict().keys()))
            if (len(cur_arg) != 1):
                print('nie rozpoznano "{}", kontynuuje program..'.format(arg))
                continue
            print('nie rozpoznano "{}", wiec wykonuje {}..'.format(arg, cur_arg[0]))

        print('{} in progress..'.format(cur_arg[0]))
        get_command_dict()[cur_arg[0]]()


def get_command_dict():
    return {
        'add_normal':  add_normal,
        'add_project': add_project,
        'show_todo':   show_todo,
        'show_recent': show_recent,
        'status':      status,
        'help':        Help,
        'open':        Open,
        'update_git':  update_git
    }

if __name__ == '__main__':
    parsuj()



	
