from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {             # REQUIRED dict, must be named 'app'
    'name' : 'Vim', # Application name
    'macros' : [    # List of button macros...
        # 1st row
        ('Wiki', [' wt']),
        ('EDot', [' ev']),
        ('SDot', [' sv']),

        # 2nd row
        ('Tree', [':NERDTree', Keycode.ENTER]),
        ('Down', [Keycode.CONTROL, 'd']),
        ('Up', [Keycode.CONTROL, 'u']),

        # 3rd row
        ('Top', ['gg']),
        ('Diary', [' w w']),
        ('Git', [':Git\n']),

        # 4th row
        ('Bottom', ['G']),
        ('Journal', [' w i']),
        ('Commit', [':Git commit\n']),

        # Encoder
        ('Undo', ['u']),
        ('Redo', [Keycode.CONTROL, 'r'])
    ],
    'layout' : [
        0x05ac2f, 0x05ac2f, 0x05ac2f,
        0xd26d00, 0xdf0080, 0x04c2eb,
        0xd26d00, 0xdf0080, 0x04c2eb,
        0x660de6, 0x660de6, 0x660de6
    ]
}
