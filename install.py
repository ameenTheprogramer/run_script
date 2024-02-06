import subprocess

def run_with_confirmation(command):
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    process.communicate(b'y\n')

if __name__ == "__main__":
    commands = [
        ['sudo', 'apt', 'install', '-y', 'python3-pip'],
        ['pip3', 'install', '--upgrade', 'pip'],
        ['pip3', 'install', 'pynput'],
        ['pip3', 'install', 'pyautogui'],
        ['sudo', 'apt-get', 'install', 'xdotool'],
        ['sudo', 'apt-get', 'install', 'xterm']
    ]

    for cmd in commands:
        run_with_confirmation(cmd)
