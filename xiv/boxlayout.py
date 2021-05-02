from kivymd.app import MDApp
from kivy.lang import Builder


kv = '''

Screen:    
    
    MDToolbar:
        title: "Box Layout"
        pos_hint: {'top': 1}


    BoxLayout:
        orientation: "vertical"
        
        ### adaptive_height ###
        size_hint_y: None
        height: self.minimum_height
        
        ### adaptive_width ###
        #size_hint_x: None
        #height: self.minimum_width

        ### adaptive_size ###
        #size_hint: None, None
        #size: self.minimum_size

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
