from PyQt5.QtWidgets import QLabel
from const import SQUARE_SIZE

class Checker(QLabel):
    def __init__(self, color):
        super().__init__()
        self.color = color