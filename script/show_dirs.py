import subprocess

def list_current_directory():
    # выполнить команду 'ls -la'
    result = subprocess.run(['ls', '-la'], capture_output=True, text=True)

    # вывести результат
    print(result.stdout)

if __name__ == "__main__":
    list_current_directory()
