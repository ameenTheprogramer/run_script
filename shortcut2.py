import time
import subprocess

def open_new_terminal(command):
    # Open a new terminal window and run the command
    subprocess.Popen(['xterm', '-e', command])

if __name__ == "__main__":
    # Open a new terminal and run 'python3 arrow_key_press.py'
    open_new_terminal('python3 arrow_key_press.py')

    # Open another new terminal and run 'firefox clickasnap.com/iamthecoolguy'
    open_new_terminal('firefox clickasnap.com/iamthecoolguy')

    time.sleep(10)
    open_new_terminal('python click.py')
    time.sleep(10)
    open_new_terminal('python scroll.py')
    time.sleep(10)
    open_new_terminal('python click2.py')
    time.sleep(10)
    open_new_terminal('python scroll2.py')
