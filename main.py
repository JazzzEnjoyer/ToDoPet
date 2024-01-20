from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class ToDoApp(MDApp):
    def build(self):
        return MDLabel(text="ToDo", halign="center")


ToDoApp().run()