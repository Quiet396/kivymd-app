from kivymd.app import MDApp
from kivy.lang import Builder


kv = '''

Screen:    
    
    MDToolbar:
        title: "Stack Layout"
        pos_hint: {'top': 1}


    MDStackLayout:
        ### capture 4 ###
        orientation: "lr-tb"
        adaptive_size: True

        ### capture 5 ###
        #orientation: "bt-rl"

        MDRectangleFlatButton:
            text: "BUTTON 1"

        MDRectangleFlatButton:
            text: "BUTTON 2"

        MDRectangleFlatButton:
            text: "BUTTON 3"

        MDRectangleFlatButton:
            text: "BUTTON 4"

'''

class Test(MDApp):

    def build(self):
        return Builder.load_string(kv)

Test().run()
