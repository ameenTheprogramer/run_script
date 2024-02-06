import subprocess
import time

def open_new_terminal(command):
    # Open a new terminal window and run the command
    subprocess.run(['xterm', '-e', command])

if __name__ == "__main__":
    # Open a new terminal and run 'python3 arrow_key_press.py'
    open_new_terminal('python3 arrow_key_press.py')

    # Open another new terminal and run 'firefox clickasnap.com/iamthecoolguy'
    open_new_terminal('firefox clickasnap.com/iamthecoolguy')
