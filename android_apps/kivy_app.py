from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.progressbar import MDProgressbar
from kivymd.uix.
Builder.load_string("""
<Box>:
    orientation: 'vertical'
    AsyncImage:
        source:"http://192.168.43.67:5000/static/image/ic_launcher.png"
""")


class Box(BoxLayout):
    ...


class MyApp(MDApp):
    def build(self):
        return Box()


MyApp().run()
