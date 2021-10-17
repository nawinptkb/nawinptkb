from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class UI(QMainWindow):
        def __init__(self):
                super(UI,self).__init__()

        #Load the ui file
        uic.loadUi("Pyqt_calculator.ui", self)