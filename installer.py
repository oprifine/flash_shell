import subprocess
import sys

def install_package(package_manager, package_name):
    try:
        if package_manager == 'apt':
            subprocess.check_call(['sudo', 'apt', 'install', package_name])
        elif package_manager == 'pip':
            subprocess.check_call(['pip', 'install', package_name])
        elif package_manager == 'winget':
            subprocess.check_call(['winget', 'install', package_name])
        elif package_manager == 'yum':
            subprocess.check_call(['sudo', 'yum', 'install', package_name])
        elif package_manager == 'dnf':
            subprocess.check_call(['sudo', 'dnf', 'install', package_name])
        elif package_manager == 'exit':
            sys.exit(0)
        else:
            print(f"Error: Unsupported package manager '{package_manager}'.")
            return
        
        print(f"Package '{package_name}' installed successfully using {package_manager}.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to install package '{package_name}' using {package_manager}.")

def choose_package_manager():
    print("Choose a package manager:")
    print("1. apt")
    print("2. pip")
    print("3. winget")
    print("4. yum")
    print("5. dnf")
    print("6. exit")

    choice = input("Enter the number corresponding to your choice: ")
    return {
        '1': 'apt',
        '2': 'pip',
        '3': 'winget',
        '4': 'yum',
        '5': 'dnf',
        '6': 'exit'
    }.get(choice, 'exit')

if __name__ == "__main__":
    package_manager = choose_package_manager()

    if package_manager == 'exit':
        sys.exit(0)

    package_name = input("Enter the name of the package to install: ")
    install_package(package_manager, package_name)