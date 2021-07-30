# Adabox 019 - Macropad
Project adapted from https://learn.adafruit.com/macropad-hotkeys
Macropad firmware and software for the RP2040 macropad kit included in Adabox 019

## Changes from original
Rotated device so screen and encoder placed at the bottom
Uses encoder button to change between different hotkey layers
Allows for encoder turns to be programmed as hotkeys in both clockwise and counter clockwise directions

## Installing
Set up Circuit Python for RP2040 - https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython
Copy contents from src directory into CIRCUITPY root directory

## Creating hotkeys
- Add Hotkeys in this form:
    ('DisplayName', [Keycode.GUI, Keycode.ENTER])
- Keycode Documentation: https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode
- Layouts can be named anything as long as they are listed in the macros/ directory
- Layouts must list an app dict in its own file
- First three hotkeys correspond to the first row, the next three correspond to the next row and so on
- The 13th and 14th hotkeys correspond to the counter clockwise turn of the encoder and the clockwise turn of the encoder, respectively

## Notes
- When using a key to launch dmenu, for some reason the first text key gets consumed, as a quick havk you can add dummy keypresses to be consumed
- When assigning macros to the encoder turns, somehow the keys won't be released or is somehow repeated, not 100% sure if it's the current code or the firmware, so I reccomend ending the encoder turn macros with a text, so that it uses the macropad.write function

