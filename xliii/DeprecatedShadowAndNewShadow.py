from kivy.lang import Builder
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<Box@MDBoxLayout>
    adaptive_size: True
    orientation: "vertical"
    spacing: "36dp"


<BaseShadowWidget>
    size_hint: None, None
    size: 100, 100
    md_bg_color: 0, 0, 1, 1
    elevation: 36
    pos_hint: {'center_x': .5}


MDFloatLayout:

    MDBoxLayout:
        adaptive_size: True
        pos_hint: {'center_x': .5, 'center_y': .5}
        spacing: "56dp"

        Box:

            MDLabel:
                text: "Deprecated shadow rendering"
                adaptive_size: True

            DeprecatedShadowWidget:

            MDLabel:
                text: "Doesn't require a lot of resources"
                adaptive_size: True

        Box:

            MDLabel:
                text: "New shadow rendering"
                adaptive_size: True

            NewShadowWidget:

            MDLabel:
                text: "It takes a lot of resources"
                adaptive_size: True
'''


class BaseShadowWidget(Widget):
    pass


class DeprecatedShadowWidget(MDCard, BaseShadowWidget):
    '''Deprecated shadow rendering. Doesn't require a lot of resources.'''


class NewShadowWidget(RectangularElevationBehavior, BaseShadowWidget, MDBoxLayout):
    '''New shadow rendering. It takes a lot of resources.'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()
