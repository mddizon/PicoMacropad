from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                 # REQUIRED dict, must be named 'app'
    'name' : 'Browser', # Application name
    'macros' : [        # List of button macros...
        # 1st row
        ('< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        ('Reload', [Keycode.CONTROL, 'r']),
        ('Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),

        # 2nd row
        ('< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        ('Hard', [Keycode.CONTROL, Keycode.SHIFT, 'r']),
        ('Tab >', [Keycode.CONTROL, Keycode.TAB]),

        # 3rd row
        ('BMarks', [Keycode.CONTROL, 'b']),
        ('New', [Keycode.CONTROL, 't']),
        ('Private', [Keycode.CONTROL, Keycode.SHIFT, 'p']),

        # 4th row
        ('Home', [Keycode.ALT, Keycode.HOME]),
        ('Top', [Keycode.HOME]),
        ('Bottom', [Keycode.END]),

        # Encoder
        # This right now is a hack, there's a bug somewhere in the
        # encoder dial where I suspect keys are not released, so
        # What happens I think is that if the sequence does not end
        # in a string, the keys don't get released and the sequence will
        # repeat indefinitely. This is a hack, but if I want to move beween
        # tabs in the browser I need to use the special \t character
        ('Prv', [Keycode.CONTROL, Keycode.SHIFT, '\t']),
        ('Nxt', [Keycode.CONTROL, '\t']),
    ],
    'layout' : [
        0x04c2eb, 0xdf0080, 0x04c2eb,
        0x05ac2f, 0xdf0080, 0x05ac2f,
        0xd26d00, 0xd26d00, 0xd26d00,
        0x660de6, 0x660de6, 0x660de6
    ]
}
