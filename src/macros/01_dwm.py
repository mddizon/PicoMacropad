from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {             # REQUIRED dict, must be named 'app'
    'name' : 'DWM', # Application name
    'macros' : [    # List of button macros...
        # 1st row
        ('< Move', [Keycode.GUI, Keycode.SHIFT, '.']),
        ('Up', [Keycode.GUI, 'k']),
        ('Move >', [Keycode.GUI, Keycode.SHIFT, '.']),

        # 2nd row
        ('Left', [Keycode.GUI, ',']),
        ('Focus', [Keycode.GUI, Keycode.ENTER]),
        ('Right', [Keycode.GUI, '.']),

        # 3rd row
        ('Switch', [Keycode.GUI, Keycode.TAB]),
        ('Down', [Keycode.GUI, 'j']),
        ('Close', [Keycode.GUI, Keycode.SHIFT, 'q']),

        # 4th row
        # Not 100% sure why but after launching dmenu the first character
        # is not entered, so as a hacky work around i added a space
        # before the application I want to open
        ('Files', [Keycode.GUI, 'p', -Keycode.GUI, ' thunar\n']),
        ('Term', [Keycode.GUI, Keycode.SHIFT, Keycode.ENTER]),
        ('Screen', [Keycode.GUI, 'p', -Keycode.GUI, ' shot\n']),

        # Encoder
        ('Contract', [Keycode.GUI, 'h']),
        ('Expand', [Keycode.GUI, 'l'])
    ],
    'layout' : [
        0x04c2eb, 0xdf0080, 0x04c2eb,
        0xdf0080, 0x05ac2f, 0xdf0080,
        0xd26d00, 0xdf0080, 0xd26d00,
        0x660de6, 0x660de6, 0x660de6
    ]
}
