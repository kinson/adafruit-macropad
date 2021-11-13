from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Mac Firefox', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'wms', [Keycode.COMMAND, 'l', -Keycode.COMMAND, 'github.com/stordco/wms-service\n']),
        (0x004000, 'wms-ui', [Keycode.COMMAND, 'l', -Keycode.COMMAND, 'github.com/stordco/wms-ui\n']),
        (0x400000, 'Master', [Keycode.COMMAND, 'l', -Keycode.COMMAND, 'github.com/notifications\n']),      # Scroll up
        # 2nd row ----------
        (0x202000, 'prs', [Keycode.COMMAND, 'l', -Keycode.COMMAND, 'github.com/stordco/wms-service/pulls\n']),
        (0x202000, 'prs', [Keycode.COMMAND, 'l', -Keycode.COMMAND, 'github.com/stordco/wms-ui/pulls\n']),
        (0x400000, 'all', [Keycode.COMMAND, 'l', -Keycode.COMMAND, 'https://github.com/pulls?q=is%3Aopen+is%3Apr+archived%3Afalse+repo%3Astordco%2Fwms-ui+repo%3Astordco%2Fwms-service\n']),
        # 3rd row ----------
        (0x000040, 'dcu', [Keycode.COMMAND, 'c', -Keycode.COMMAND, 'dcr\n']),
        (0x000040, 'dcd', [Keycode.COMMAND, 'c', -Keycode.COMMAND, 'dcd\n']),
        (0x000040, 'dcr', [Keycode.COMMAND, 'c', -Keycode.COMMAND, 'dcr\n']),
        # 4th row ----------
        (0x000000, 'api-up', [Keycode.COMMAND, 'c', -Keycode.COMMAND, 'mix setup && mix phx.server\n']),   # Adafruit in new window
        (0x800000, 'ui-up', [Keycode.COMMAND, 'c', -Keycode.COMMAND, 'yarn start\n']),
        (0x101010, 'test', [Keycode.COMMAND, 'c', -Keycode.COMMAND, 'yarn test a\n']),
        # Encoder button ---
        (0x000000, 'gst', [Keycode.COMMAND, 'c', -Keycode.COMMAND, 'gst\n'])
    ]
}