from kivy.app import App
from lib.Analyst import Analyst
from lib.Incrementer import Incrementer
import webbrowser

class MyApp(App,Analyst):

    def build(self):
        self.setLayout(Incrementer())
        self.verifyActive()

        return self.layout

    def openPMA(self):
        webbrowser.open('http://localhost/dumbby/index.php')

    def openLocalhost(self):
        webbrowser.open('http://localhost')