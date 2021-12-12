from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import FakeRectangularElevationBehavior, RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
MDFloatLayout:

    ElevatedWidget:
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint: None, None
        size: 100, 100
        md_bg_color: 0, 0, 1, 1
'''


class ElevatedWidget(
    ThemableBehavior,
    FakeRectangularElevationBehavior,
    RectangularRippleBehavior,
    ButtonBehavior,
    MDBoxLayout,
):
    shadow_animation = ObjectProperty()

    def on_press(self, *args):
        if self.shadow_animation:
            Animation.cancel_all(self, "_elevation")
        self.shadow_animation = Animation(_elevation=self.elevation + 10, d=0.4)
        self.shadow_animation.start(self)

    def on_release(self, *args):
        if self.shadow_animation:
            Animation.cancel_all(self, "_elevation")
        self.shadow_animation = Animation(_elevation=self.elevation, d=0.1)
        self.shadow_animation.start(self)


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()
