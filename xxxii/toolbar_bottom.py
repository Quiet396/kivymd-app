from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:

    # Will always be at the bottom of the screen.
    MDBottomAppBar:
        md_bg_color: 0, 1, 0, 1

        MDToolbar:
            title: "Title"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            on_action_button: app.call(self.icon)
            mode: "free-end"
            icon_color: 0, 1, 0, 1
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def call(self, icon):
        print("icon is : " + icon)


Test().run()
