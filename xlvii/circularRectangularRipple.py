from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

from kivymd.app import MDApp
from kivymd.uix.behaviors import CircularRippleBehavior, RectangularRippleBehavior, BackgroundColorBehavior

KV = '''
MDScreen:

    CircularRippleButton:
        source: "./photo/genba_neko.png"
        size_hint: None, None
        size: "250dp", "250dp"
        pos_hint: {"center_x": .3, "center_y": .5}

    RectangularRippleButton:
        size_hint: None, None
        size: "250dp", "50dp"
        pos_hint: {"center_x": .7, "center_y": .5}
'''


class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)


class RectangularRippleButton(
    RectangularRippleBehavior, ButtonBehavior, BackgroundColorBehavior
):
    #ripple_scale = 1.00
    md_bg_color = [0, 0, 1, 1]


class Example(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


Example().run()
