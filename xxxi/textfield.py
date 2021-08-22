from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''

ScrollView:

    MDList:
        MDLabel:
            text: "MDTextField"
        
        # Without helper text mode
        MDTextField:
            hint_text: "No helper text"
    
        # Helper text mode on on_focus event
        MDTextField:
            hint_text: "Helper text on focus"
            helper_text: "This will disappear when you click off"
            helper_text_mode: "on_focus"
    
        # Persistent helper text mode
        MDTextField:
            hint_text: "Persistent helper text"
            helper_text: "Text is always here"
            helper_text_mode: "persistent"
    
        # Helper text mode ‘on_error’
        MDTextField:
            id: text_field_error
            hint_text: "Helper text on error (press 'Enter')"
            helper_text: "There will always be a mistake"
            helper_text_mode: "on_error"
    
        # Helper text mode ‘on_error’ (with required)
        MDTextField:
            hint_text: "required = True"
            required: True
            helper_text_mode: "on_error"
            helper_text: "Enter text"

        # Text length control    
        MDTextField:
            hint_text: "Max text length = 5"
            max_text_length: 5
    
        # Multi line text
        MDTextField:
            multiline: True
            hint_text: "Multi-line text"

        # Rectangle mode
        MDTextField:
            hint_text: "Rectangle mode"
            mode: "rectangle"
        
        # Fill mode 
        MDTextField:
            hint_text: "Fill mode"
            mode: "fill"
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
    
    def build(self):
        self.screen.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True

Test().run()

