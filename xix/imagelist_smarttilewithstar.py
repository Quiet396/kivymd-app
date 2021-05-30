from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "200dp"


ScrollView:

    MDGridLayout:
        cols: 1
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)

        MyTile:
            stars: 5
            source: "./sample1.jpg"

        MyTile:
            stars: 5
            source: "./sample2.jpg"

        MyTile:
            stars: 5
            source: "./sample3.jpg"
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()
