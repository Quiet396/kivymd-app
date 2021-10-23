from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import BaseSnackbar

KV = '''
<CustomSnackbar>

    MDIconButton:
        pos_hint: {'center_y': .5}
        icon: root.icon
        opposite_colors: True

    MDLabel:
        id: text_bar
        size_hint_y: None
        height: self.texture_size[1]
        text: root.text
        font_size: root.font_size
        theme_text_color: 'Custom'
        text_color: get_color_from_hex('ffffff')
        shorten: True
        shorten_from: 'right'
        pos_hint: {'center_y': .5}


Screen:

    MDRaisedButton:
        text: "SHOW"
        pos_hint: {"center_x": .5, "center_y": .45}
        on_press: app.show()
'''


class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def show(self):
        snackbar = CustomSnackbar(
            text="[color=#ddbb34]This is a snackbar![/color]",
            icon="information",
            # Usage with snackbar_x, snackbar_y
            snackbar_x="10dp",
            snackbar_y="10dp",
            # Usage with button
            buttons=[MDFlatButton(text="ACTION", text_color=(1, 0, 0, 1))],
            # Using a button with custom color
            bg_color=(0, 0.5, 0.5, 1)
        )
        # Control width
        snackbar.size_hint_x = (
            Window.width - (snackbar.snackbar_x * 2)
        ) / Window.width
        #print("window.width={0}, snackbar.snackbar_x={1}".format(Window.width, snackbar.snackbar_x))
        snackbar.open()


Test().run()

