from kivy.factory import Factory
from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex


<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"


MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDNavigationRail"
        md_bg_color: rail.md_bg_color
        left_action_items: [["menu", lambda x: app.rail_open()]]

    MDBoxLayout:

        MDNavigationRail:
            id: rail
            # item text selected
            visible: "Selected"
            # menu( item) color
            md_bg_color: get_color_from_hex("#407294")
            color_normal: get_color_from_hex("#e6e6fa")
            color_active: get_color_from_hex("#e2d0ca")
            # hover
            use_hover_behavior: True
            hover_bg: 1, 1, 1, .2
            # rail open/close
            use_resizeable: True
            # title
            use_title: True
            icon_title: "./genba_neko.png"
            text_title: "[b][color=#ffffff]Example[/color][/b]"
            # action button
            use_action_button: True
            action_text_button: "COMPOSE"
            on_action_button: print(args)

            MDNavigationRailItem:
                icon: "language-cpp"
                text: "C++"

            MDNavigationRailItem:
                icon: "language-java"
                text: "Java"

            MDNavigationRailItem:
                icon: "language-swift"
                text: "Swift"

        MDBoxLayout:
            padding: "24dp"

            ScrollView:

                MDList:
                    id: box
                    cols: 3
                    spacing: "12dp"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def rail_open(self):
        if self.root.ids.rail.rail_state == "open":
            self.root.ids.rail.rail_state = "close"
        else:
            self.root.ids.rail.rail_state = "open"

    def on_start(self):
        for i in range(9):
            tile = Factory.MyTile(source="./saya.jpg")
            tile.stars = 5
            self.root.ids.box.add_widget(tile)


Test().run()

