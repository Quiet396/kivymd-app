from kivymd.app import MDApp
from kivy.lang import Builder


kv = '''

Screen:    
    
    MDToolbar:
        title: "Box Layout"
        pos_hint: {'top': 1}


    MDBoxLayout:
        orientation: "vertical"
       
        adaptive_size: True 
        
        padding: dp(10)
        spacing: dp(10)

        canvas:
            Color:
                rgba: 0, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        MDRectangleFlatButton:
            text: "BUTTON 1"
            size: 20, 20

        MDRectangleFlatButton:
            text: "BUTTON 2"
            size: 30, 30

        MDRectangleFlatButton:
            text: "BUTTON 3"
            size: 40, 40

        MDRectangleFlatButton:
            text: "BUTTON 4"
            size: 50, 50

        MDRectangleFlatButton:
            text: "BUTTON 5"
            size: 60, 60
'''

class Test(MDApp):

    def build(self):
        return Builder.load_string(kv)

Test().run()
