from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDrag, QPixmap, QPainter
from const import SQUARE_SIZE, CHECKER_SQUARE_RATIO


class Checker(QLabel):
    def __init__(self, color, square=None, is_queen=False):
        super().__init__()
        self.square = square
        self.is_queen = is_queen
        self.setFixedWidth(SQUARE_SIZE * CHECKER_SQUARE_RATIO)
        self.setFixedHeight(SQUARE_SIZE * CHECKER_SQUARE_RATIO)
        stylesheet = "QLabel { border-radius: " + str(SQUARE_SIZE * CHECKER_SQUARE_RATIO / 2) + "px; background-color: "
        if color:
            stylesheet += "#fff }"
        else:
            stylesheet += "#000 }"

        self.setStyleSheet(stylesheet)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = self.square

    def mouseMoveEvent(self, event):
        '''if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return'''
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(f"{self.square.row},{self.square.col}")
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
