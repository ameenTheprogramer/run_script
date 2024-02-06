import subprocess

def run_command(command):
    subprocess.run(command, shell=True, check=True)

def main():
    # Get the value of $DISPLAY
    display = subprocess.run("echo $DISPLAY", shell=True, capture_output=True, text=True)
    display_value = display.stdout.strip()

    # Create .Xauthority file and set permissions
    run_command("touch ~/.Xauthority")
    run_command("chmod 600 ~/.Xauthority")

    # Export DISPLAY=:0
    run_command(f"export DISPLAY={display_value}")

if __name__ == "__main__":
    main()
    
    subprocess.run(['exit'])
