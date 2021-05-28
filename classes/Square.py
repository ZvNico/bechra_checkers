from const import SQUARE_SIZE
from PyQt5.QtWidgets import QLabel, QGridLayout


class Square(QLabel):
    def __init__(self, row, col, checkers, checker=None):
        super().__init__(checkers)
        if ((row + col % 2) % 2):
            self.setStyleSheet('QLabel {background-color: #9f4e0f;}')
        else:
            self.setStyleSheet('QLabel {background-color: #fbe889;}')
        self.setFixedWidth(SQUARE_SIZE)
        self.setFixedHeight(SQUARE_SIZE)
        self.checkers = checkers
        self.x = row * SQUARE_SIZE
        self.y = col * SQUARE_SIZE
        self.row = row
        self.col = col
        self._checker = None
        if checker:
            self.checker = checker

        self.layout = QGridLayout()
        self.setLayout(self.layout)

    @property
    def checker(self):
        return self._checker

    @checker.setter
    def checker(self, checker):
        self._checker = checker
        if checker:
            self.layout.addWidget(checker, 0, 0)
            self.checker.show()

    def get_pos(self):
        return self.row, self.col

    def is_playable(self):
        return (self.row + self.col) % 2 != 0
