from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDIcon
from kivymd.icon_definitions import md_icons


KV = '''
Screen:

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDIcon"

        ScrollView:

            MDList:
                id: box
                padding: dp(20)
                spacing: dp(30)
'''


class Test(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        # Names of standard font styles.
        for name_icon in md_icons.keys():
            screen.ids.box.add_widget(
                MDIcon(
                    halign="center",
                    icon=name_icon,
                )
            )
        return screen


Test().run()
