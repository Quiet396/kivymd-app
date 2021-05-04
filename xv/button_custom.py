from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp

Builder.load_string(
    """
<ExampleButtons@Screen>:

    MDToolbar:
        title: app.title
        elevation: 10
        pos_hint: {'top': 1}

    BoxLayout:
        padding: dp(10)
        size_hint: None, None
        size: self.minimum_size
        spacing: dp(10)
        orientation: "vertical"
        pos_hint: {"center_x": .5}

        MDIconButton:
            icon: "sd"
            user_font_size: "64sp"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            pos_hint: {"center_x": .5}

        MDFloatingActionButton:
            icon: "plus"
            elevation_normal: 12
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {"center_x": .5}

        MDFlatButton:
            text: "MDFlatButton"
            pos_hint: {"center_x": .5}
            text_color: 1, 0, 0, 1

        MDRaisedButton:
            text: "MDRaisedButton"
            elevation_normal: 2
            #opposite_colors: True
            md_bg_color: 1, 0, 1, 1
            pos_hint: {"center_x": .5}

        MDRectangleFlatButton:
            text: "MDRectangleFlatButton"
            pos_hint: {"center_x": .5}

        MDRectangleFlatIconButton:
            text: "MDRectangleFlatIconButton"
            icon: "language-python"
            width: dp(230)
            text_color: 0, 0, 1, 1
            line_color: 1, 0, 1, 1
            icon_color: 1, 0, 0, 1
            pos_hint: {"center_x": .5}

        MDRoundFlatButton:
            text: "MDRoundFlatButton"
            pos_hint: {"center_x": .5}

        MDRoundFlatIconButton:
            text: "MDRoundFlatIconButton"
            icon: "language-python"
            width: dp(200)
            pos_hint: {"center_x": .5}

        MDFillRoundFlatButton:
            text: "MDFillRoundFlatButton"
            pos_hint: {"center_x": .5}

        MDFillRoundFlatIconButton:
            text: "MDFillRoundFlatIconButton"
            icon: "language-python"
            pos_hint: {"center_x": .5}

        MDTextButton:
            text: "MDTextButton"
            color: 0, 1, 0, 1
            pos_hint: {"center_x": .5}
    
    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True
"""
)


class MainApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "KivyMD Examples - Buttons"
        self.data = {
            'language-python': 'Python',
            'language-php': 'PHP',
            'language-cpp': 'C++',
        }
        super().__init__(**kwargs)

    def build(self):
        self.root = Factory.ExampleButtons()


if __name__ == "__main__":
    MainApp().run()
