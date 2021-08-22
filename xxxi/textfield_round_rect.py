from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
Screen:

    BoxLayout:
        orientation: "vertical"
        
        MDLabel:
            text: "MDTextFieldRect"

        MDTextFieldRect:
            #password: True

        MDSeparator:
        
        MDLabel:
            text: "MDTextFieldRound"
 
        MDTextFieldRound:
            hint_text: 'Empty field'
    
        MDTextFieldRound:
            icon_left: "email"
            hint_text: "Field with left icon"
    
        MDTextFieldRound:
            icon_left: 'key-variant'
            icon_right: 'eye-off'
            hint_text: 'Field with left and right icons'
    
        MDTextFieldRound:
            icon_left: 'key-variant'
            normal_color: app.theme_cls.accent_color
    
        MDTextFieldRound:
            icon_left: 'key-variant'
            normal_color: app.theme_cls.accent_color
            color_active: 1, 0, 0, 1
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
    
    def build(self):
        return self.screen

Test().run()

