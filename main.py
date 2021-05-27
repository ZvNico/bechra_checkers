import sys
from classes.Application import Application
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    fen = Application()
    fen.show()
    app.exec_()
