#!/usr/bin/env python3
import os
import subprocess

# Install necessary packages
subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'])
subprocess.run(['pip3', 'install', '--upgrade', 'pip'])
subprocess.run(['pip3', 'install', 'pynput'])
subprocess.run(['pip3', 'install', 'pyautogui'])

# Download the arrow_key_press.py script
subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/right_arrow/main/arrow_key_press.py'])


