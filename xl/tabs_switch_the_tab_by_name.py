from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Example Tabs"

    MDTabs:
        id: tabs


<Tab>

    MDBoxLayout:
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        spacing: dp(48)

        MDIconButton:
            id: icon
            icon: "arrow-right"
            user_font_size: "48sp"
            on_release: app.switch_tab_by_name()

        MDIconButton:
            id: icon2
            icon: "page-next"
            user_font_size: "48sp"
            on_release: app.switch_tab_by_object()
'''


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class Example(MDApp):
    icons = list(md_icons.keys())[15:30]

    def build(self):
        self.iter_list_names = iter(list(self.icons))
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab in list(self.icons):
            self.root.ids.tabs.add_widget(Tab(tab_label_text=name_tab))
        self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))

    def switch_tab_by_object(self):
        try:
            x = next(self.iter_list_objects)
            print(f"Switch slide by object, next element to show: [{x}]")
            self.root.ids.tabs.switch_tab(x)
        except StopIteration:
            # reset the iterator an begin again.
            self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))
            self.switch_tab_by_object()

    def switch_tab_by_name(self):
        '''Switching the tab by name.'''

        try:
            x = next(self.iter_list_names)
            print(f"Switch slide by name, next element to show: [{x}]")
            self.root.ids.tabs.switch_tab(x)
        except StopIteration:
            # Reset the iterator an begin again.
            self.iter_list_names = iter(list(self.icons))
            self.switch_tab_by_name()


Example().run()
