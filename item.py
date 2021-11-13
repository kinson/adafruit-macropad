from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'iTerm', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Pull', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'git pull\n']),
        (0x004000, 'Push', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'git push\n']),
        (0x400000, 'Master', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'git checkout master\n']),      # Scroll up
        # 2nd row ----------
        (0x202000, 'wms-api', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'cd ~/Documents/wms/warehouse\n']),
        (0x202000, 'wms-ui', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'cd ~/Documents/wms/warehouse-ui\n']),
        (0x400000, '~/', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'cd ~/\n']),
        # 3rd row ----------
        (0x000040, 'dcu', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'dcu\n']),
        (0x000040, 'dcd', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'dcd\n']),
        (0x000040, 'dcr', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'dcr\n']),
        # 4th row ----------
        (0x000000, 'api-up', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'mix setup && mix phx.server\n']),   # Adafruit in new window
        (0x800000, 'ui-up', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'yarn start\n']),
        (0x101010, 'test', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'yarn test a\n']),
        # Encoder button ---
        (0x000000, 'gst', [Keycode.CONTROL, 'c', -Keycode.CONTROL, 'gst\n'])
    ]
}