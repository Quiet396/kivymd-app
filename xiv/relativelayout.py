from kivymd.app import MDApp
from kivy.lang import Builder


kv = '''

Screen:    
    
    MDToolbar:
        title: "Relative Layout"
        pos_hint: {'top': 1}

    RelativeLayout:
        canvas:
            Color:
                rgba: 0, 1, 1, 1
            RoundedRectangle:
                pos: (400, 300)
                size: self.size
                radius: [25, ]
        
        MDRectangleFlatButton:
            text: "BUTTON 1"
            pos: 10, 200

        MDRectangleFlatButton:
            text: "BUTTON 2"
            pos: 300, 200

        MDRectangleFlatButton:
            text: "BUTTON 3"
            pos: 10, 10

        MDRectangleFlatButton:
            text: "BUTTON 4"
            pos: 300, 10
'''

class Test(MDApp):

    def build(self):
        return Builder.load_string(kv)

Test().run()
