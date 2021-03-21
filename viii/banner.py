from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.app import MDApp

Builder.load_string('''
<ExampleBanner@Screen>

    MDBanner:
        id: banner
        text: ["One line string text example without actions."]
        
        # two-line
        #type: "two-line"
        #text:
        #    ["One line string text example without actions.", "This is the second line of the banner message."]
        
        # three-line
        #type: "three-line"
        #text:
        #    ["One line string text example without actions.", "This is the second line of the banner message.", "and this is the third line of the banner message."]

        # one-button
        #text: ["One line string text example without actions."]
        #left_action: ["CANCEL", lambda x: None]
        
        # two-buttons
        #text: ["One line string text example without actions."]
        #left_action: ["CANCEL", lambda x: None]
        #right_action: ["CLOSE", lambda x: None]
        
        # one-line with icon
        
        #type: "one-line-icon"
        #icon: f"{images_path}kivymd_logo.png"
        #text: ["One line string text example without actions."]
        
        # The widget that is under the banner.
        # It will be shifted down to the height of the banner.
        over_widget: screen
        #vertical_pad: toolbar.height
        vertical_pad: 80

    MDToolbar:
        id: toolbar
        title: "Example Banners"
        elevation: 10
        pos_hint: {'top': 1}

    BoxLayout:
        id: screen
        orientation: "vertical"
        size_hint_y: None
        height: Window.height - toolbar.height

        OneLineListItem:
            text: "Banner without actions"
            on_release: banner.show()

        Widget:
''')


class Test(MDApp):
    def build(self):
        return Factory.ExampleBanner()


Test().run()

