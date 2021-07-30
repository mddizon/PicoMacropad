"""
A fairly straightforward macro/hotkey program for Adafruit MACROPAD.
Macro key setups are stored in the /macros folder (configurable below),
load up just the ones you're likely to use. Plug into computer's USB port,
use dial to select an application macro set, press MACROPAD keys to send
key sequences.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad

# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'

# CLASSES AND FUNCTIONS ----------------

class App:
    """ Class representing a host-side application, for which we have a set
        of macro sequences. Project code was originally more complex and
        this was helpful, but maybe it's excessive now?"""
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']
        self.layout = appdata['layout']

    def switch(self):
        """ Activate application settings; update OLED labels and LED
            colors. """
        GROUP[13].text = self.name   # Application name
        for i in range(12):
            if i < len(self.layout): # Key in use, set label + LED color
                MACROPAD.pixels[i] = self.layout[i]
                GROUP[i].text = self.macros[i][0]
            else:  # Key not in use, no label or LED
                MACROPAD.pixels[i] = 0
                GROUP[i].text = ''
        MACROPAD.pixels.show()
        MACROPAD.display.refresh()

# INITIALIZATION -----------------------

MACROPAD = MacroPad(rotation=180)
MACROPAD.display.auto_refresh = False
MACROPAD.pixels.auto_write = False

# Set up displayio group with all the labels
GROUP = displayio.Group(max_size=14) # 12 keys + rect + app name
for KEY_INDEX in range(12):
    x = KEY_INDEX % 3
    y = KEY_INDEX // 3
    GROUP.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                             anchored_position=((MACROPAD.display.width - 1) * x / 2,
                                                MACROPAD.display.height - 1 -
                                                (3 - y) * 12),
                             anchor_point=(x / 2, 1.0), max_glyphs=15))
GROUP.append(Rect(0, 0, MACROPAD.display.width, 12, fill=0xFFFFFF))
GROUP.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(MACROPAD.display.width//2, -2),
                         anchor_point=(0.5, 0.0), max_glyphs=30))
MACROPAD.display.show(GROUP)

# Load all the macro key setups from .py files in MACRO_FOLDER
APPS = []
FILES = os.listdir(MACRO_FOLDER)
FILES.sort()
for FILENAME in FILES:
    if FILENAME.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + FILENAME[:-3])
            APPS.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            pass

if not APPS:
    GROUP[13].text = 'NO MACRO FILES FOUND'
    MACROPAD.display.refresh()
    while True:
        pass

LAST_POSITION = MACROPAD.encoder
APP_INDEX = 0
APPS[APP_INDEX].switch()

# MAIN LOOP ----------------------------

while True:
    POSITION = MACROPAD.encoder

    if MACROPAD.encoder_switch:
        APP_INDEX = (APP_INDEX + 1) % len(APPS)
        APPS[APP_INDEX].switch()
        continue

    EVENT = MACROPAD.keys.events.get()
    if EVENT and EVENT.key_number < len(APPS[APP_INDEX].macros):
        KEY_NUMBER = EVENT.key_number
        PRESSED = EVENT.pressed
    elif POSITION != LAST_POSITION:
        KEY_NUMBER = 13 if POSITION > LAST_POSITION else 12
        PRESSED = True
        LAST_POSITION = POSITION
        #GROUP[13].text = "KEY_NUMBER: %d" % KEY_NUMBER
        #MACROPAD.display.refresh()
    else:
        PRESSED = False
        continue

    SEQUENCE = APPS[APP_INDEX].macros[KEY_NUMBER][1]
    if PRESSED:
        if KEY_NUMBER < 12: # No pixel for encoder button
            MACROPAD.pixels[KEY_NUMBER] = 0xd1e30a
            MACROPAD.pixels.show()
        for item in SEQUENCE:
            if isinstance(item, int):
                if item >= 0:
                    MACROPAD.keyboard.press(item)
                else:
                    MACROPAD.keyboard.release(item)
            else:
                MACROPAD.keyboard_layout.write(item)
    else:
        # Release any still-pressed modifier keys
        for item in SEQUENCE:
            if isinstance(item, int) and item >= 0:
                MACROPAD.keyboard.release(item)
        if KEY_NUMBER < 12: # No pixel for encoder button
            MACROPAD.pixels[KEY_NUMBER] = APPS[APP_INDEX].layout[KEY_NUMBER]
            MACROPAD.pixels.show()
