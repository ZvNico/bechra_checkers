from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QWidget, QGridLayout, QFileDialog, QMessageBox
from PyQt5 import QtGui
from classes.Checkers import Checkers
import pickle


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('assets/logo.png'))
        self.setWindowTitle("Jeu de dames ESME Sudria")
        self.init_menu()
        self.central_widget = QWidget()
        self.checkers = []
        self._atual_checkers = -1
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)
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
            "file": {"new_game": QAction("Nouvelle Partie", self),
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

        self.menu_action["file"]["new_game"].triggered.connect(self.new_game)
        self.menu_action["file"]["save_game"].triggered.connect(self.save_game)
        self.menu_action["file"]["load_game"].triggered.connect(self.load_game)

        self.menu_action["help"]["propos"].triggered.connect(self.propos)

    @property
    def actual_checkers(self):
        return self._atual_checkers

    @actual_checkers.setter
    def actual_checkers(self, i):
        if self._atual_checkers != -1:
            self.checkers[self._atual_checkers].hide()
        self._actual_checkers = i
        self.layout.addWidget(self.checkers[self.actual_checkers], 0, 0)
        self.checkers[self._atual_checkers].show()

    def new_game(self, checker=Checkers()):
        self.checkers.append(checker)
        self.actual_checkers = len(self.checkers) - 1

    def load_game(self):
        filename = QFileDialog().getOpenFileName(self, 'Pickle File', 'saves/games/')
        if filename[0]:
            with open(filename[0], 'rb') as f:
                # enfait pickle ne fonctionne pas avec cette classe, l'idée était là
                self.new_game(pickle.load(f))

    def save_game(self):
        filename = QFileDialog().getSaveFileName(self, 'Pickle File', 'saves/games/')
        if filename[0]:
            with open(filename[0], 'wb+') as f:
                # enfait pickle ne fonctionne pas avec cette classe, l'idée était là
                pickle.dump(self.checkers[self.actual_checkers], f)

    def propos(self):
        msg_box = QMessageBox()
        msg_box.setText(
            "Ce projet a ete realise par Bechraoui Alexandre et Pereira-Fereira Alex.\nLe but du projet est de creer un jeu de dames en ligne. On peut y jouer de deux manieres differentes : - soit contre un bot (ordinateur) - soit a 2.\nOn peut reprendre une partie qu'on a commencé à l'aide sauvegarder ou meme jouer plusieures parties en simultané.\nBref, laissez vous tenter par le jeu de dames version amélioré !")
        msg_box.setWindowTitle("A propos")
        msg_box.exec_()

