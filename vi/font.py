KV = '''
Screen:
    MDLabel:
        text: "JetBrainsMono"
        #text: "昔々あるところにおじいさんとおばあさんがいました。\\n\\n\\n\\n\\n\\nおしまい。"
        halign: "center"
        font_style: "JetBrainsMono"
        #font_style: "gomarice_mukasi_mukasi"
'''

from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles

class MainApp(MDApp):
    def build(self):
        LabelBase.register(name="JetBrainsMono",fn_regular="JetBrainsMono-Regular.ttf")
        #LabelBase.register(name="gomarice_mukasi_mukasi",fn_regular="gomarice_mukasi_mukasi.ttf")
        
        theme_font_styles.append('JetBrainsMono')
        #theme_font_styles.append('gomarice_mukasi_mukasi')
        
        #print(type(theme_font_styles)) # ->  <class 'list'>
        #print(theme_font_styles) # -> ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Subtitle1', 'Subtitle2', 'Body1', 'Body2', 'Button', 'Caption', 'Overline', 'Icon', 'JetBrainsMono']
        
        self.theme_cls.font_styles["JetBrainsMono"] = [
                                       "JetBrainsMono",
        #self.theme_cls.font_styles["gomarice_mukasi_mukasi"] = [
        #                               "gomarice_mukasi_mukasi",
                                       32,
                                       False,
                                       0.15,
                                  ]
        return Builder.load_string(KV)

MainApp().run()

