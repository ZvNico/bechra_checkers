from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QWidget, QGridLayout
from PyQt5 import QtGui
from const import FIELD_SIZE
from classes.Square import Square
from classes.Checker import Checker
from classes.Checkers import Checkers


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('assets/logo.png'))
        self.setWindowTitle("Jeu de dames ESME Sudria")
        self.init_menu()
        self.boards = []
        self.central_widget = QWidget()
        self.checkers = Checkers()
        layout = QGridLayout()
        layout.addWidget(self.checkers, 0, 0)
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    def init_menu(self):
        """initialisation du menu"""
        self.menu = self.menuBar()
        self.submenu = {
            "file": QMenu("&Fichier", self),
            "help": QMenu("&Aide", self),
            "history": QMenu("&Historique", self
                             )}

        for value in self.submenu.values():
            self.menu.addMenu(value)

        self.menu_action = {
            "file": {"new_game": QAction("Sauvegarder la Partie", self),
                     "load_game": QAction("&Charger une Partie", self),
                     "save_game": QAction("&Sauvegarder la Partie", self)},

            "help": {"manuel": QAction("&Manuel", self),
                     "propos": QAction("&A propos", self)},

            "history": {"toggle_display  ": QAction("&Afficher chaque deplacement lorsqu'il est effectué", self),
                        "display": QAction("&Afficher l'historique des déplacements de la partie en cours", self),
                        "load": QAction("&Afficher  l'historique des  déplacements d'une  partie  précédente", self),
                        "save": QAction("&Sauvegarder l'historique des déplacements", self)}
        }

        for key in self.menu_action:
            for value in self.menu_action[key].values():
                self.submenu[key].addAction(value)
