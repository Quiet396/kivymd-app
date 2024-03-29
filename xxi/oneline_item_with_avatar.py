from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch

KV = '''
OneLineAvatarIconListItem:
    text: "cup cup cup!"
    on_size:
        self.ids._right_container.width = container.width
        self.ids._right_container.x = container.width

    IconLeftWidget:
        icon: "cup"

    Container:
        id: container

        MDIconButton:
            icon: "thumb-up"

        MDIconButton:
            icon: "thumb-down"
'''


class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

