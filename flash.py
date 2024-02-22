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
        print(f"Script not found: {script_name}")

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

def run_emulator(emulator_name):
    emulator_module = f'dep.emulators.{emulator_name}'
    try:
        # Import the run_emulator function dynamically
        emulator_module = __import__(emulator_module, fromlist=['run_emulator'])
        run_emulator = emulator_module.run_emulator
        return run_emulator()
    except ImportError:
        print(f"Error: Emulator '{emulator_name}' not found.")
        return None

while True:
    cmd = input(f"{base_dir}|flash ")

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
            print(f"Changed directory to: {base_dir}")
        except FileNotFoundError:
            print(f"Directory not found: {new_path}")
        except PermissionError:
            print(f"Permission denied to access: {new_path}")
    elif cmd == "setbase":
        new_base_dir = input("Enter the new base directory: ").strip()
        if os.path.exists(new_base_dir) and os.path.isdir(new_base_dir):
            base_dir = os.path.abspath(new_base_dir)
            print(f"Base directory set to: {base_dir}")
        else:
            print(f"Invalid directory: {new_base_dir}")
    elif cmd == "ls":
        files = os.listdir(base_dir)  # Use base_dir instead of path
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
    elif cmd.startswith("chmod "):
        try:
            permission, file_name = cmd.split(" ", 2)[1:]
            permission = int(permission, 8)  # Convert octal to decimal
            os.chmod(os.path.join(path, file_name), permission)
            print(f"Permissions for '{file_name}' changed successfully.")
        except (ValueError, FileNotFoundError) as e:
            print(f"Error: {e}")
    elif cmd == "tasklist":
        sp.run(['tasklist'])
    elif cmd == "git":
        git_command = input("Enter Git command: ")
        run_git(git_command)
    elif cmd.startswith("bf "):
        code = cmd[3:]
        result = run_emulator('bf')
        if result is not None:
            print("Output:")
            print(result)
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
            os.mkdir(os.path.join(base_dir, dir_name))  # Use base_dir instead of path
            print(f"Directory '{dir_name}' created successfully.")
        except FileExistsError:
            print(f"Directory '{dir_name}' already exists.")
    elif cmd.startswith("rmdir "):
        dir_name = cmd.split(" ", 1)[1].strip()
        try:
            os.rmdir(os.path.join(base_dir, dir_name))  # Use base_dir instead of path
            print(f"Directory '{dir_name}' removed successfully.")
        except FileNotFoundError:
            print(f"Directory '{dir_name}' not found.")
    elif cmd.startswith("rm ") or cmd.startswith("remove "):
        file_name = cmd.split(" ", 1)[1].strip()
        try:
            os.remove(os.path.join(base_dir, file_name))  # Use base_dir instead of path
            print(f"File '{file_name}' removed successfully.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
    elif cmd.startswith("copy "):
        file_source, file_destination = map(str.strip, cmd.split(" ", 2)[1:])
        try:
            shutil.copyfile(os.path.join(base_dir, file_source), os.path.join(base_dir, file_destination))  # Use base_dir instead of path
            print(f"File '{file_source}' copied to '{file_destination}' successfully.")
        except FileNotFoundError:
            print(f"File '{file_source}' not found.")
        except PermissionError:
            print(f"Permission denied to copy '{file_source}'.")
    elif cmd.startswith("rename "):
        old_name, new_name = map(str.strip, cmd.split(" ", 2)[1:])
        try:
            os.rename(os.path.join(base_dir, old_name), os.path.join(base_dir, new_name))  # Use base_dir instead of path
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
        disk_usage = psutil.disk_usage(base_dir)  # Use base_dir instead of path
        print("Disk Usage Information:")
        print(f"    Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
        print(f"    Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
        print(f"    Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
        print(f"    Disk Usage Percentage: {disk_usage.percent}%")
    elif cmd.startswith("open "):
        file_to_open = cmd.split(" ", 1)[1].strip()
        try:
            sp.run(['open', file_to_open])  # Adjust 'open' based on the operating system
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
        print("version, get, cd/changedir, ls, turtle, time, date, whoami, !info, info, cal, echo, uptime, clear, listusb, systeminfo, netstat, tasklist, shutdown, restart, cpuinfo, mkdir, rmdir, rm/remove, copy, rename, listprocesses, kill, diskusage, open, listenv, setenv, unsetenv, listaliases, alias, unalias, listusers, userinfo, listgroups, groupinfo, ipconfig, ping, traceroute, help, exit, sourcecode")
    elif cmd == "sourcecode":
        with open(__file__, 'r') as source_code:
            print(source_code.read())
    elif cmd == "exit":
        print("Exiting flash shell. Goodbye!")
        break