from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu, QAction, QWidget
from PyQt5 import QtGui
from const import FIELD_SIZE
from classes.Square import Square
from classes.Checker import Checker
from typing import Tuple


class Checkers(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('assets/logo.png'))
        self.setWindowTitle("Jeu de dames ESME Sudria")
        self.setFixedWidth(FIELD_SIZE)
        self.setFixedHeight(FIELD_SIZE)
        self.init_menu()
        self.board = [[Square(i, j, self) for i in range(10)] for j in range(10)]

        for i in range(4):
            for j in range(1, 10, 2):
                self.board[i][j - i % 2].checker = Checker("B")
                self.board[6 + i][j - i % 2].checker = Checker("W")

    def __getitem__(self, key: Tuple[int, int]):
        return self.board[key[0]][key[1]]
