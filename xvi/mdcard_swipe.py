from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCard

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
                
                MDCardSample:
                MDCardSample:
                MDCardSample:
                MDCardSample:
                MDCardSample:

<MDCardSample@MDCard>:
    orientation: "vertical"

    MDLabel:
        text: "Title"
        theme_text_color: "Secondary"
        size_hint_y: None
        height: self.texture_size[1]

    MDSeparator:
        height: "1dp"

    MDLabel:
        text: "Body"
'''


class TestCard(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen

    def on_start(self):
        '''Creates a list of cards.'''


TestCard().run()
