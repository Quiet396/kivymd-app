from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
ScrollView:

    MDList:
        
        OneLineListItem:
            text: "Single-line item"

        TwoLineListItem:
            text: "Two-line item"
            secondary_text: "Secondary text here"

        ThreeLineListItem:
            text: "Three-line item"
            secondary_text: "This is a multi-line label where you can"
            tertiary_text: "fit more text than usual"
        
        OneLineAvatarListItem:
            text: "Single-line item with avatar"

            ImageLeftWidget:
                source: "data/logo/kivy-icon-256.png"

        TwoLineAvatarListItem:
            text: "Two-line item with avatar"
            secondary_text: "Secondary text here"

            ImageLeftWidget:
                source: "data/logo/kivy-icon-256.png"

        ThreeLineAvatarListItem:
            text: "Three-line item with avatar"
            secondary_text: "Secondary text here"
            tertiary_text: "fit more text than usual"

            ImageLeftWidget:
                source: "data/logo/kivy-icon-256.png"

        OneLineIconListItem:
            text: "Single-line item with avatar"

            IconLeftWidget:
                icon: "language-python"

        TwoLineIconListItem:
            text: "Two-line item with avatar"
            secondary_text: "Secondary text here"

            IconLeftWidget:
                icon: "language-python"

        ThreeLineIconListItem:
            text: "Three-line item with avatar"
            secondary_text: "Secondary text here"
            tertiary_text: "fit more text than usual"

            IconLeftWidget:
                icon: "language-python"

        OneLineAvatarIconListItem:
            text: "One-line item with avatar"

            IconLeftWidget:
                icon: "plus"

            IconRightWidget:
                icon: "minus"

        TwoLineAvatarIconListItem:
            text: "Two-line item with avatar"
            secondary_text: "Secondary text here"

            IconLeftWidget:
                icon: "plus"

            IconRightWidget:
                icon: "minus"

        ThreeLineAvatarIconListItem:
            text: "Three-line item with avatar"
            secondary_text: "Secondary text here"
            tertiary_text: "fit more text than usual"

            IconLeftWidget:
                icon: "plus"

            IconRightWidget:
                icon: "minus"

        OneLineAvatarIconListItem:
            on_release: print("Click 2!")

            IconLeftWidget:
                icon: "gitlab"
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

