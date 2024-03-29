from kivymd.app import MDApp
from kivy.lang.builder import Builder

kv = '''
<MySwiper@MDSwiperItem>

    FitImage:
        source: "./photo/saya&kesiki/saya160104274702_TP_V.jpg"
        radius: [20,]

MDScreen:

    MDToolbar:
        id: toolbar
        title: "MDSwiper"
        elevation: 10
        pos_hint: {"top": 1}

    MDSwiper:
        size_hint_y: None
        height: root.height - toolbar.height - dp(20)
        y: root.height - self.height - toolbar.height - dp(20)

        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)

Main().run()
