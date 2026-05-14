import os

folder_name = 'rezult'
project_directory = os.getcwd()

file_path = project_directory +"/setting.txt"


def read_setting_file():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readline()
            if not content:
                return []
            sp = content.strip().split(";")
            return sp
    except FileNotFoundError:
        create_file()
        sp = read_setting_file()
        return sp
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


def write_setting_file(n, s):
    sp = read_setting_file()
    if sp is []:
        pass
    else:
        sp[n] = s
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                d = ";".join(sp)
                file.write(d)
        except FileNotFoundError:
            create_file()
            write_setting_file(n, s)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def create_file():
    with open(file_path, 'w') as file:
        file.write("#ffff80;#ffffff;#ff00ff;pj;ttf;name3;9099999990")
        print(file_path)