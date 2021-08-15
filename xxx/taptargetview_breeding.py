from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.taptargetview import MDTapTargetView

KV = '''
Screen:

    MDFloatingActionButton:
        id: button_left_top
        icon: "plus"
        pos: 50, 480
        on_release: app.tap_target_view_lt.start() if app.tap_target_view_lt.state == "close" else app.tap_target_view_lt.stop()

    MDFloatingActionButton:
        id: button_top
        icon: "plus"
        pos: 150, 480
        on_release: app.tap_target_view_t.start() if app.tap_target_view_t.state == "close" else app.tap_target_view_t.stop()

    MDFloatingActionButton:
        id: button_right_top
        icon: "plus"
        pos: 250, 480
        on_release: app.tap_target_view_rt.start() if app.tap_target_view_rt.state == "close" else app.tap_target_view_rt.stop()

    MDFloatingActionButton:
        id: button_left
        icon: "plus"
        pos: 50, 240
        on_release: app.tap_target_view_l.start() if app.tap_target_view_l.state == "close" else app.tap_target_view_l.stop()

    MDFloatingActionButton:
        id: button_center
        icon: "plus"
        pos: 150, 240
        on_release: app.tap_target_view_c.start() if app.tap_target_view_c.state == "close" else app.tap_target_view_c.stop()

    MDFloatingActionButton:
        id: button_right
        icon: "plus"
        pos: 250, 240
        on_release: app.tap_target_view_r.start() if app.tap_target_view_r.state == "close" else app.tap_target_view_r.stop()

    MDFloatingActionButton:
        id: button_left_bottom
        icon: "plus"
        pos: 50, 30
        on_release: app.tap_target_view_lb.start() if app.tap_target_view_lb.state == "close" else app.tap_target_view_lb.stop()

    MDFloatingActionButton:
        id: button_bottom
        icon: "plus"
        pos: 150, 30
        on_release: app.tap_target_view_b.start() if app.tap_target_view_b.state == "close" else app.tap_target_view_b.stop()

    MDFloatingActionButton:
        id: button_right_bottom
        icon: "plus"
        pos: 250, 30
        on_release: app.tap_target_view_rb.start() if app.tap_target_view_rb.state == "close" else app.tap_target_view_rb.stop()
'''


class TapTargetViewDemo(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view_lt = MDTapTargetView(
            widget=screen.ids.button_left_top,
            title_text="Title text",
            title_text_size="36sp",
            description_text="Description text",
            description_text_color=[1, 0, 0, 1],
            widget_position="left_top",
        )
        
        self.tap_target_view_t = MDTapTargetView(
            widget=screen.ids.button_top,
            title_text="This is an add top button",
            description_text="This is a description of the top button",
            outer_circle_color=(1, 0, 0),
            widget_position="top",
        )
        
        self.tap_target_view_rt = MDTapTargetView(
            widget=screen.ids.button_right_top,
            title_text="This is an add right top button",
            description_text="This is a description of the right top button",
            target_circle_color=(0, 1, 0),
            widget_position="right_top",
        )

        self.tap_target_view_l = MDTapTargetView(
            widget=screen.ids.button_left,
            title_text="This is an add left button",
            description_text="This is a description of the left button",
            outer_radius="150dp",
            widget_position="left",
        )
        
        self.tap_target_view_c = MDTapTargetView(
            widget=screen.ids.button_center,
            title_text="This is an add center button",
            title_position="left_top",
            description_text="This is a description of the center button",
            widget_position="center",
        )
        
        self.tap_target_view_r = MDTapTargetView(
            widget=screen.ids.button_right,
            title_text="This is an add right button",
            description_text="This is a description of the right button",
            target_radius="30dp",
            widget_position="right",
        )
        
        self.tap_target_view_lb = MDTapTargetView(
            widget=screen.ids.button_left_bottom,
            title_text="This is an add left bottom button",
            description_text="This is a description of the left bottom button",
            title_text_bold=False,
            widget_position="left_bottom",
        )
        
        self.tap_target_view_b = MDTapTargetView(
            widget=screen.ids.button_bottom,
            title_text="This is an add bottom button",
            description_text="This is a description of the bottom button",
            description_text_size="5dp",
            widget_position="bottom",
        )
        
        self.tap_target_view_rb = MDTapTargetView(
            widget=screen.ids.button_right_bottom,
            title_text="This is an add right button",
            description_text="This is a description of the right button",
            description_text_bold=True,
            widget_position="right_bottom",
        )

        return screen

TapTargetViewDemo().run()
