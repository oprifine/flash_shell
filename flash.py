import os
import subprocess as sp
import sys
import datetime as dt
import time as ti
import psutil
import random as r
import shutil
import requests
from bs4 import BeautifulSoup

print("Setting shell....")
print("Optimizing...")
ti.sleep(0.5)
print("Done loading!")

print("Welcome to flash!")

base_dir = os.getcwd()


def run_script(script_name, *flags):
    script_path = os.path.join(base_dir, script_name)
    if os.path.exists(script_path):
        command = [sys.executable, script_path, *flags]
        try:
            sp.run(command)
        except FileNotFoundError:
            print(f"Command not found. Please install the necessary tool or check the command.")
    else:
        print(f"Script not found: {script_name}")


def display_system_info():
    print("CPU Information:")
    print(f"    CPU Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical")
    print(f"    CPU Usage: {psutil.cpu_percent()}%")

    disk_usage = psutil.disk_usage(base_dir)
    print("\nDisk Usage Information:")
    print(f"    Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"    Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"    Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
    print(f"    Disk Usage Percentage: {disk_usage.percent}%")


while True:
    cmd = input(f"{base_dir}|flash ")
    try:
        if cmd == "version" or cmd == "ver" or cmd == "v":
            run_script('databases/version.py', "--upgrade", "--flag1", "--flag2", "--flag3")
        elif cmd == "get" or cmd == "g" or cmd == "fetch":
            run_script('databases/installer.py', "--upgrade", "--flag1", "--flag2", "--flag3")
        elif cmd.startswith("cd ") or cmd.startswith("changedir "):
            new_path = cmd.split(" ", 1)[1].strip()
            full_path = os.path.join(base_dir, new_path)
            try:
                os.chdir(full_path)
                base_dir = os.getcwd()
                print(f"Changed directory to: {base_dir}")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error: {e}")
        elif cmd == "setbase" or cmd == "setbasedir" or cmd == "setdir":
            new_base_dir = input("Enter the new base directory: ").strip()
            if os.path.exists(new_base_dir) and os.path.isdir(new_base_dir):
                base_dir = os.path.abspath(new_base_dir)
                print(f"Base directory set to: {base_dir}")
            else:
                print(f"Invalid directory: {new_base_dir}")
        elif cmd == "ls" or cmd == "list" or cmd == "dirlist":
            files = os.listdir(base_dir)
            print("\n".join(files))
        elif cmd == "therapist":
            print(f"you'll be fine")
        elif cmd == "turtle" or cmd == "programmersturtle" or cmd == "drawturtle":
            run_script('dep/programmersturtle.py')
        elif cmd == "time" or cmd == "currenttime" or cmd == "showtime":
            current_time = dt.datetime.now().strftime("%H:%M:%S")
            print(f"Current time: {current_time}")
        elif cmd == "!number" or cmd == "randomnumber" or cmd == "randnum":
            random_number = r.randint(0, 100)
            print(random_number)
        elif cmd == "date" or cmd == "currentdate" or cmd == "showdate":
            current_date = dt.datetime.now().strftime("%Y-%m-%d")
            print(f"Current date: {current_date}")
        elif cmd == "whoami" or cmd == "myname" or cmd == "username":
            print(os.getlogin())
        elif cmd == "!info" or cmd == "flashinfo" or cmd == "information":
            run_script('dep/flashinfo.py')
        elif cmd == "weather" or cmd == "forecast" or cmd == "getweather":
            city = input("Enter the city for weather information: ")
            sp.run(['curl', f'wttr.in/{city}'])
        elif cmd == "randomword" or cmd == "randword" or cmd == "randomtext":
            response = requests.get('https://randomword.com/')
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                random_word = soup.find('div', {'id': 'random_word'}).text
                print(random_word)
            else:
                print(f"Failed to fetch a random word. Status code: {response.status_code}")
        elif cmd == "download" or cmd == "fetchfile" or cmd == "getfile":
            url = input("Enter the URL to download: ")
            try:
                sp.run(['wget', url])
                print(f"Downloaded successfully from {url}.")
            except FileNotFoundError:
                print("Command 'wget' not found. Please install it to use this command.")
        elif cmd == "hawks":
            print("WE ARE THE BEST SCHOOL EVER!!!")
        elif cmd.startswith("search "):
            query = cmd.split(" ", 1)[1].strip()
            sp.run(['curl', f'https://www.google.com/search?q={query}'])
        elif cmd.startswith("translate "):
            text_to_translate = cmd.split(" ", 1)[1].strip()
            sp.run(['trans', text_to_translate])
        elif cmd == "spotify" or cmd == "music" or cmd == "playmusic":
            sp.run(['spotify'])
        elif cmd.startswith("calculate "):
            expression = cmd.split(" ", 1)[1].strip()
            sp.run(['python', '-c', f'print({expression})'])
        elif cmd == "checkinternet" or cmd == "internetstatus" or cmd == "pinggoogle":
            sp.run(['ping', '-c', '4', '8.8.8.8'])
        elif cmd == "calendar" or cmd == "showcalendar" or cmd == "viewcalendar":
            sp.run(['cal'])
        elif cmd == "fortune" or cmd == "randomfortune" or cmd == "showfortune":
            print("A fun social event is in your near future.")
        elif cmd == "rolladice" or cmd == "dice" or cmd == "rolldice":
            sp.run(['shuf', '-i', '1-6', '-n', '1'])
        elif cmd.startswith("wiki "):
            topic = cmd.split(" ", 1)[1].strip()
            sp.run(['curl', f'https://en.wikipedia.org/wiki/{topic}'])
        elif cmd.startswith("quote "):
            author = cmd.split(" ", 1)[1].strip()
            sp.run(['curl', f'https://api.quotable.io/random?author={author}'])
        elif cmd == "info" or cmd == "flashiinfo" or cmd == "information":
            run_script('dep/flashiinfo.py')
        elif cmd == "twister" or cmd == "switchshell" or cmd == "changesystem":
            twistos = input("What variant do you want to switch to? (Just input 'flash' if you want to go back to the original shell.) ")
            if twistos in ('zsh', 'bash', 'csh', 'powershell', 'fish', 'pufferfish'):
                sp.run(['python', f'flash{twistos}.py'])
            else:
                sp.run(['python', 'flash.py'])
        elif cmd == "cal" or cmd == "calculator" or cmd == "math":
            run_script('dep/calcshell.py')
        elif cmd == "greet" or cmd == "sayhello" or cmd == "hellomessage":
            name = input("What is your name?")
            print("Hello,", name, "!")
        elif cmd == "echo" or cmd == "repeat" or cmd == "say":
            message = input("Enter a message to echo: ")
            print(f"Echo: {message}")
        elif cmd == "infinite" or cmd == "repeattext" or cmd == "infiniteprint":
            while_text = input("Enter text: ")
            while True:
                print(while_text)
        elif cmd == "uptime" or cmd == "systemuptime" or cmd == "showuptime":
            uptime_seconds = int(ti.time() - psutil.boot_time())
            uptime_string = str(dt.timedelta(seconds=uptime_seconds))
            print(f"System Uptime: {uptime_string}")
        elif cmd == "clear" or cmd == "cls" or cmd == "cleanscreen":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif cmd == "listusb" or cmd == "usblist" or cmd == "showusbdevices":
            sp.run(['wmic', 'diskdrive', 'list', 'brief'])
        elif cmd == "custom" or cmd == "customcommand" or cmd == "runcustom":
            print(locals())  # or print(globals())
        elif cmd == "systeminfo" or cmd == "info" or cmd == "showinfo":
            sp.run(['systeminfo'])
        elif cmd == "netstat" or cmd == "networkstatus" or cmd == "shownetwork":
            sp.run(['netstat', '-a'])
        elif cmd.startswith("chmod "):
            try:
                permission, file_name = cmd.split(" ", 2)[1:]
                permission = int(permission, 8)
                os.chmod(os.path.join(base_dir, file_name), permission)
                print(f"Permissions for '{file_name}' changed successfully.")
            except (ValueError, FileNotFoundError) as e:
                print(f"Error: {e}")
        elif cmd == "tasklist" or cmd == "processlist" or cmd == "showtasks":
            sp.run(['tasklist'])
        elif cmd == "git" or cmd == "rungit" or cmd == "gitcommand":
            git_command = input("Enter Git command: ")
            sp.run(['git', git_command])
        elif cmd == "shutdown" or cmd == "turnoff" or cmd == "poweroff":
            sp.run(['shutdown', '/s'])
        elif cmd == "restart" or cmd == "reboot" or cmd == "softrestart":
            sp.run(['shutdown', '/r'])
        elif cmd == "cpuinfo" or cmd == "processorinfo" or cmd == "showcpuinfo":
            print("CPU Information:")
            print(f"    CPU Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical")
            print(f"    CPU Usage: {psutil.cpu_percent()}%")
        elif cmd.startswith("mkdir "):
            dir_name = cmd.split(" ", 1)[1].strip()
            try:
                os.mkdir(os.path.join(base_dir, dir_name))
                print(f"Directory '{dir_name}' created successfully.")
            except FileExistsError:
                print(f"Directory '{dir_name}' already exists.")
        elif cmd.startswith("rmdir "):
            dir_name = cmd.split(" ", 1)[1].strip()
            try:
                os.rmdir(os.path.join(base_dir, dir_name))
                print(f"Directory '{dir_name}' removed successfully.")
            except FileNotFoundError:
                print(f"Directory '{dir_name}' not found.")
        elif cmd.startswith("rm ") or cmd.startswith("remove "):
            file_name = cmd.split(" ", 1)[1].strip()
            try:
                os.remove(os.path.join(base_dir, file_name))
                print(f"File '{file_name}' removed successfully.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
        elif cmd.startswith("copy "):
            file_source, file_destination = map(str.strip, cmd.split(" ", 2)[1:])
            try:
                shutil.copyfile(os.path.join(base_dir, file_source), os.path.join(base_dir, file_destination))
                print(f"File '{file_source}' copied to '{file_destination}' successfully.")
            except FileNotFoundError:
                print(f"File '{file_source}' not found.")
            except PermissionError:
                print(f"Permission denied to copy '{file_source}'.")
        elif cmd.startswith("rename "):
            old_name, new_name = map(str.strip, cmd.split(" ", 2)[1:])
            try:
                os.rename(os.path.join(base_dir, old_name), os.path.join(base_dir, new_name))
                print(f"Renamed '{old_name}' to '{new_name}' successfully.")
            except FileNotFoundError:
                print(f"File or directory '{old_name}' not found.")
        elif cmd == "listprocesses" or cmd == "showprocesses" or cmd == "processlist":
            processes = psutil.process_iter(['pid', 'name'])
            print("Running Processes:")
            for process in processes:
                print(f"    {process.info['pid']}: {process.info['name']}")
        elif cmd.startswith("kill ") or cmd.startswith("terminate ") or cmd.startswith("endprocess "):
            pid_to_kill = cmd.split(" ", 1)[1].strip()
            try:
                process = psutil.Process(int(pid_to_kill))
                process.terminate()
                print(f"Process with PID {pid_to_kill} terminated successfully.")
            except psutil.NoSuchProcess:
                print(f"No process found with PID {pid_to_kill}.")
        elif cmd == "diskusage" or cmd == "showdiskusage" or cmd == "storageinfo":
            disk_usage = psutil.disk_usage(base_dir)
            print("Disk Usage Information:")
            print(f"    Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
            print(f"    Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
            print(f"    Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
            print(f"    Disk Usage Percentage: {disk_usage.percent}%")
        elif cmd == "help" or cmd == "?":
            print("Available commands:")
            print("    version (ver, v)             - Check flash version")
            # ... (rest of the commands)
            print("    exit (quit)                  - Exit flash")
        elif cmd == "exit" or cmd == "quit":
            print("Exiting flash. Goodbye!")
            sys.exit()
        else:
            print(f"Command not recognized: {cmd}")
    except FileNotFoundError:
        print("No file found. You may need to install it.")