from kivymd.app import MDApp
from kivy.lang import Builder


kv = '''

Screen:    
    
    MDToolbar:
        title: "Grid Layout"
        pos_hint: {'top': 1}


    MDGridLayout:
        cols: 2
        adaptive_size: True

        canvas:
            Color:
                rgba: 0, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
    
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
