import argparse
def execute_command(user_input):
    parts = user_input.split()
    if not parts:
        return "OK"
    command = parts[0]
    command_args = parts[1:]
    if command == "exit":
        print("Завершение работы VFS")
        return "exit"
    elif command == "ls":
        print("Команда: ls")
        print("Аргументы: ", command_args)
    elif command == "cd":
        print("Команда: cd")
        print("Аргументы: ", command_args)
    else:
        print(f"Ошибка: неизвестная команда{command}")
    return "ok"

def run(path):
    try:
        with open(path, "r", encoding = "utf-8") as file:
            for line_number, raw_line in enumerate(file, start = 1):
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
            print(f"VFS>{line}")
            res = execute_command(line)
            if res == "error":
                print( f"Ошибка в стартовом скрипте на строке {line_number}")
            if res == "exit":
                return False
    except(OSError, UnicodeError) as error:
        print(f"Ошибка выполнения стартового скрипта: {error}")

    return True
def main():
    parser = argparse.ArgumentParser(description="Эмулятор командной оболочки VFS")
    parser.add_argument("--vfs", help = "Путь к физическому расположению VFS")
    parser.add_argument("--script", help="Путь к стартовому скрипту")
    options = parser.parse_args()
    print("Параметры запуска: ")
    print("VFS:", options.vfs or "не указан")
    print("Стартовый скрипт:", options.script or "не указан")
    if options.script:
        if not run(options.script):
            return
    while True:
        try:
            user_input = input("VFS> ")
        except(EOFError, KeyboardInterrupt):
            print("\nЗавершение работы VFS.")
            break
        if execute_command(user_input) == "exit":
            break
if __name__ == "__main__":
    main()
