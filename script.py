#!/usr/bin/env python3
import os
import subprocess

# Install necessary packages
subprocess.run(['apt', 'update'])
subprocess.run(['apt', 'install', 'python3-pip'])
subprocess.run(['pip', 'install', 'pynput'])
subprocess.run(['pip', 'install', 'pyautogui'])

# Download the arrow_key_press.py script
subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/right_arrow/main/arrow_key_press.py'])


