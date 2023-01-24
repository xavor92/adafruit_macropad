""" MACROPAD Hotkeys example: CS Buyscript

// Key bindings (Aliases are used here)
bind "kp_home" " buy vesthelm; buy vest;"
bind "kp_uparrow" " buy defuser;"
bind "kp_pgup" "autobuy;"
bind "kp_leftarrow" "buy mag7;"
bind "kp_5" "buy ak47; buy m4a1;"
bind "kp_rightarrow" "buy aug; buy sg556;"
bind "kp_end" " buy hegrenade;"
bind "kp_downarrow" " buy flashbang;"
bind "kp_pgdn" " buy smokegrenade;"
bind "kp_del" " buy incgrenade; buy molotov;"
bind "kp_ins" "buy deagle; buy revolver;"
bind "kp_enter" " buy taser;"

// Debug
echo
echo +++ autoexec.cfg executed successfully +++
echo

"""
from utils.apps.key import Key, KeyApp
from utils.commands import (
    Keycode,
    Press,
    PreviousAppCommand,
)

COLOR_RED = 0xFF0000
COLOR_GREEN = 0x00FF00
COLOR_BLUE = 0x0000FF

class CSApp(KeyApp):
    name = "Numpad"

    # First row
    key_0 = Key("Vest", COLOR_GREEN, Press(Keycode.KEYPAD_SEVEN), double_tap_command=Press(Keycode.KEYPAD_NUMLOCK))
    key_1 = Key("Def", COLOR_GREEN, Press(Keycode.KEYPAD_EIGHT))
    key_2 = Key("Autobuy", 0xFFFFFF, Press(Keycode.KEYPAD_NINE), double_tap_command=PreviousAppCommand())

    # Second row
    key_3 = Key("Swag7", COLOR_RED, Press(Keycode.KEYPAD_FOUR))
    key_4 = Key("M4", COLOR_RED, Press(Keycode.KEYPAD_FIVE))
    key_5 = Key("Aug", COLOR_RED, Press(Keycode.KEYPAD_SIX))

    # Third row
    key_6 = Key("HE", COLOR_BLUE, Press(Keycode.KEYPAD_ONE))
    key_7 = Key("Flash", COLOR_BLUE, Press(Keycode.KEYPAD_TWO))
    key_8 = Key("Smoke", COLOR_BLUE, Press(Keycode.KEYPAD_THREE))

    # Fourth row
    key_9 = Key("Fire", COLOR_BLUE, Press(Keycode.KEYPAD_PERIOD))
    key_10 = Key("Deagle", COLOR_RED, Press(Keycode.KEYPAD_ZERO))
    key_11 = Key("Taser", COLOR_RED, Press(Keycode.KEYPAD_ENTER))
