from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.snackbar import Snackbar

KV = '''
Screen:

    MyButton:
        text: "PRESS ME"
        pos_hint: {"center_x": .5, "center_y": .5}

'''


class MyButton(MDRaisedButton, TouchBehavior):
    def on_long_touch(self, *args):
        Snackbar(text="on long touch event!").open()

    def on_double_tap(self, *args):
        Snackbar(text="on double tap event!").open()

    def on_triple_tap(self, *args):
        Snackbar(text="on triple tap event!").open()


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

