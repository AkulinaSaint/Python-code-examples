import os


def ch_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    os.chdir(path)
    print('Переход в папку {} совершен!'.format(path))


def list_dir():
    print('Содержимое папки {}'.format(os.getcwd()))
    for i in os.listdir(os.getcwd()):
        print(i)


def del_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    os.rmdir(path)
    print('Удаление папки {} совершено!'.format(path))


def add_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    os.mkdir(path)
    print('Создание папки {} совершено!'.format(path))
