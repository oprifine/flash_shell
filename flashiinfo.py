import platform

def display_system_info():
    system_info = platform.uname()

    print("System Information:")
    print(f"System: {system_info.system}")
    print(f"Node: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

def main():
    print("Computer Information Script")
    display_system_info()

if __name__ == "__main__":
    main()
