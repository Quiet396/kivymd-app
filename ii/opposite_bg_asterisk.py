KV = '''
<Box@BoxLayout>:
    bg: 0, 0, 0, 0

    canvas:
        Color:
            rgba: root.bg
        Rectangle:
            pos: self.pos
            size: self.size

BoxLayout:

    Box:
        bg: app.theme_cls.opposite_bg_light
    Box:
        bg: app.theme_cls.opposite_bg_normal
    Box:
        bg: app.theme_cls.opposite_bg_dark
    Box:
        bg: app.theme_cls.opposite_bg_darkest
'''

from kivy.lang import Builder

from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  # "Light"
        return Builder.load_string(KV)


MainApp().run()
