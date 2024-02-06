# #!/usr/bin/env python3
# import subprocess

# def install_dependencies():
#     # Install necessary packages
#     subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'])
#     subprocess.run(['pip3', 'install', '--upgrade', 'pip'])
#     subprocess.run(['pip3', 'install', 'pynput'])
#     subprocess.run(['pip3', 'install', 'pyautogui'])
#     subprocess.run(['sudo', 'apt-get', 'install', 'xdotool'])

# def download_scripts():
#     # Download the arrow_key_press.py script
#     subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/right_arrow/main/arrow_key_press.py'])
#     subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/run_script/main/script2.py'])
#     subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/run_script/main/shortcut2.py'])
    

# def main():
#     color = 'echo -e "\033]10;#00FF00\007"'
#     subprocess.run(['sudo', 'apt', 'update'])
#     subprocess.run(['sudo', 'apt-get', 'install', 'xterm'])
#     subprocess.run(color, shell=True)
#     install_dependencies()
#     download_scripts()












#!/usr/bin/env python3
import subprocess

def run_with_confirmation(command):
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    process.communicate(b'y\n')

def install_dependencies():
    # Install necessary packages
    run_with_confirmation(['sudo', 'apt', 'install', '-y', 'python3-pip'])
    subprocess.run(['pip3', 'install', '--upgrade', 'pip'])
    subprocess.run(['pip3', 'install', 'pynput'])
    subprocess.run(['pip3', 'install', 'pyautogui'])
    run_with_confirmation(['sudo', 'apt-get', 'install', 'xdotool'])

def download_scripts():
    # Download the arrow_key_press.py script
    subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/right_arrow/main/arrow_key_press.py'])
    subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/run_script/main/script2.py'])
    subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/run_script/main/shortcut2.py'])

def main():
    color = 'echo -e "\033]10;#00FF00\007"'
    subprocess.run(['sudo', 'apt', 'update'])
    run_with_confirmation(['sudo', 'apt-get', 'install', 'xterm'])
    subprocess.run(color, shell=True)
    install_dependencies()
    download_scripts()

    # Run script2.py
    subprocess.run(['python3', 'script2.py'])

if __name__ == "__main__":
    main()

#     # Run script2.py
#     subprocess.run(['python3', 'script2.py'])

# if __name__ == "__main__":
#     main()






