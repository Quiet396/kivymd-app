from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager #, Screen
from kivymd.uix.screen import MDScreen

KV = '''

ScreenManager:
    MenuScreen:
    NextScreen:

<MenuScreen>:
    name: "main"

    MDRaisedButton:
        text: "Goto Next Page"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_release: app.root.current = 'next'

<NextScreen>:
    name: "next"

    MDRaisedButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Go back'
        on_release: app.root.current = 'main'
'''


# Declare both screens
class MenuScreen(MDScreen):
    pass


class NextScreen(MDScreen):
    pass


class TestApp(MDApp):

    def build(self):
        screen = Builder.load_string(KV)
        return screen

if __name__ == '__main__':
    TestApp().run()
