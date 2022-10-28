from kivy.core.window import Window
from lib.MyApp import MyApp
from kivy.lang.builder import Builder

Window.size = (550,650)

Builder.load_file('media/content.kv')

if __name__ == '__main__':
    MyApp().run()