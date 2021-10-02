from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem

KV = '''
<ItemDrawer>:

    IconLeftWidget:
        icon: root.icon

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "./genba_neko.png"

    MDLabel:
        text: "User_name of TwitterClone"
        font_style: "Button"
        adaptive_height: True

    MDLabel:
        text: "@screen_name of TwitterClone"
        font_style: "Caption"
        adaptive_height: True

    MDBoxLayout:
        adaptive_height: True
        spacing: "1dp"

        MDLabel:
            text: "123 follow"
            font_style: "Button"
            adaptive_height: True

        MDLabel:
            text: "456 follower"
            font_style: "Button"
            adaptive_height: True

    ScrollView:

        MDList:

            ItemDrawer:
                icon: "account"
                text: "Profile"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "profile"

            ItemDrawer:
                icon: "note-text-outline"
                text: "List"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "list"

            ItemDrawer:
                icon: "comma-circle-outline"
                text: "Topic"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "topic"

            ItemDrawer:
                icon: "bookmark-outline"
                text: "Bookmark"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "bookmark"

            ItemDrawer:
                icon: "lightning-bolt-outline"
                text: "Moment"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "moment"
            
            MDSeparator:

            ItemDrawer:
                icon: "arrow-top-right-thin-circle-outline"
                text: "Twitter Ad"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "twitter_ad"
            
            MDSeparator:

            OneLineListItem:
                text: "Setting And Privacy"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "setting_privacy"

            OneLineListItem:
                text: "Help Center"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "help_center"

MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Twitter Clone(imperfect)"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "profile"

                MDLabel:
                    text: "Profile"
                    halign: "center"

            MDScreen:
                name: "list"

                MDLabel:
                    text: "List"
                    halign: "center"

            MDScreen:
                name: "topic"

                MDLabel:
                    text: "Topic"
                    halign: "center"

            MDScreen:
                name: "bookmark"

                MDLabel:
                    text: "Bookmark"
                    halign: "center"

            MDScreen:
                name: "moment"

                MDLabel:
                    text: "Moment"
                    halign: "center"

            MDScreen:
                name: "twitter_ad"

                MDLabel:
                    text: "Twitter Ad"
                    halign: "center"

            MDScreen:
                name: "setting_privacy"

                MDLabel:
                    text: "Setting And Privacy"
                    halign: "center"

            MDScreen:
                name: "help_center"

                MDLabel:
                    text: "Help Center"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class ContentNavigationDrawer(MDBoxLayout):
    pass

class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


TestNavigationDrawer().run()
