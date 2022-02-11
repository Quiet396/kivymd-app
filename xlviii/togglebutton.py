from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton

KV = '''
Screen:

    MDBoxLayout:
        adaptive_size: True
        pos_hint: {"center_x": .5, "center_y": .5}

        MyToggleRectangleButton:
            text: "Show ads"
            group: "x"

        MyToggleRectangleButton:
            text: "Do not show ads"
            group: "x"

        MyToggleRectangleButton:
            text: "Does not matter"
            group: "x"

        MyToggleRoundButton:
            text: "Show ads"
            group: "y"

        MyToggleRoundButton:
            text: "Do not show ads"
            group: "y"

        MyToggleRoundButton:
            text: "Does not matter"
            group: "y"
'''


class MyToggleRectangleButton(MDRectangleFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light


class MyToggleRoundButton(MDFillRoundFlatButton, MDToggleButton):
    def __init__(self, **kwargs):
        self.background_down = MDApp.get_running_app().theme_cls.primary_dark
        super().__init__(**kwargs)

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
