from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDFloatLayout:

    MDSwitch:
        pos_hint: {'center_x': .5, 'center_y': .6}

    MDSwitch:
        pos_hint: {'center_x': .5, 'center_y': .4}
        width: dp(64)
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
