import os
from base64 import standard_b64decode
import subprocess as sp
import sys
import datetime as dt
import time as ti
import psutil
import random as r
import shutil
import requests
from bs4 import BeautifulSoup
import webbrowser
import http.server
import socketserver
import socket
import matplotlib.pyplot as plt


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
        
def exefun():
    print(f"Executing {function}...")
    return

def create_graph():
    # Get user input for the graph title
    graph_title = input("Enter graph title: ")

    # Get user input for x and y coordinates
    x_values = list(map(float, input("Enter x values (comma-separated): ").split(',')))
    y_values = list(map(float, input("Enter y values (comma-separated): ").split(',')))

    # Plot the graph
    plt.plot(x_values, y_values, marker='o')
    plt.title(graph_title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)


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
        elif cmd == "pyfunct":
            try:
                function = input("What Python function do you want to use?")
            except EOFError:
                print("The function didn't work..")

            if function.strip() == "":
                print("No function specified")
            elif function.lower() == "import":
                try:
                    module = input("What module would you like to import?")
                    imported_module = __import__(module)
                    print(f"Module '{module}' imported successfully.")
                    exefun()  # Call the function here
                except ImportError as e:
                    print(f"Error importing module '{module}': {e}")
            else:
                print(f"Executing {function}...")
        if cmd == "ls" or cmd == "list" or cmd == "dirlist":
            files = os.listdir(base_dir)
            print("\n".join(files))
        elif cmd == "therapist":
            print(f"you'll be fine")
        elif cmd == "turtle" or cmd == "programmersturtle" or cmd == "drawturtle":
            run_script('dep/programmersturtle.py')
        elif cmd == "time" or cmd == "currenttime" or cmd == "showtime":
            current_time = dt.datetime.now().strftime("%H:%M:%S")
            print(f"Current time: {current_time}")
        elif cmd == "graph" or cmd == "plan":
            create_graph()
            plt.show()
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
            try:
                query = cmd.split(" ", 1)[1].strip()
                search_url = f'https://www.google.com/search?q={query}'
                webbrowser.open(search_url)
            except requests.RequestException as e:
                print(f"Error during the search: {e}")
        if cmd.startswith("translate "):
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

        if cmd.startswith("quote "):
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
        elif cmd == "webs" or cmd == "websource":
        # Open a local HTML file in the default web browser
            webbrowser.open('http://127.0.0.1:5500/gratitudepay.org/website.html')  # Adjust the URL as needed
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
        # Check if the command starts with 'git'
        if cmd == 'git' or cmd == "gitcmd":
			cmd = input.strip()()
        if cmd == "shutdown" or cmd == "turnoff" or cmd == "poweroff":
            sp.run(['shutdown', '/s'])
        elif cmd == "restart" or cmd == "reboot" or cmd == "softrestart":
            sp.run(['shutdown', '/r'])
        elif cmd == "inst" or cmd == "instantshutdown":
            sp.run(['shutdown', '/s', '00'])
        elif cmd == "insrs" or cmd == "instantrestart":
            sp.run(['shutdown', '/r' '00'])
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
            print("    get (g, fetch)               - Update flash")
            print("    cd [directory] (changedir)   - Change current directory")
            print("    setbase (setbasedir, setdir) - Set base directory")
            print("    ls (list, dirlist)           - List files in the current directory")
            print("    turtle (programmersturtle, drawturtle) - Draw a turtle")
            print("    time (currenttime, showtime) - Display current time")
            print("    !number (randomnumber, randnum) - Generate a random number")
            print("    date (currentdate, showdate) - Display current date")
            print("    whoami (myname, username)    - Display current username")
            print("    !info (flashinfo, information) - Display flash information")
            print("    weather (forecast, getweather) - Check weather")
            print("    randomword (randword, randomtext) - Display a random word")
            print("    download (fetchfile, getfile) - Download a file")
            print("    search [query]               - Search Google")
            print("    translate [text]             - Translate text")
            print("    spotify (music, playmusic)   - Open Spotify")
            print("    calculate [expression]       - Calculate a math expression")
            print("    checkinternet (internetstatus, pinggoogle) - Check internet status")
            print("    calendar (showcalendar, viewcalendar) - Display calendar")
            print("    fortune (randomfortune, showfortune) - Display a random fortune")
            print("    rolladice (dice, rolldice)   - Roll a six-sided dice")
            print("    wiki [topic]                 - Search Wikipedia")
            print("    quote [author]               - Get a random quote by the author")
            print("    info (flashiinfo, information) - Display flash information")
            print("    twister (switchshell, changesystem) - Switch to another shell variant")
            print("    cal (calculator, math)       - Open calculator shell")
            print("    greet (sayhello, hellomessage) - Greet the user")
            print("    echo (repeat, say)           - Repeat a message")
            print("    infinite (repeattext, infiniteprint) - Print a message infinitely")
            print("    uptime (systemuptime, showuptime) - Display system uptime")
            print("    clear (cls, cleanscreen)     - Clear the screen")
            print("    listusb (usblist, showusbdevices) - List connected USB devices")
            print("    custom (customcommand, runcustom) - Run a custom command")
            print("    systeminfo (info, showinfo)  - Display system information")
            print("    netstat (networkstatus, shownetwork) - Display network status")
            print("    chmod [permission] [file]    - Change file permissions")
            print("    tasklist (processlist, showtasks) - List running processes")
            print("    git (rungit, gitcommand)     - Run a Git command")
            print("    shutdown (turnoff, poweroff) - Shutdown the system")
            print("    restart (reboot, softrestart) - Restart the system")
            print("    cpuinfo (processorinfo, showcpuinfo) - Display CPU information")
            print("    mkdir [directory]            - Create a new directory")
            print("    rmdir [directory]            - Remove an empty directory")
            print("    rm [file] (remove)           - Remove a file")
            print("    copy [source] [destination]  - Copy a file")
            print("    rename [old_name] [new_name] - Rename a file or directory")
            print("    listprocesses (showprocesses, processlist) - List running processes")
            print("    kill [pid] (terminate, endprocess) - Terminate a process")
            print("    diskusage (showdiskusage, storageinfo) - Display disk usage")
            print("    help (?)                     - Display this help message")
            print("    exit (quit)                  - Exit flash") 
            print("    graph (plan)                 - Create a graph")          
        elif cmd == "exit" or cmd == "quit":
            print("Exiting flash. Goodbye!")
            sys.exit()
        else:
            print(f"Command not recognized / executed successfully: {cmd}")
    except FileNotFoundError:
        print("No file found. You may need to install it.")
