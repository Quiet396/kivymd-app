from kivymd.app import MDApp
from kivy.lang import Builder
#from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""

<MenuScreen>:

    MDRaisedButton:
        text: "Goto Next Page"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_release: app.root.current = 'next'

<NextScreen>:

    MDRaisedButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}
        text: 'Go back'
        on_release: app.root.current = 'main'
""")


# Declare both screens
class MenuScreen(Screen):
    pass


class NextScreen(Screen):
    pass


class TestApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='main'))
        sm.add_widget(NextScreen(name='next'))

        return sm


if __name__ == '__main__':
    TestApp().run()
