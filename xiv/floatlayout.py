from kivymd.app import MDApp
from kivy.lang import Builder


kv = '''

Screen:    
    
    MDToolbar:
        title: "Float Layout"
        pos_hint: {'top': 1}


    FloatLayout:
        #canvas:
        #    Color:
        #        rgba: 0, 1, 1, 1
        #    RoundedRectangle:
        #        pos: self.pos
        #        size: self.size
        #        radius: [25, 0, 0, 0]
        
        MDRectangleFlatButton:
            text: "BUTTON 1"
            pos: 10, 460

        MDRectangleFlatButton:
            text: "BUTTON 2"
            pos: 690, 460

        MDRectangleFlatButton:
            text: "BUTTON 3"
            pos: 360, 240

        MDRectangleFlatButton:
            text: "BUTTON 4"
            pos: 10, 10

        MDRectangleFlatButton:
            text: "BUTTON 5"
            pos: 690, 10
'''

class Test(MDApp):

    def build(self):
        return Builder.load_string(kv)

Test().run()
