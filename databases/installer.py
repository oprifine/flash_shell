import subprocess as sp

print("Welcome to the flash package installer!")
mng = input("What manager do you use?\n"
             "|apt| Linux package manager.\n"
             "|yum| Linux package manager.\n"
             "|winget| Windows package manager.\n"
             "|pip| Python package/module manager.\n"
             "|exit| Exit this manager. ")
pkg = input("What package do you want to install/uninstall? ")

# Ensure the user input is lowercase for case-insensitive comparison
mng = mng.lower()

# Prompt the user for flags
use_flags = input("Do you want to use flags? (yes/no): ").lower()
flags = ""
if use_flags == "yes":
    flags = input("Enter flags (separated by space): ")

if mng == "apt":
    command = f"sudo apt install {pkg} {flags}"
elif mng == "yum":
    command = f"sudo yum install {pkg} {flags}"
elif mng == "winget":
    command = f"winget install {pkg} {flags}"
elif mng == "pip":
    command = f"pip install {pkg} {flags}"
elif mng == "exit":
    print("Exiting the manager.")
    exit()
elif mng == "vscode":
    command = f"code"
else:
    print("Invalid manager choice. Exiting.")
    exit()

try:
    # Run the command using subprocess
    sp.run(command, shell=True, check=True)
    print(f"{pkg} has been successfully installed/uninstalled using {mng}.")
except sp.CalledProcessError as e:
    print(f"Error: {e}")