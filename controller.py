import pyvjoy
from pynput import keyboard
import time

j = pyvjoy.VJoyDevice(1)

# Valeurs centrales
x = 16384  # axe X = direction
y = 0      # axe Y = accélérateur (de 0 à 32768)

# Vitesses
step_normal = 500
step_fast = 3000
min_val = 0
max_val = 32768

keys_pressed = set()

def on_press(key):
    try:
        keys_pressed.add(key.char)
    except AttributeError:
        keys_pressed.add(key)

def on_release(key):
    try:
        keys_pressed.discard(key.char)
    except AttributeError:
        keys_pressed.discard(key)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

try:
    while True:
        step = step_fast if keyboard.Key.shift in keys_pressed or keyboard.Key.shift_r in keys_pressed else step_normal

        # Axe X (direction)
        if keyboard.Key.left in keys_pressed:
            x = max(min_val, x - step)
        elif keyboard.Key.right in keys_pressed:
            x = min(max_val, x + step)
        else:
            if x < 16384:
                x = min(16384, x + step)
            elif x > 16384:
                x = max(16384, x - step)

        # Axe Y (accélérateur)
        if keyboard.Key.up in keys_pressed:
            y = min(max_val, y + step)
        elif keyboard.Key.down in keys_pressed:
            y = max(min_val, y - step)
        else:
            # ralenti progressif
            if y > 0:
                y = max(0, y - step)

        # Appliquer les valeurs
        j.set_axis(pyvjoy.HID_USAGE_X, int(x))
        j.set_axis(pyvjoy.HID_USAGE_Y, int(y))

        time.sleep(1/60)
except KeyboardInterrupt:
    listener.stop()
