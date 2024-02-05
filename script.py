#!/usr/bin/env python3

import subprocess

# Install necessary packages
subprocess.run(['apt', 'update'])
subprocess.run(['apt', 'install', 'python3-pip'])
subprocess.run(['pip', 'install', 'pynput'])
subprocess.run(['pip', 'install', 'pyautogui'])

# Download the arrow_key_press.py script
subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/right_arrow/main/arrow_key_press.py'])

# Print the value of DISPLAY
display_value = subprocess.run(['echo', '$DISPLAY'], capture_output=True, text=True).stdout.strip()
print(f"DISPLAY value: {display_value}")




# Create and set permissions for .Xauthority file
subprocess.run(['touch', '~/.Xauthority'])
subprocess.run(['chmod', '600', '~/.Xauthority'])

# Export DISPLAY=:0
subprocess.run(['export', 'DISPLAY=:0'])

# Exit the current terminal session
subprocess.run(['exit'])

