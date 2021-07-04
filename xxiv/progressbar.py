from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:
    padding: "10dp"

    MDProgressBar:
        #orientation: "vertical"
        #color: app.theme_cls.accent_color
        value: 10
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()

