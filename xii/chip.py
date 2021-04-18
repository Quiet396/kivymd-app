from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.toast import toast

kv = """
Screen:

    MDToolbar:
        title: app.title
        pos_hint: {"top": 1}
        left_action_items: [["menu", lambda x: x]]

    MDLabel:
        text: "Chips"
        pos_hint: {"center_x": .5, "center_y": .85}

    MDSeparator:
        pos_hint: {"center_x": .5, "center_y": .8}

    ### Use custom icon    

    MDChip:
        label: "Coffee"
        color: .4470588235294118, .19607843137254902, 0, 1
        icon: "coffee"
        callback: app.callback
        pos_hint: {"center_x": .15, "center_y": .7}

     ### Use without icon 
    
    MDChip:
        label: "Without icon"
        icon: ""
        callback: app.callback
        pos_hint: {"center_x": .15, "center_y": .6}

    ### Chips with check 

    MDChip:
        label: "Check with icon"
        icon: "city"
        check: True
        callback: app.callback
        pos_hint: {"center_x": .22, "center_y": .5}

    ### Choose chip

    MDChooseChip:

        MDChip:
            label: "Earth"
            icon: "earth"
            callback: app.callback
            selected_chip_color: .21176470535294, .098039627451, 1, 1

        MDChip:
            label: "Face"
            icon: "face"
            callback: app.callback
            selected_chip_color: .21176470535294, .098039627451, 1, 1

        MDChip:
            label: "Facebook"
            icon: "facebook"
            callback: app.callback
            selected_chip_color: .21176470535294, .098039627451, 1, 1
"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD Examples - Chips"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(kv)

    def callback(self, instance, value):
        # print(instance) # chip object
        # print(value)    # text
        toast(value)


if __name__ == "__main__":
    MainApp().run()
