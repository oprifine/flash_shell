#!/usr/bin/env python3

import os
import subprocess as sp
import sys
import datetime as dt
import time as ti
import psutil
import shutil

base_dir = os.getcwd()

def run_script(script_name):
    script_path = os.path.join(base_dir, script_name)
    if os.path.exists(script_path):
        sp.run([sys.executable, script_path])
    else:
        print(f"bash: {script_name}: command not found")

version_script = 'databases/version.py'
version = sp.run([sys.executable, os.path.join(base_dir, version_script)], capture_output=True, text=True)

print("Setting shell....")
print("Optimizing...")
ti.sleep(0.5)
print("Done loading!")

print("Welcome to flash!")

def run_programmersturtle():
    run_script('dep/programmersturtle.py')

def run_flashinfo():
    run_script('dep/flashinfo.py')

def run_flashiinfo():
    run_script('dep/flashiinfo.py')

def run_calcshell():
    run_script('dep/calcshell.py')

# Thank y'all for viewing this!

while True:
    cmd = input(f"{base_dir}|bash ")

    path = os.getcwd()

    if cmd == "version":
        print(version.stdout)
    elif cmd == "get":
        run_script('databases/installer.py')
    elif cmd.startswith("cd ") or cmd.startswith("changedir "):
        new_path = cmd.split(" ", 1)[1].strip()
        full_path = os.path.join(path, new_path)
        try:
            os.chdir(full_path)
            base_dir = os.getcwd()  # Update base_dir to the new current directory
            print(f"bash: cd: {base_dir}: No such file or directory")
        except FileNotFoundError:
            print(f"bash: cd: {new_path}: No such file or directory")
        except PermissionError:
            print(f"bash: cd: {new_path}: Permission denied")
    elif cmd == "setbase":
        new_base_dir = input("Enter the new base directory: ").strip()
        if os.path.exists(new_base_dir) and os.path.isdir(new_base_dir):
            base_dir = os.path.abspath(new_base_dir)
            print(f"bash: setbase: {base_dir}: No such file or directory")
        else:
            print(f"bash: setbase: {new_base_dir}: No such file or directory")
    elif cmd == "ls":
        files = os.listdir(base_dir)  # Use base_dir instead of path
        print("\n".join(files))
    elif cmd == "turtle":
        run_programmersturtle()
    elif cmd == "time":
        current_time = dt.datetime.now().strftime("%H:%M:%S")
        print(f"bash: time: {current_time}")
    elif cmd == "date":
        current_date = dt.datetime.now().strftime("%Y-%m-%d")
        print(f"bash: date: {current_date}")
    elif cmd == "whoami":
        print(os.getlogin())
    elif cmd == "!info":
        run_flashinfo()
     
    elif cmd == "info":
        run_flashiinfo()
    elif cmd == "twister":
        twistos = input("What variant do you want to switch to? (Just input 'flash' if you want to go back to the original shell.) ")
        if twistos in ('zsh', 'bash', 'csh', 'powershell', 'fish', 'pufferfish', ):
            sp.run(['python', f'flash{twistos}.py'])
        else:
            sp.run(['python', 'flash.py'])
    elif cmd == "cal":
        run_calcshell()
    elif cmd == "echo":
        message = input("Enter a message to echo: ")
        print(f"bash: echo: {message}")
    elif cmd == "infinite":
        while_text = input("Enter text: ")
        while True:
            print(while_text)
    elif cmd == "uptime":
        uptime_seconds = int(ti.time() - psutil.boot_time())
        uptime_string = str(dt.timedelta(seconds=uptime_seconds))
        print(f"bash: uptime: {uptime_string}")
    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == "listusb":
        sp.run(['wmic', 'diskdrive', 'list', 'brief'])
    elif cmd == "systeminfo":
        sp.run(['systeminfo'])
    elif cmd == "netstat":
        sp.run(['netstat', '-a'])
    elif cmd.startswith("chmod "):
        try:
            permission, file_name = cmd.split(" ", 2)[1:]
            permission = int(permission, 8)  # Convert octal to decimal
            os.chmod(os.path.join(path, file_name), permission)
            print(f"bash: chmod: changing permissions of '{file_name}': No such file or directory")
        except (ValueError, FileNotFoundError) as e:
            print(f"bash: chmod: {e}")
    elif cmd == "tasklist":
        sp.run(['tasklist'])
    elif cmd == "git":
        git_command = input("Enter Git command: ")
        # Assuming run_git is defined elsewhere
        sp.run(['git', git_command])
    elif cmd.startswith("bf "):
        print("bash: bf: command not found")
    elif cmd == "shutdown":
        sp.run(['shutdown', '/s'])
    elif cmd == "restart":
        sp.run(['shutdown', '/r'])
    elif cmd == "cpuinfo":
        print("bash: cpuinfo: command not found")
    elif cmd.startswith("mkdir "):
        dir_name = cmd.split(" ", 1)[1].strip()
        try:
            os.mkdir(os.path.join(base_dir, dir_name))  # Use base_dir instead of path
            print(f"bash: mkdir: {dir_name}: File exists")
        except FileExistsError:
            print(f"bash: mkdir: {dir_name}: File exists")
    elif cmd.startswith("rmdir "):
        dir_name = cmd.split(" ", 1)[1].strip()
        try:
            os.rmdir(os.path.join(base_dir, dir_name))  # Use base_dir instead of path
            print(f"bash: rmdir: {dir_name}: No such file or directory")
        except FileNotFoundError:
            print(f"bash: rmdir: {dir_name}: No such file or directory")
    elif cmd.startswith("rm ") or cmd.startswith("remove "):
        file_name = cmd.split(" ", 1)[1].strip()
        try:
            os.remove(os.path.join(base_dir, file_name))  # Use base_dir instead of path
            print(f"bash: rm: cannot remove '{file_name}': No such file or directory")
        except FileNotFoundError:
            print(f"bash: rm: cannot remove '{file_name}': No such file or directory")
    elif cmd.startswith("copy "):
        file_source, file_destination = map(str.strip, cmd.split(" ", 2)[1:])
        try:
            shutil.copyfile(os.path.join(base_dir, file_source), os.path.join(base_dir, file_destination))  # Use base_dir instead of path
            print(f"bash: copy: {file_source}: No such file or directory")
        except FileNotFoundError:
            print(f"bash: copy: {file_source}: No such file or directory")
        except PermissionError:
            print(f"bash: copy: {file_source}: Permission denied")
    elif cmd.startswith("rename "):
        old_name, new_name = map(str.strip, cmd.split(" ", 2)[1:])
        try:
            os.rename(os.path.join(base_dir, old_name), os.path.join(base_dir, new_name))  # Use base_dir instead of path
            print(f"bash: rename: {old_name}: No such file or directory")
        except FileNotFoundError:
            print(f"bash: rename: {old_name}: No such file or directory")
    elif cmd == "listprocesses":
        processes = psutil.process_iter(['pid', 'name'])
        print("bash: listprocesses: command not found")
    elif cmd.startswith("kill "):
        pid_to_kill = cmd.split(" ", 1)[1].strip()
        try:
            process = psutil.Process(int(pid_to_kill))
            process.terminate()
            print(f"bash: kill: {pid_to_kill}: No such process")
        except psutil.NoSuchProcess:
            print(f"bash: kill: {pid_to_kill}: No such process")
    elif cmd == "diskusage":
        disk_usage = psutil.disk_usage(base_dir)  # Use base_dir instead of path
        print("bash: diskusage: command not found")
    elif cmd.startswith("open "):
        file_to_open = cmd.split(" ", 1)[1].strip()
        try:
            sp.run(['open', file_to_open])  # Adjust 'open' based on the operating system
        except FileNotFoundError:
            print(f"bash: open: {file_to_open}: No such file or directory")
        except PermissionError:
            print(f"bash: open: {file_to_open}: Permission denied")
    elif cmd == "listenv":
        for key, value in os.environ.items():
            print(f"{key}={value}")
    elif cmd.startswith("setenv "):
        env_var, env_value = map(str.strip, cmd.split(" ", 2)[1:])
        os.environ[env_var] = env_value
        print(f"bash: setenv: {env_var}: No such file or directory")
    elif cmd.startswith("unsetenv "):
        env_var_to_unset = cmd.split(" ", 1)[1].strip()
        try:
            del os.environ[env_var_to_unset]
            print(f"bash: unsetenv: {env_var_to_unset}: No such file or directory")
        except KeyError:
            print(f"bash: unsetenv: {env_var_to_unset}: No such file or directory")
    elif cmd == "listaliases":
        print("bash: listaliases: command not found")
    elif cmd.startswith("alias "):
        alias_definition = cmd.split(" ", 1)[1].strip()
        alias_name, alias_command = map(str.strip, alias_definition.split("=", 1))
        if alias_name and alias_command:
            locals()[alias_name] = alias_command
            print(f"bash: alias: {alias_name}={alias_command}: No such file or directory")
        else:
            print("bash: alias: invalid alias definition. Usage: alias <name> = <command>")
    elif cmd.startswith("unalias "):
        alias_to_remove = cmd.split(" ", 1)[1].strip()
        try:
            del locals()[alias_to_remove]
            print(f"bash: unalias: {alias_to_remove}: No such file or directory")
        except KeyError:
            print(f"bash: unalias: {alias_to_remove}: No such file or directory")
    elif cmd == "listusers":
        try:
            users = sp.run(['net', 'user'], capture_output=True, text=True)
            print("bash: listusers: command not found")
        except FileNotFoundError:
            print("bash: listusers: command not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("userinfo "):
        username = cmd.split(" ", 1)[1].strip()
        try:
            user_info = sp.run(['net', 'user', username], capture_output=True, text=True)
            print(f"bash: userinfo: {username}: No such file or directory")
        except FileNotFoundError:
            print("bash: userinfo: command not found. This command may not work on non-Windows systems.")
    elif cmd == "listgroups":
        try:
            groups = sp.run(['net', 'localgroup'], capture_output=True, text=True)
            print("bash: listgroups: command not found")
        except FileNotFoundError:
            print("bash: listgroups: command not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("groupinfo "):
        groupname = cmd.split(" ", 1)[1].strip()
        try:
            group_info = sp.run(['net', 'localgroup', groupname], capture_output=True, text=True)
            print(f"bash: groupinfo: {groupname}: No such file or directory")
        except FileNotFoundError:
            print("bash: groupinfo: command not found. This command may not work on non-Windows systems.")
    elif cmd == "ipconfig":
        try:
            ipconfig_info = sp.run(['ipconfig'], capture_output=True, text=True)
            print("bash: ipconfig: command not found")
        except FileNotFoundError:
            print("bash: ipconfig: command not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("ping "):
        host = cmd.split(" ", 1)[1].strip()
        try:
            ping_result = sp.run(['ping', '-n', '4', host], capture_output=True, text=True)
            print(f"bash: ping: {host}: No such file or directory")
        except FileNotFoundError:
            print("bash: ping: command not found. This command may not work on non-Windows systems.")
    elif cmd.startswith("traceroute "):
        host = cmd.split(" ", 1)[1].strip()
        try:
            traceroute_result = sp.run(['tracert', host], capture_output=True, text=True)
            print(f"bash: traceroute: {host}: No such file or directory")
        except FileNotFoundError:
            print("bash: traceroute: command not found. This command may not work on non-Windows systems.")
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
        print("uptime - Display system uptime.")
        print("clear - Clear the terminal screen.")
        print("listusb - List connected USB devices.")
        print("systeminfo - Display system information.")
        print("netstat - Display network connections.")
        print("chmod <permission> <file_name> - Change file permissions.")
        print("tasklist - Display a list of running processes.")
        print("git - Run a Git command.")
        print("bf - (placeholder).")
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
    elif cmd == "sourcecode":
        with open(__file__, 'r') as source_code:
            print(source_code.read())
    elif cmd == "exit":
        print("Exiting flash shell. Goodbye!")
        break
    else:
        print(f"bash: {cmd}: command not found")