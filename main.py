import sys
from classes.Application import Application
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    fen = Application()
    fen.showMaximized()
    app.exec_()
