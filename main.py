from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
import webbrowser
import os

Window.size = (350, 650)

KV = '''
MDScreen:
    md_bg_color: (0,0,0,1)
    Image:
        source: "logo_maluxa.jpg"
        size_hint:.85,.75
        pos_hint:{'center_x':.5,'center_y':.5}
        allow_stretch: True
        keep_ratio: True

    

    MDFloatLayout:    

        MDRaisedButton:
            md_bg_color:0.251, 0.878, 0.816, 1

            

            text: "INICIAR"
            #font_name: "Montserrat-Bold.ttf"
            pos_hint: {"center_x": .5,"center_y":.15}
            on_release: app.switch_theme_style()
'''

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def switch_theme_style(self):
        
        webbrowser.open("https://www.boomplay.com/")


Example().run()
