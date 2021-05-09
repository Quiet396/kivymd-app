from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

KV = '''

MDScreen:

    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        pos_hint: {"center_x": .5}
        
        MDToolbar:
            elevation: 10
            title: "MDCardList"
            pos_hint: {'top': 1}
        
        ScrollView:
            scroll_timeout : 100

            MDList:
                id: md_list
                padding: 0

<MDCardSample>:
    orientation: "vertical"

    MDLabel:
        id: label1
        text: root.title
        theme_text_color: "Secondary"
        size_hint_y: None
        height: self.texture_size[1]

    MDSeparator:
        height: "1dp"

    MDLabel:
        id: label2
        text: root.body
'''

class MDCardSample(MDCard):
    title = StringProperty()
    body = StringProperty()

class TestCard(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen

    def on_start(self):
        for i in range(20):
            self.screen.ids.md_list.add_widget(
                MDCardSample(title=f"card item{i}", body=f"contents {i}")
            )

TestCard().run()
