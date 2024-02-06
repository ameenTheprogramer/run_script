import subprocess
import time

def open_new_terminal():
    # Simulate the key combination Shift+Ctrl+N using xdotool
    subprocess.run(['xdotool', 'keydown', 'shift', 'keydown', 'ctrl', 'key', 'n'])
    time.sleep(0.1)  # Add a small delay to ensure the keys are registered
    subprocess.run(['xdotool', 'keyup', 'shift', 'keyup', 'ctrl'])

if __name__ == "__main__":
    open_new_terminal()
    subprocess.run(['python3', 'arrow_key_press.py'])
    open_new_terminal()
    subprocess.run(['firefox', 'clickasnap.com/iamthecoolguy'])
    
