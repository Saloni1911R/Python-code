#•	Design Counter App (This app has a button that increments a counter displayed on the screen every time the button is clicked)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        # Counter label
        self.count = 0
        self.label = Label(text=f"Count: {self.count}", font_size='40sp', size_hint=(1, .6))
        self.add_widget(self.label)

        # Increment button
        inc_btn = Button(text="Increment", font_size='24sp', size_hint=(1, .2))
        inc_btn.bind(on_press=self.increment)
        self.add_widget(inc_btn)

        # Reset button
        reset_btn = Button(text="Reset", font_size='20sp', size_hint=(1, .2))
        reset_btn.bind(on_press=self.reset_count)
        self.add_widget(reset_btn)

    def increment(self, instance):
        self.count += 1
        self.label.text = f"Count: {self.count}"

    def reset_count(self, instance):
        self.count = 0
        self.label.text = f"Count: {self.count}"

class CounterApp(App):
    def build(self):
        return CounterLayout()

if __name__ == "__main__":
    CounterApp().run()
