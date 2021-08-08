from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    # Indeterminate mode
    MDSpinner:
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .3, 'center_y': .5}
        #color: [0.8,0.8,0.8,1]
        active: True if check.active else False

    # Spinner palette
    MDSpinner:
        # The number of color values can be any.
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        palette:
            [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1], [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1], [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1], [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
        active: True if check.active else False

    # Determinate mode
    MDSpinner:
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .7, 'center_y': .5}
        determinate: True
        active: True if check.active else False

    MDCheckbox:
        id: check
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .4}
        active: True
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()

