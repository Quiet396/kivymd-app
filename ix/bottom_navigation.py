from kivymd.app import MDApp
from kivy.lang import Builder

### font package
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles

class Test(MDApp):

    def build(self):
        ### self.theme_cls.primary_palette = "Gray"
        
        ### add font info
        LabelBase.register(name="gomarice_mukasi_mukasi",fn_regular="gomarice_mukasi_mukasi.ttf")
        theme_font_styles.append('gomarice_mukasi_mukasi')
        self.theme_cls.font_styles["gomarice_mukasi_mukasi"] = ["gomarice_mukasi_mukasi", 32, 0.15]

        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Bottom navigation'
        #md_bg_color: .2, .2, .2, 1
        #specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        #panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'season1'
            icon: 'human-male-female'

            MDLabel:
                text: 'いま今、あるところにおじいさんと\\nおばあさんがいました。'
                font_style: "gomarice_mukasi_mukasi"
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'season2'
            icon: 'golf-cart'

            MDLabel:
                text: 'おじいさんは山でゴルフに、\\nおばあさんは近所の\\nコインランドリーへ。'
                font_style: "gomarice_mukasi_mukasi"
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'end.'
            icon: 'clock-end'

            MDLabel:
                text: 'めでたし、めでたし。'
                font_style: "gomarice_mukasi_mukasi"
                halign: 'center'
'''
        )


Test().run()

