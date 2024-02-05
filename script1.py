#!/usr/bin/env python3

import subprocess
import os

# Install necessary packages
subprocess.run(['sudo', 'apt', 'update'])
subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'])
subprocess.run(['pip3', 'install', '--upgrade', 'pip'])
subprocess.run(['pip3', 'install', 'pynput'])
subprocess.run(['pip3', 'install', 'pyautogui'])

# Download the arrow_key_press.py script
subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/right_arrow/main/arrow_key_press.py'])

# Print the value of DISPLAY
display_value = subprocess.run(['echo', '$DISPLAY'], capture_output=True, text=True).stdout.strip()
print(f"DISPLAY value: {display_value}")

# Set the DISPLAY environment variable
os.environ['DISPLAY'] = display_value

# Create and set permissions for .Xauthority file
subprocess.run(['touch', os.path.expanduser('~/.Xauthority')])
subprocess.run(['chmod', '600', os.path.expanduser('~/.Xauthority')])

# Run the arrow_key_press.py script
subprocess.run(['python3', 'arrow_key_press.py'])
