# deej controller for MacroPad

from utils.app_pad import AppPad
from utils.apps.key import KeyApp, Key, KeyAppSettings
from utils.apps.base import BaseApp
from utils.commands import (
    Command,
    Keycode,
    MacroCommand,
    Press,
    PreviousAppCommand,
    Release,
    Sequence,
    Text,
    Wait,
)
from utils.constants import (
    COLOR_3,
    COLOR_7,
    COLOR_9,
    COLOR_BACK,
    COLOR_CHROME,
    COLOR_CLOSE,
    OS_MAC,
)

class Deej():
    def __init__(self):
        self.values = [0, 0, 0]
        self.current_index = 0

    def encoder_increase(self):
        self.values[self.current_index] += 1

    def encoder_decrease(self):
        self.values[self.current_index] -= 1

    def encoder_press(self):
        print(self.values)
        print(self.current_index)


class DeejCommandBase(Command):
    def __init__(self, deej_instance: Deej):
        self.deej_instance = deej_instance
        super().__init__()

class EncoderIncrease(DeejCommandBase):
    def execute(self, _app):
        self.deej_instance.encoder_increase()

class EncoderDecrease(DeejCommandBase):
    def execute(self, _app):
        self.deej_instance.encoder_decrease()

class EncoderButton(DeejCommandBase):
    def execute(self, _app):
        self.deej_instance.encoder_press()

class DeejSelectChannel(DeejCommandBase):
    def __init__(self, deej_instance: Deej, channel: int):
        self.channel = channel
        super().__init__(deej_instance)

    def execute(self, _app):
        self.deej_instance.current_index = self.channel
        print(self.deej_instance.current_index)



class DeejApp(KeyApp):
    NUM_VALUES = 3
    name = "Deej"

    deej_instance = Deej()

    key_0 = Key("0", command=DeejSelectChannel(deej_instance, 0))
    key_1 = Key("1", command=DeejSelectChannel(deej_instance, 1))
    key_2 = Key(
        "F3", COLOR_3, Press(Keycode.F3), double_tap_command=PreviousAppCommand()
    )

    encoder_button = EncoderButton(deej_instance)
    encoder_decrease = EncoderDecrease(deej_instance)
    encoder_increase = EncoderIncrease(deej_instance)