from kivy.lang.builder import Builder

from kivymd.icon_definitions import md_icons
from kivymd.uix.label import MDIcon
from kivymd.uix.tooltip import MDTooltip
from kivymd.app import MDApp

kv = '''
MDScreen:

    MDCircularLayout:
        id: container
        pos_hint: {"center_x": .95, "center_y": .5}
        row_spacing: min(self.size) * 0.1
'''

class MyIcon(MDIcon, MDTooltip):
    pass


class Main(MDApp):
    icons = list(md_icons.keys())[50:98]

    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        for iconname in self.icons:
            self.root.ids.container.add_widget(
                MyIcon(icon=iconname, tooltip_text=iconname)
            )


Main().run()
