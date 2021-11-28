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

    MDBoxLayout:
        padding: dp(10)
        spacing: dp(10)
        adaptive_height: True
        orientation: "vertical"
        pos_hint: {"center_x": .5}
        md_bg_color: 0, 0.3828215, 0.625, 1 # Cobalt Blue
        #md_bg_color: 0, 0.3828215, 0.625, 0 # Cobalt Blue alpha 0.5
        #md_bg_color: 0.16796875, 0.29296875, 0.39453125, 1 # Indigo
        #md_bg_color: 0.16796875, 0.29296875, 0.39453125, 0.5 # Indigo alpha 0.5
        line_color: 1, 0, 0, 1

        MDIconButton:
            icon: "sd"
            pos_hint: {"center_x": .5}
            on_release: print(app.theme_cls.primary_color)

        MDFloatingActionButton:
            icon: "plus"
            opposite_colors: True
            elevation_normal: 8
            pos_hint: {"center_x": .5}

        MDFlatButton:
            text: "MDFlatButton"
            pos_hint: {"center_x": .5}

        MDRaisedButton:
            text: "MDRaisedButton"
            elevation_normal: 2
            opposite_colors: True
            pos_hint: {"center_x": .5}

        MDRectangleFlatButton:
            text: "MDRectangleFlatButton"
            pos_hint: {"center_x": .5}

        MDRectangleFlatIconButton:
            text: "MDRectangleFlatIconButton"
            icon: "language-python"
            width: dp(230)
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
            'Python': 'language-python',
            'PHP': 'language-php',
            'C++': 'language-cpp',
        }
        super().__init__(**kwargs)

    def build(self):
        self.root = Factory.ExampleButtons()


if __name__ == "__main__":
    MainApp().run()
