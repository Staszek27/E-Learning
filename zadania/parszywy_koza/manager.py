import manager_parent
import shutil

EXAMPLE_NAME = 'example'

def available_name(extension, path):
    '''finding new filename with given extension under some path'''
    print(extension, path)
    exit(0)



def add(extenstion):
    pass


def add_as_material(filename):
    pass 


def send(email):
    pass


def change_attr(key, value, filename):
    d = manager_parent.get_info_dict(filename)
    p = open(filename, 'w+')
    d[key] = value
    for key, value in d.items():
        p.write(key, ':', value)
    p.close()
    

def done():
    change_attr('TODO', 'False', '.info.txt')


def undone():
    change_attr('TODO', 'True', '.info.txt')


def get_command_dict():
    return {
        'add':  add,
        'add_as_material': add_as_material,
        'send':   send,
        'done': done,
        'undone': undone
    }


if __name__ == '__main__':
    manager_parent.parsuj(get_command_dict())