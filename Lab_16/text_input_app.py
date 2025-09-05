#•	Text Input App (This app allows users to type in a text field and display the typed text on the screen when a button is pressed.)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 16
        self.spacing = 10

        # Instruction
        self.add_widget(Label(text="Type something below:", size_hint=(1, .15), font_size='18sp'))

        # Text input
        self.user_input = TextInput(multiline=False, hint_text="Enter text here", size_hint=(1, .15), font_size='18sp')
        self.add_widget(self.user_input)

        # Show button
        show_btn = Button(text="Show Text", size_hint=(1, .15), font_size='20sp')
        show_btn.bind(on_press=self.show_text)
        self.add_widget(show_btn)

        # Output label
        self.output_label = Label(text="", size_hint=(1, .55), font_size='20sp')
        self.add_widget(self.output_label)

    def show_text(self, instance):
        txt = self.user_input.text.strip()
        if txt:
            self.output_label.text = f"You typed: {txt}"
        else:
            self.output_label.text = "You typed nothing."

class TextInputApp(App):
    def build(self):
        return TextInputLayout()

if __name__ == "__main__":
    TextInputApp().run()
