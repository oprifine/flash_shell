import os
import subprocess as sp
import sys
import turtle
import datetime as dt
import time as ti
import psutil
import random as r
import shutil

print("Setting shell....")
print("Optimizing...")
ti.sleep(0.5)
print("Done loading!")

print("Welcome to flash!")

base_dir = os.getcwd()


def run_script(script_name, upgrade=False, flag1=False, flag2=False, flag3=False):
    script_path = os.path.join(base_dir, script_name)
    if os.path.exists(script_path):
        command = [sys.executable, script_path]
        if upgrade:
            command.append("--upgrade")
        if flag1:
            command.append("--flag1")
        if flag2:
            command.append("--flag2")
        if flag3:
            command.append("--flag3")
        sp.run(command)
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

    if cmd == "version":
        run_script('databases/version.py', upgrade=True, flag1=True, flag2=True, flag3=True)
    elif cmd == "get":
        run_script('databases/installer.py', upgrade=True, flag1=True, flag2=True, flag3=True)
    elif cmd.startswith("cd ") or cmd.startswith("changedir "):
        new_path = cmd.split(" ", 1)[1].strip()
        full_path = os.path.join(base_dir, new_path)
        try:
            os.chdir(full_path)
            base_dir = os.getcwd()
            print(f"Changed directory to: {base_dir}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error: {e}")
    elif cmd == "setbase":
        new_base_dir = input("Enter the new base directory: ").strip()
        if os.path.exists(new_base_dir) and os.path.isdir(new_base_dir):
            base_dir = os.path.abspath(new_base_dir)
            print(f"Base directory set to: {base_dir}")
        else:
            print(f"Invalid directory: {new_base_dir}")
    elif cmd == "ls":
        files = os.listdir(base_dir)
        print("\n".join(files))
    elif cmd == "turtle":
        run_script('dep/programmersturtle.py')
    elif cmd == "time":
        current_time = dt.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
    elif cmd == "!number":
        random_number = r.randint(0, 100)
        print(random_number)
    elif cmd == "date":
        current_date = dt.datetime.now().strftime("%Y-%m-%d")
        print(f"Current date: {current_date}")
    elif cmd == "whoami":
        print(os.getlogin())
    elif cmd == "!info":
        run_script('dep/flashinfo.py')
    elif cmd == "weather":
        city = input("Enter the city for weather information: ")
        sp.run(['curl', f'wttr.in/{city}'])
    elif cmd == "randomword":
        sp.run(['curl', 'randomword.com'])
    elif cmd == "download":
        url = input("Enter the URL to download: ")
        try:
            sp.run(['wget', url])
            print(f"Downloaded successfully from {url}.")
        except FileNotFoundError:
            print("Command 'wget' not found. Please install it to use this command.")
    elif cmd.startswith("search "):
        query = cmd.split(" ", 1)[1].strip()
        sp.run(['curl', f'https://www.google.com/search?q={query}'])
    elif cmd.startswith("translate "):
        text_to_translate = cmd.split(" ", 1)[1].strip()
        sp.run(['trans', text_to_translate])
    elif cmd == "spotify":
        sp.run(['spotify'])
    elif cmd.startswith("calculate "):
        expression = cmd.split(" ", 1)[1].strip()
        sp.run(['python', '-c', f'print({expression})'])
    elif cmd == "checkinternet":
        sp.run(['ping', '-c', '4', '8.8.8.8'])
    elif cmd == "calendar":
        sp.run(['cal'])
    elif cmd == "fortune":
        sp.run(['fortune'])
    elif cmd == "rolladice":
        sp.run(['shuf', '-i', '1-6', '-n', '1'])
    elif cmd.startswith("wiki "):
        topic = cmd.split(" ", 1)[1].strip()
        sp.run(['curl', f'https://en.wikipedia.org/wiki/{topic}'])
    elif cmd.startswith("quote "):
        author = cmd.split(" ", 1)[1].strip()
        sp.run(['curl', f'https://api.quotable.io/random?author={author}'])
    elif cmd == "info":
        run_script('dep/flashiinfo.py')
    elif cmd == "twister":
        twistos = input("What variant do you want to switch to? (Just input 'flash' if you want to go back to the original shell.) ")
        if twistos in ('zsh', 'bash', 'csh', 'powershell', 'fish', 'pufferfish'):
            sp.run(['python', f'flash{twistos}.py'])
        else:
            sp.run(['python', 'flash.py'])
    elif cmd == "cal":
        run_script('dep/calcshell.py')
    elif cmd == "greet":
        name = input("What is your name?")
        print("Hello,", name, "!")
    elif cmd == "echo":
        message = input("Enter a message to echo: ")
        print(f"Echo: {message}")
    elif "fuck" in cmd:
        print("no.")
    elif cmd == "infinite":
        while_text = input("Enter text: ")
        while True:
            print(while_text)
    elif cmd == "uptime":
        uptime_seconds = int(ti.time() - psutil.boot_time())
        uptime_string = str(dt.timedelta(seconds=uptime_seconds))
        print(f"System Uptime: {uptime_string}")
    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == "listusb":
        sp.run(['wmic', 'diskdrive', 'list', 'brief'])
    elif cmd == "custom":
        print(vars)
    elif cmd == "systeminfo":
        sp.run(['systeminfo'])
    elif cmd == "netstat":
        sp.run(['netstat', '-a'])
    elif cmd.startswith("chmod "):
        try:
            permission, file_name = cmd.split(" ", 2)[1:]
            permission = int(permission, 8)
            os.chmod(os.path.join(base_dir, file_name), permission)
            print(f"Permissions for '{file_name}' changed successfully.")
        except (ValueError, FileNotFoundError) as e:
            print(f"Error: {e}")
    elif cmd == "tasklist":
        sp.run(['tasklist'])
    elif cmd == "git":
        git_command = input("Enter Git command: ")
        sp.run(['git', git_command])
    elif cmd == "shutdown":
        sp.run(['shutdown', '/s'])
    elif cmd == "restart":
        sp.run(['shutdown', '/r'])
    elif cmd == "cpuinfo":
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
    elif cmd == "listprocesses":
        processes = psutil.process_iter(['pid', 'name'])
        print("Running Processes:")
        for process in processes:
            print(f"    {process.info['pid']}: {process.info['name']}")
    elif cmd.startswith("kill "):
        pid_to_kill = cmd.split(" ", 1)[1].strip()
        try:
            process = psutil.Process(int(pid_to_kill))
            process.terminate()
            print(f"Process with PID {pid_to_kill} terminated successfully.")
        except psutil.NoSuchProcess:
            print(f"No process found with PID {pid_to_kill}.")
    elif cmd == "diskusage":
        disk_usage = psutil.disk_usage(base_dir)
        print("Disk Usage Information:")
        print(f"    Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
        print(f"    Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
        print(f"    Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
        print(f"    Disk Usage Percentage: {disk_usage.percent}%")
    elif cmd.startswith("open "):
        file_to_open = cmd.split(" ", 1)[1].strip()
        try:
            sp.run(['open', file_to_open])
        except FileNotFoundError:
            print(f"File '{file_to_open}' not found.")
        except PermissionError:
            print(f"Permission denied to open '{file_to_open}'.")
    elif cmd == "listenv":
        for key, value in os.environ.items():
            print(f"{key}: {value}")
    elif cmd.startswith("setenv "):
        env_var, env_value = map(str.strip, cmd.split(" ", 2)[1:])
        os.environ[env_var] = env_value
        print(f"Environment variable '{env_var}' set to '{env_value}'.")
    elif cmd.startswith("unsetenv "):
        env_var_to_unset = cmd.split(" ", 1)[1].strip()
        try:
            del os.environ[env_var_to_unset]
            print(f"Environment variable '{env_var_to_unset}' unset successfully.")
        except KeyError:
            print(f"Environment variable '{env_var_to_unset}' not found.")
    elif cmd == "listaliases":
        print("Defined Aliases:")
        print("    ls -> list")
        print("    cd -> changedir")
    elif cmd.startswith("alias "):
        alias_definition = cmd.split(" ", 1)[1].strip()
        alias_name, alias_command = map(str.strip, alias_definition.split("=", 1))
        if alias_name and alias_command:
            locals()[alias_name] = alias_command
            print(f"Alias '{alias_name}' defined successfully.")
        else:
            print("Invalid alias definition. Usage: alias <name> = <command>")
    elif cmd.startswith("unalias "):
        alias_to_remove = cmd.split(" ", 1)[1].strip()
        try:
            del locals()[alias_to_remove]
            print(f"Alias '{alias_to_remove}' removed successfully.")
        except KeyError:
            print(f"Alias '{alias_to_remove}' not found.")
    elif cmd == "listusers":
        try:
            users = sp.run(['net', 'user'], capture_output=True, text=True)
            print("List of Users:")
            print(users.stdout)
        except FileNotFoundError:
            print("Command 'net' not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("userinfo "):
        username = cmd.split(" ", 1)[1].strip()
        try:
            user_info = sp.run(['net', 'user', username], capture_output=True, text=True)
            print(f"User Information for {username}:")
            print(user_info.stdout)
        except FileNotFoundError:
            print("Command 'net' not found. This command may not work on non-Windows systems.")
    elif cmd == "listgroups":
        try:
            groups = sp.run(['net', 'localgroup'], capture_output=True, text=True)
            print("List of Groups:")
            print(groups.stdout)
        except FileNotFoundError:
            print("Command 'net' not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("groupinfo "):
        groupname = cmd.split(" ", 1)[1].strip()
        try:
            group_info = sp.run(['net', 'localgroup', groupname], capture_output=True, text=True)
            print(f"Group Information for {groupname}:")
            print(group_info.stdout)
        except FileNotFoundError:
            print("Command 'net' not found. This command may not work on non-Windows systems.")
    elif cmd == "ipconfig":
        try:
            ipconfig_info = sp.run(['ipconfig'], capture_output=True, text=True)
            print("IP Configuration Information:")
            print(ipconfig_info.stdout)
        except FileNotFoundError:
            print("Command 'ipconfig' not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("ping "):
        host = cmd.split(" ", 1)[1].strip()
        try:
            ping_result = sp.run(['ping', '-n', '4', host], capture_output=True, text=True)
            print(f"Ping Result for {host}:")
            print(ping_result.stdout)
        except FileNotFoundError:
            print("Command 'ping' not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("traceroute "):
        host = cmd.split(" ", 1)[1].strip()
        try:
            traceroute_result = sp.run(['tracert', host], capture_output=True, text=True)
            print(f"Traceroute Result for {host}:")
            print(traceroute_result.stdout)
        except FileNotFoundError:
            print("Command 'tracert' not found. This command may not work on non-Windows systems.")
    elif cmd == "help":
        print("List of available commands:")
        print("version - Display the current version of the flash shell.")
        print("get - Run the installer script.")
        print("cd/changedir <directory> - Change the current working directory.")
        print("ls - List files and directories in the current directory.")
        print("turtle - Run the programmersturtle script.")
        print("time - Display the current time.")
        print("date - Display the current date.")
        print("whoami - Display the current username.")
        print("!info - Run the flashinfo script.")
        print("info - Run the flashiinfo script.")
        print("cal - Run the calcshell script.")
        print("echo - Echo a message.")
        print("infinite - Print a given text infinitely.")
        print("!number - Selects random number.")
        print("uptime - Display system uptime.")
        print("clear - Clear the terminal screen.")
        print("listusb - List connected USB devices.")
        print("systeminfo - Display system information.")
        print("netstat - Display network connections.")
        print("chmod <permission> <file_name> - Change file permissions.")
        print("tasklist - Display a list of running processes.")
        print("git - Run a Git command.")
        print("c, java, cpp, bf - Emulators for these languages. C, Java, C++, and .bf")
        print("shutdown - Shut down the system.")
        print("restart - Restart the system.")
        print("cpuinfo - Display CPU information.")
        print("mkdir <directory> - Create a new directory.")
        print("rmdir <directory> - Remove an empty directory.")
        print("rm/remove <file> - Remove a file.")
        print("copy <source> <destination> - Copy a file.")
        print("rename <old_name> <new_name> - Rename a file.")
        print("listprocesses - List running processes.")
        print("kill <pid> - Terminate a process by PID.")
        print("diskusage - Display disk usage information.")
        print("open <file> - Open a file.")
        print("listenv - List environment variables.")
        print("setenv <variable> <value> - Set an environment variable.")
        print("unsetenv <variable> - Unset an environment variable.")
        print("listaliases - List defined aliases.")
        print("alias <name> = <command> - Define an alias.")
        print("unalias <name> - Remove an alias.")
        print("listusers - List user accounts.")
        print("userinfo <username> - Display information about a user.")
        print("listgroups - List local groups.")
        print("groupinfo <groupname> - Display information about a group.")
        print("ipconfig - Display IP configuration.")
        print("ping <host> - Ping a host.")
        print("traceroute <host> - Perform a traceroute to a host.")
        print("help - Display this help message.")
        print("exit - Exit the flash shell.")
        print("sourcecode - Display the source code of the flash shell.")
        print("download <url> - Downloads from the internet.")
        print("cowsay <input> - The cow says something.")
        print("nmap <target/ip address> - Finds the location?")
        print("adduser <username> - Adds a user to the system.")
        print("publicip - Finds your public ip (e.g 69.696.666.66)")
        print("randomword - Prints a random word.")
        print("search <query> - Searches Google for the query.")
        print("translate <text> - Translates the text to English.")
        print("spotify - Opens Spotify.")
        print("calculate <expression> - Evaluates a mathematical expression.")
        print("checkinternet - Checks internet connection.")
        print("calendar - Displays calendar.")
        print("fortune - Displays a fortune.")
        print("rolladice - Rolls a six-sided dice.")
        print("wiki <topic> - Opens Wikipedia page for the topic.")
        print("quote <author> - Displays a random quote by the author.")
        print("twister - Switch to another shell variant.")
        print("greet - Greets the user.")
    elif cmd == "exit":
        print("Exiting flash...")
        break
    elif cmd == "sourcecode":
        run_script('dep/sourcecode.py')
    elif cmd.startswith("cowsay "):
        message = cmd.split(" ", 1)[1].strip()
        sp.run(['cowsay', message])
    elif cmd.startswith("nmap "):
        target = cmd.split(" ", 1)[1].strip()
        sp.run(['nmap', target])
    elif cmd.startswith("adduser "):
        username = cmd.split(" ", 1)[1].strip()
        sp.run(['net', 'user', username])
    elif cmd == "publicip":
        sp.run(['curl', 'ifconfig.me'])
    else:
        print(f"Command not found: {cmd}")