from kivy.lang.builder import Builder

from kivymd.app import MDApp

kv = '''
<MagicButton@MagicBehavior+MDIconButton>


<MySwiper@MDSwiperItem>

    RelativeLayout:

        FitImage:
            source: "./photo/saya&kesiki/SAYA160312500I9A3721_TP_V.jpg"
            radius: [20,]

        MDBoxLayout:
            adaptive_height: True
            spacing: "12dp"

            MagicButton:
                id: icon
                icon: "thumb-up-outline"
                user_font_size: "56sp"
                opposite_colors: True

            MDLabel:
                text: "Saya"
                font_style: "H5"
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {"center_y": .5}
                # opposite_colors: True
                # add custom color
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1


MDScreen:

    MDToolbar:
        id: toolbar
        title: "MDSwiper"
        elevation: 10
        # add auto switch
        right_action_items: [["hand-pointing-left", lambda x: swiper.set_current(swiper.get_current_index() - 1)], ["hand-pointing-right", lambda x: swiper.set_current(swiper.get_current_index() + 1)]]
        pos_hint: {"top": 1}

    MDSwiper:
        id: swiper
        size_hint_y: None
        height: root.height - toolbar.height - dp(40)
        y: root.height - self.height - toolbar.height - dp(20)
        on_swipe: self.get_current_item().ids.icon.shake()
        on_pre_swipe: print("on_pre_swipe")
        on_overswipe_right: print("on_overswipe_right")
        on_overswipe_left: print("on_overswipe_left")
        on_swipe_left: print("on_swipe_left")
        on_swipe_right: print("on_swipe_right")


        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:

        MySwiper:
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)


Main().run()
