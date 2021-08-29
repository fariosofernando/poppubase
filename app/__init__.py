
# Python

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.animation import Animation


Builder.load_file("./app/view/home_style.kv")
class MainHome(Screen):
    def __init__(self, **kw):
        super(MainHome, self).__init__(**kw)

    def abrir_menu(self, widget): 
        tamanho = Window.width - 10
        abrir = Animation(width = tamanho, opacity = 1, d = .1)
        abrir.start(widget)
    
    def fechar_menu(self, widget): 
        tamanho = Window.width - 10
        abrir = Animation(width = 0, opacity = 0, d = .1)
        abrir.start(widget)

class Keep(MDApp):
    def build(self):
        return MainHome()

app = Keep()
