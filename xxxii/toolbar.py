from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"
        left_action_items: [["menu", lambda x: app.call()]]
        right_action_items: [["dots-vertical", lambda x: app.call_kebab()], ["clock", lambda x: app.call_clock()]]
        md_bg_color: app.theme_cls.accent_color
        specific_text_color: app.theme_cls.primary_color
        elevation: 10

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def call(self):
        print("left action from hamburger menu!")
    
    def call_kebab(self):
        print("right action from kebab menu!")

    def call_clock(self):
        print("right action from clock menu!")

Test().run()
