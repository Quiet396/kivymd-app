from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

KV = '''
Screen:

    BoxLayout:
        id: box
        orientation: "vertical"

        MDToolbar:
            title: "MDLabel"
        
        # add 
        MDLabel:
            text: "Custom color"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 1, 1
'''


class Test(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        # Names of standard color themes.
        for name_theme in [
            "Primary",
            "Secondary",
            "Hint",
            "Error",
            "ContrastParentBackground",
        ]:
            screen.ids.box.add_widget(
                MDLabel(
                    text=name_theme,
                    halign="center",
                    theme_text_color=name_theme,
                )
            )
        return screen


Test().run()
