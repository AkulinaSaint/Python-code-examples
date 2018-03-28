import os
import psutil
import shutil


def duplicate_file(filename):
    if os.path.isfile(filename):
        new_filename = filename + ".dupl"
        shutil.copy(filename, new_filename)
        if os.path.exists(new_filename):
            print("Файл создан!")
            return True
        else:
            print("Возникли проблемы")
            return False


def duplicate_all_files(dirname):
    file_list = os.listdir(dirname)
    for filename in file_list:
        duplicate_file(filename)


def remove_files(file):
    file_list = os.listdir(file)
    count = 0
    for filename in file_list:
        fullname = os.path.join(file, filename)
        if fullname.endswith(".dupl"):
            os.remove(fullname)
            if not os.path.exists(fullname):
                count += 1
    return count


def sys_info():
    print("Количество процессоров: ", os.cpu_count())
    print("Название ОС: ", os.name)
    print("Текущая рабочая директория: ", os.getcwd())
    print("Имя пользователя: ", os.getlogin())


def main():
    answer = ''
    while answer != "q":
        answer = input("Давай поработаем?(Y/N/q): ")
        if answer == "Y":
            print("Отлично, хозяин!")
            print("Я умею: ")
            print(" [1] - выведу список файлов")
            print(" [2] - выведу информацию о системе")
            print(" [3] - выведу список процессов")
            print(" [4] - продублирую файлы в текущей директории")
            print(" [5] - продублирую конкретный файл")
            print(" [6] - удалю все файлы-дубликаты из указанной директории")
            do = int(input("Введите вариант: "))
            if do == 1:
                print(os.listdir())
            elif do == 2:
                sys_info()
            elif do == 3:
                print(psutil.pids())
            elif do == 4:
                print("==Дублирование файлов в текущей директории==")
                duplicate_all_files('.')
            elif do == 5:
                filename = input("Какой файл продублировать?: ")
                duplicate_file(filename)
            elif do == 6:
                print("==Удаление дубликатов в директории==")
                dirname = str(input("Из какой директории будем удалять?"))
                count = remove_files(dirname)
                print("Удалено файлов: ", count)
            else:
                print("Неизвестный ответ")
        elif answer == "N":
            print("До свидания!")
        else:
            print("Неизвестный ответ")

if __name__ == "__main__":
    main()