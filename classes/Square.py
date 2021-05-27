from const import SQUARE_SIZE
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
import math


class Square(QLabel):
    def __init__(self, row, col, parent, checker=None):
        super().__init__(parent)
        color = self.palette()
        self.setStyleSheet('QLabel {background-color: #112233;}')
        self.setFixedWidth(SQUARE_SIZE)
        self.setFixedHeight(SQUARE_SIZE)

        self.x = row * SQUARE_SIZE
        self.y = col * SQUARE_SIZE
        self.row = row
        self.col = col
        self.checker = checker
        self.show()

    def get_pos(self):
        return self.x, self.y

    def is_playable(self):
        return (self.row + self.col) % 2 != 0
