class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
try:
    import platform
    import ctypes, os
    from time import sleep
    import requests
except ImportError:
    print(Color.RED + "Import error, dependencies not installed trying to auto install" + Color.END)
    try:
        os.system("pip install -r requirements.txt")
    except:
        print(Color.RED + "Cannot install manual install required" + Color.END)

try:

    version = "1.0"

    print(
'''
  _____  _   _  _____    _____                    __          
 |  __ \| \ | |/ ____|  / ____|                  / _|         
 | |  | |  \| | (___   | (___  _ __   ___   ___ | |_ ___ _ __ 
 | |  | | . ` |\___ \   \___ \| '_ \ / _ \ / _ \|  _/ _ \ '__|
 | |__| | |\  |____) |  ____) | |_) | (_) | (_) | ||  __/ |   
 |_____/|_| \_|_____/  |_____/| .__/ \___/ \___/|_| \___|_|   
                              | |                             
                              |_|                             
 By kokofixcomputers
    ''')

    print("Welcome! Spoofer V" + version)
    print(Color.GREEN + "Checking for latest version" + Color.END)

    latest_version_url = "https://raw.githubusercontent.com/kokofixcomputers/spoofer/main/VERSION"
    request = requests.get(latest_version_url)

    if request.status_code == 200:
        latest_version = request.text.strip()
        if latest_version == version:
            print(Color.GREEN + "You have the latest version! Continue..." + Color.END)
        else:
            print(Color.YELLOW + f"New Version available! New version: {latest_version}" + Color.END)
    else:
        print(Color.RED + "Failed to check for the latest version. Please try again later." + Color.END)

    print(Color.GREEN + 'Checking for admin permissions.' + Color.END)

    def is_admin():
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    admin = is_admin()
    if admin:
        print(Color.GREEN + 'Admin Permissions Granted! Continue' + Color.END)
    else:
        print(Color.RED + 'Admin Permissions Not Granted. Please note that this requires admin permissions to run. Error: insufficient privileges. Exiting...' + Color.END)
        exit(1)
except KeyboardInterrupt:
    print(Color.RED + "Keyboard Interrupt Closing..." + Color.END)

def modify_host_file():
    try:
        action = input("Enter the action (Add Spoof or Delete Spoof): ")
    except KeyboardInterrupt:
        print(Color.RED + '''
Keyboard Interrupt Closing...''' + Color.END)
        exit(0)

    if action.lower() == 'add spoof':
     try:
        spoofing_domain = input("Enter the Spoofing Domain: ")
        spoofing_ip = input("Enter the Spoofing IP: ")

        current_platform = platform.system()

        if current_platform == 'Windows':
            print(Color.GREEN + 'Windows Detected. Setting host file location...' + Color.END)
            host_file_path = r'C:\Windows\System32\drivers\etc\hosts'
        else:
            print(Color.GREEN + 'Linux-Based Detected. Setting host file location...' + Color.END)
            host_file_path = '/etc/hosts'

        try:
             with open(host_file_path, 'a') as host_file:
                host_file.write('\n' + spoofing_ip + ' ' + spoofing_domain + " #added by spoofer made by kokofixcomputers")
                print(Color.GREEN + "Host file has been modified successfully!" + Color.END)
        except PermissionError:
                print(Color.RED + "Permission denied. Please run the script with administrative privileges." + Color.END)
        except KeyboardInterrupt:
            print(Color.RED + '''
Keyboard Interrupt, Closing...''' + Color.END)
            sleep(1)
            print(Color.GREEN + "Gracefull Shutdown Completed" + Color.END)
        except Exception as e:
                print(Color.RED + f"An error occurred: {e}" + Color.END)
     except:
         print(Color.RED + '''
Keyboard Interrupt Closing...''' + Color.END)

    elif action.lower() == 'delete spoof':
        print(Color.GREEN + "Delete Spoof..." + Color.END)
        current_platform = platform.system()
        if current_platform == 'Windows':
            print(Color.GREEN + 'Windows Detected. Setting host file location...' + Color.END)
            host_file_path = r'C:\Windows\System32\drivers\etc\hosts'
        else:
            print(Color.GREEN + 'Linux-Based Detected. Setting host file location...' + Color.END)
            host_file_path = '/etc/hosts'
        try:
            with open(host_file_path, 'r') as host_file:
                lines = host_file.readlines()
                filtered_lines = [line for line in lines if line.strip() and not line.startswith('#')]
                for i, line in enumerate(filtered_lines):
                    print(f"{i + 1}. {line.strip()}")

            line_number = int(input("Enter the line number to delete: "))
        
            # Remove the selected line from the list of filtered lines
            del filtered_lines[line_number - 1]

            # Write the modified lines back to the host file
            with open(host_file_path, 'w') as host_file:
                for line in filtered_lines:
                    host_file.write(line + '\n')

            print(Color.GREEN + "Spoof has been deleted successfully!" + Color.END)
        except PermissionError:
            print(Color.RED + "Permission denied. Please run the script with administrative privileges." + Color.END)
        except KeyboardInterrupt:
            print(Color.RED + '''
Keyboard Interrupt, Closing...''' + Color.END)
            sleep(1)
            print(Color.GREEN + "Gracefull Shutdown Completed" + Color.END)

        except Exception as e:
            print(Color.RED + f"An error occurred: {e}" + Color.END)
    else:
        print(Color.RED + "Invalid action. Please enter 'Add Spoof' or 'Delete Spoof'." + Color.END)

# Call the function to modify the host file
modify_host_file()