from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5 import QtCore
from const import FIELD_SIZE, SQUARE_SIZE
from classes.Square import Square
from classes.Checker import Checker
from typing import Tuple
import math


class Checkers(QWidget):
    def __init__(self):
        super().__init__()
        self.white_pawns = [Checker(1) for i in range(20)]
        self.black_pawns = [Checker(0) for i in range(20)]
        self.setAcceptDrops(True)
        self.setFixedWidth(FIELD_SIZE)
        self.setFixedHeight(FIELD_SIZE)
        layout = QGridLayout()
        self.board = [[Square(i, j, self) for i in range(10)] for j in range(10)]
        for i in range(10):
            for j in range(10):
                layout.addWidget(self[i, j], i, j)
        for i in range(4):
            for j in range(1, 10, 2):
                self.board[i][j - i % 2].checker = self.black_pawns[i * 5 + j // 2]
                self.black_pawns[i * 5 + j // 2].square = self.board[i][j - i % 2]
                self.board[6 + i][j - i % 2].checker = self.white_pawns[i * 5 + j // 2]
                self.white_pawns[i * 5 + j // 2].square = self.board[6 + i][j - i % 2]
        self.setLayout(layout)

    def __getitem__(self, key: Tuple[int, int]):
        return self.board[key[0]][key[1]]

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(QtCore.Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            square = self[math.ceil(event.pos().y() / SQUARE_SIZE) - 1, math.ceil(event.pos().x() / SQUARE_SIZE) - 1]
            last_pos = event.mimeData().text().split(',')
            last_pos = [int(elt) for elt in last_pos]
            print(f"{last_pos[1],last_pos[0]} -> {math.ceil(event.pos().y() / SQUARE_SIZE) - 1, math.ceil(event.pos().x() / SQUARE_SIZE) - 1}")
            square.checker = self[last_pos[1], last_pos[0]].checker
            print(square.checker)
            self[last_pos[1], last_pos[0]]._checker = None
            print(square.checker)
            square.checker.show()
            event.setDropAction(QtCore.Qt.MoveAction)
            event.accept()
        else:
            event.ignore()
