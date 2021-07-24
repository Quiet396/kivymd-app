from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)
    on_active: app.on_checkbox_active(*args)


MDFloatLayout:

    Check:
        active: True
        pos_hint: {'center_x': .4, 'center_y': .5}
#        on_active: app.on_checkbox_active(*args)

    Check:
        pos_hint: {'center_x': .6, 'center_y': .5}
#        on_active: app.on_checkbox_active(*args)
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')

Test().run()
