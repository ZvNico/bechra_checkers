from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QFont
from const import SQUARE_SIZE, CHECKER_SQUARE_RATIO


class Checker(QLabel):
    def __init__(self, color):
        super().__init__()
        self.square = None
        self._is_queen = False
        self.setFixedWidth(SQUARE_SIZE * CHECKER_SQUARE_RATIO)
        self.setFixedHeight(SQUARE_SIZE * CHECKER_SQUARE_RATIO)
        stylesheet = "QLabel { box-shadow: 5px 5px grey ; border-radius: " + str(SQUARE_SIZE * CHECKER_SQUARE_RATIO / 2) + "px; background-color: %s; color: %s;}"
        if color:
            stylesheet = stylesheet % ("#fff", "#000")
        else:
            stylesheet = stylesheet % ("#000", "#fff")
        self.color = color
        self.setStyleSheet(stylesheet)
        self.setFont(QFont('Arial', 15))
        self.setAlignment(Qt.AlignCenter)

    @property
    def is_queen(self):
        return self._is_queen

    @is_queen.setter
    def is_queen(self, is_queen):
        self._is_queen = is_queen
        self.setText("D")

    def __eq__(self, other):
        return self.color == other

    def move(self, square):
        self.square.checker = None
        self.square = square
        self.square.checker = self

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = self.square

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if not ((self.color and self.square.checkers.tour % 2) or (not self.color and not self.square.checkers.tour % 2)):
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(f"{self.square.get_pos()}")
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        # rendre rond
        # painter.drawRoundedRect(pixmap.rect(), SQUARE_SIZE * CHECKER_SQUARE_RATIO / 2, SQUARE_SIZE * CHECKER_SQUARE_RATIO / 2)
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        self.hide()
        drag.exec_(Qt.CopyAction | Qt.MoveAction)
