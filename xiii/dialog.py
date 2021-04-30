from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
'''


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type='alert', # List -> ‘alert’, ‘simple’, ‘confirmation’, ‘custom’
                title="So what do you want to do?",
                text="Discard draft?",
                buttons=[
                    MDFlatButton(text="CANCEL"), 
                    MDRaisedButton(text="DISCARD"),
                ],
            )
        self.dialog.open()


Example().run()
