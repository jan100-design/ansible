import os
from pprint import pprint

def list_current_directory():
    # выполнить команду 'ls -la'
    result = os.listdir()

    # вывести результат
    print(result)

if __name__ == "__main__":
    list_current_directory()
