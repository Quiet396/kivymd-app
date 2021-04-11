from kivymd.app import MDApp
from kivy.lang import Builder

### import font package
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles


KV = '''
Screen:

   MDToolbar:
      title: "Example Carousel"
      pos_hint: {"top": 1}
   
   Carousel:
      MDLabel:
         text: "いま今、あるところにおじいさんと\\nおばあさんがいました。"
         halign: "center"
         font_style: "gomarice_mukasi_mukasi"
      MDLabel:
         text: "おじいさんは山でゴルフに、\\nおばあさんは近所の\\nコインランドリーへ。"
         halign: "center"
         font_style: "gomarice_mukasi_mukasi"
      MDLabel:
         text: "おじいさんはスコアが\\nやっと110に届き。"
         halign: "center"
         font_style: "gomarice_mukasi_mukasi"
      MDLabel:
         text: "おばあさんは、\\nお札を入れる向きが\\n分からずイライラしてしまい。"
         halign: "center"
         font_style: "gomarice_mukasi_mukasi"
      MDLabel:
         text: "おしまい。"
         halign: "center"
         font_style: "gomarice_mukasi_mukasi"
'''


class CarouselApp(MDApp):
    def build(self):
       ### font setting
       LabelBase.register(name="gomarice_mukasi_mukasi",fn_regular="gomarice_mukasi_mukasi.ttf")
       theme_font_styles.append('gomarice_mukasi_mukasi')
       self.theme_cls.font_styles["gomarice_mukasi_mukasi"] = ["gomarice_mukasi_mukasi", 32, 0.15]
       
       return Builder.load_string(KV)


CarouselApp().run()
