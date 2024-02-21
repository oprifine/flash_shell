import numpy
import datetime as dt
import time as ti
import os
import subprocess as sp
import sys
import psutil
import shutil

path = os.getcwd()

# Define the base directory for the scripts
base_dir = os.path.join(os.path.expanduser('~/OneDrive/Desktop/flash_shell'))

# Function to run scripts
def run_script(script_name):
    script_path = os.path.join(base_dir, script_name)
    sp.run([sys.executable, script_path])

# Run version script to get the initial version
version_script = 'databases/version.py'
version = sp.run([sys.executable, os.path.join(base_dir, version_script)], capture_output=True, text=True)

print("Setting shell....")
print("Optimizing...")
ti.sleep(0.5)
print("Done loading!")

print("Welcome to flash!")

# Function to run programmersturtle.py
def run_programmersturtle():
    run_script('dep/programmersturtle.py')

# Function to run flashinfo.py
def run_flashinfo():
    run_script('dep/flashinfo.py')

# Function to run flashiinfo.py
def run_flashiinfo():
    run_script('dep/flashiinfo.py')

# Function to run calcshell.py
def run_calcshell():
    run_script('dep/calcshell.py')

while True:
    cmd = input(f"{path}|flash ")

    path = os.getcwd()

    if cmd == "version":
        print(version.stdout)
    elif cmd == "get":
        run_script('databases/installer.py')
    elif cmd.startswith("cd ") or cmd.startswith("changedir "):
        new_path = cmd.split(" ", 1)[1].strip()
        full_path = os.path.join(path, new_path)
        try:
            # Change the directory
            os.chdir(full_path)
            path = os.getcwd()
            print(f"Changed directory to: {path}")
        except FileNotFoundError:
            print(f"Directory not found: {new_path}")
    elif cmd == "ls":
        # List files and directories in the current directory
        files = os.listdir(path)
        print("\n".join(files))
    elif cmd == "turtle":
        run_programmersturtle()
    elif cmd == "time":
        current_time = dt.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
    elif cmd == "date":
        current_date = dt.datetime.now().strftime("%Y-%m-%d")
        print(f"Current date: {current_date}")
    elif cmd == "whoami":
        print(os.getlogin())
    elif cmd == "!info":
        run_flashinfo()
    elif cmd == "info":
        run_flashiinfo()
    elif cmd == "cal":
        run_calcshell()
    elif cmd == "echo":
        message = input("Enter a message to echo: ")
        print(f"Echo: {message}")
    elif cmd == "uptime":
        # Get system uptime using psutil
        uptime_seconds = int(ti.time() - psutil.boot_time())
        uptime_string = str(dt.timedelta(seconds=uptime_seconds))
        print(f"System Uptime: {uptime_string}")
    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == "listusb":
        sp.run(['wmic', 'diskdrive', 'list', 'brief'])
    elif cmd == "systeminfo":
        sp.run(['systeminfo'])
    elif cmd == "netstat":
        sp.run(['netstat', '-a'])
    elif cmd == "tasklist":
        sp.run(['tasklist'])
    elif cmd == "shutdown":
        sp.run(['shutdown', '/s'])
    elif cmd == "restart":
        sp.run(['shutdown', '/r'])
    elif cmd == "cpuinfo":
        # Get CPU information using psutil
        print("CPU Information:")
        print(f"    CPU Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical")
        print(f"    CPU Usage: {psutil.cpu_percent()}%")
    elif cmd.startswith("mkdir "):
        # Create a new directory
        dir_name = cmd.split(" ", 1)[1].strip()
        try:
            os.mkdir(os.path.join(path, dir_name))
            print(f"Directory '{dir_name}' created successfully.")
        except FileExistsError:
            print(f"Directory '{dir_name}' already exists.")
    elif cmd.startswith("rmdir "):
        # Remove a directory
        dir_name = cmd.split(" ", 1)[1].strip()
        try:
            os.rmdir(os.path.join(path, dir_name))
            print(f"Directory '{dir_name}' removed successfully.")
        except FileNotFoundError:
            print(f"Directory '{dir_name}' not found.")
    elif cmd.startswith("rm ") or cmd.startswith("remove "):
        # Remove a file
        file_name = cmd.split(" ", 1)[1].strip()
        try:
            os.remove(os.path.join(path, file_name))
            print(f"File '{file_name}' removed successfully.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
    elif cmd.startswith("copy "):
        # Copy a file
        file_source, file_destination = map(str.strip, cmd.split(" ", 2)[1:])
        try:
            shutil.copyfile(os.path.join(path, file_source), os.path.join(path, file_destination))
            print(f"File '{file_source}' copied to '{file_destination}' successfully.")
        except FileNotFoundError:
            print(f"File '{file_source}' not found.")
        except PermissionError:
            print(f"Permission denied to copy '{file_source}'.")
    elif cmd.startswith("rename "):
        # Rename a file or directory
        old_name, new_name = map(str.strip, cmd.split(" ", 2)[1:])
        try:
            os.rename(os.path.join(path, old_name), os.path.join(path, new_name))
            print(f"Renamed '{old_name}' to '{new_name}' successfully.")
        except FileNotFoundError:
            print(f"File or directory '{old_name}' not found.")
    elif cmd == "listprocesses":
        # List running processes
        processes = psutil.process_iter(['pid', 'name'])
        print("Running Processes:")
        for process in processes:
            print(f"    {process.info['pid']}: {process.info['name']}")
    elif cmd.startswith("kill "):
        # Kill a process by PID
        pid_to_kill = cmd.split(" ", 1)[1].strip()
        try:
            process = psutil.Process(int(pid_to_kill))
            process.terminate()
            print(f"Process with PID {pid_to_kill} terminated successfully.")
        except psutil.NoSuchProcess:
            print(f"No process found with PID {pid_to_kill}.")
    elif cmd == "diskusage":
        # Get disk usage information using psutil
        disk_usage = psutil.disk_usage(path)
        print("Disk Usage Information:")
        print(f"    Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
        print(f"    Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
        print(f"    Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
        print(f"    Disk Usage Percentage: {disk_usage.percent}%")
    elif cmd.startswith("open "):
        # Open a file using the default system program
        file_to_open = cmd.split(" ", 1)[1].strip()
        try:
            sp.run(['open', file_to_open])  # Adjust 'open' based on the operating system
        except FileNotFoundError:
            print(f"File '{file_to_open}' not found.")
        except PermissionError:
            print(f"Permission denied to open '{file_to_open}'.")
    elif cmd == "listenv":
        # List environment variables
        for key, value in os.environ.items():
            print(f"{key}: {value}")
    elif cmd.startswith("setenv "):
        # Set environment variable
        env_var, env_value = map(str.strip, cmd.split(" ", 2)[1:])
        os.environ[env_var] = env_value
        print(f"Environment variable '{env_var}' set to '{env_value}'.")
    elif cmd.startswith("unsetenv "):
        # Unset (remove) environment variable
        env_var_to_unset = cmd.split(" ", 1)[1].strip()
        try:
            del os.environ[env_var_to_unset]
            print(f"Environment variable '{env_var_to_unset}' unset successfully.")
        except KeyError:
            print(f"Environment variable '{env_var_to_unset}' not found.")
    elif cmd == "listaliases":
        # List defined aliases
        print("Defined Aliases:")
        print("    ls -> list")
        print("    cd -> changedir")
        # Add more aliases as needed
    elif cmd.startswith("alias "):
        # Define an alias
        alias_definition = cmd.split(" ", 1)[1].strip()
        alias_name, alias_command = map(str.strip, alias_definition.split("=", 1))
        if alias_name and alias_command:
            locals()[alias_name] = alias_command
            print(f"Alias '{alias_name}' defined successfully.")
        else:
            print("Invalid alias definition. Usage: alias <name> = <command>")
    elif cmd.startswith("unalias "):
        # Remove an alias
        alias_to_remove = cmd.split(" ", 1)[1].strip()
        try:
            # Remove the alias (if exists)
            del locals()[alias_to_remove]
            print(f"Alias '{alias_to_remove}' removed successfully.")
        except KeyError:
            print(f"Alias '{alias_to_remove}' not found.")
    elif cmd == "listusers":
        # List all user accounts on the system
        try:
            users = sp.run(['net', 'user'], capture_output=True, text=True)
            print("List of Users:")
            print(users.stdout)
        except FileNotFoundError:
            print("Command 'net' not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("userinfo "):
        # Get information about a specific user
        username = cmd.split(" ", 1)[1].strip()
        try:
            user_info = sp.run(['net', 'user', username], capture_output=True, text=True)
            print(f"User Information for {username}:")
            print(user_info.stdout)
        except FileNotFoundError:
            print("Command 'net' not found. This command may not work on non-Windows systems.")
    elif cmd == "listgroups":
        # List all groups on the system
        try:
            groups = sp.run(['net', 'localgroup'], capture_output=True, text=True)
            print("List of Groups:")
            print(groups.stdout)
        except FileNotFoundError:
            print("Command 'net' not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("groupinfo "):
        # Get information about a specific group
        groupname = cmd.split(" ", 1)[1].strip()
        try:
            group_info = sp.run(['net', 'localgroup', groupname], capture_output=True, text=True)
            print(f"Group Information for {groupname}:")
            print(group_info.stdout)
        except FileNotFoundError:
            print("Command 'net' not found. This command may not work on non-Windows systems.")
    elif cmd == "ipconfig":
        # Display IP configuration information
        try:
            ipconfig_info = sp.run(['ipconfig'], capture_output=True, text=True)
            print("IP Configuration Information:")
            print(ipconfig_info.stdout)
        except FileNotFoundError:
            print("Command 'ipconfig' not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("ping "):
        # Ping a specific host or IP address
        host = cmd.split(" ", 1)[1].strip()
        try:
            ping_result = sp.run(['ping', '-n', '4', host], capture_output=True, text=True)
            print(f"Ping Result for {host}:")
            print(ping_result.stdout)
        except FileNotFoundError:
            print("Command 'ping' not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("traceroute "):
        # Perform a traceroute to a specific host or IP address
        host = cmd.split(" ", 1)[1].strip()
        try:
            traceroute_result = sp.run(['tracert', host], capture_output=True, text=True)
            print(f"Traceroute Result for {host}:")
            print(traceroute_result.stdout)
        except FileNotFoundError:
            print("Command 'tracert' not found. This command may not work on non-Windows systems.")
    elif cmd == "help":
        print("List of available commands:")
        print("version, get, cd/changedir, ls, turtle, time, date, whoami, !info, info, cal, echo, uptime, clear, listusb, systeminfo, netstat, tasklist, shutdown, restart, cpuinfo, mkdir, rmdir, rm/remove, copy, rename, listprocesses, kill, diskusage, open, listenv, setenv, unsetenv, listaliases, alias, unalias, listusers, userinfo, listgroups, groupinfo, ipconfig, ping, traceroute, help, exit, sourcecode")
    elif cmd == "sourcecode":
        with open(__file__, 'r') as source_code:
            print(source_code.read())
    elif cmd == "exit":
        print("Exiting flash shell. Goodbye!")
        break
    else:
        print(f"Unknown command: {cmd}, please wait for a future version where it might be implemented.")
