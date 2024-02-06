#!/usr/bin/env python3
import subprocess

def install_dependencies():
    # Install necessary packages
    subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'])
    subprocess.run(['pip3', 'install', '--upgrade', 'pip'])
    subprocess.run(['pip3', 'install', 'pynput'])
    subprocess.run(['pip3', 'install', 'pyautogui'])
    subprocess.run(['sudo', 'apt-get', 'install', 'xdotool'])
    subprocess.run(['sudo', 'apt-get', 'install', 'xterm'])

def download_scripts():
    # Download the arrow_key_press.py script
    subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/right_arrow/main/arrow_key_press.py'])
    subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/run_script/main/script2.py'])
    subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/run_script/main/shortcut.py'])
    

def main():
  
    subprocess.run(['sudo', 'apt', 'update'])
    install_dependencies()
    subprocess.run(['xterm', '-fg', '#00FF00'])
    download_scripts()

    # Run script2.py
    subprocess.run(['python3', 'script2.py'])

if __name__ == "__main__":
    main()
