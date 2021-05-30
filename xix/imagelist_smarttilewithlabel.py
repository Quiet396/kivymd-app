from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    height: "240dp"


ScrollView:

    MDGridLayout:
        cols: 1
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)

        MyTile:
            source: "./sample1.jpg"
            text: "[size=26]Keikan 1[/size]\\n[size=14]Shibuya no Kesiki[/size]"

        MyTile:
            source: "./sample2.jpg"
            text: "[size=26]Keikan 2[/size]\\n[size=14]Tokyo Sky Tree No Shashin[/size]"
            tile_text_color: app.theme_cls.accent_color

        MyTile:
            source: "./sample3.jpg"
            text: "[size=26][color=#ffffff]Keikan 3[/color][/size]\\n[size=14]Shinjuku No Kesiki[/size]"
            tile_text_color: app.theme_cls.accent_color
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()
