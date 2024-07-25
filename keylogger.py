import keyboard

log_file = "keystrokes.txt"

def on_key_press(event):
    # with open(log_file, 'a') as f:
    #     f.write('{}\n'.format(event.name))
    print(event)

def on_key_release(event):
    print(event)

keyboard.on_release(on_key_release)
keyboard.on_press(on_key_press)

def readInput():
   keyboard.wait()