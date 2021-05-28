from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
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
        self.checker_on_prise = -1
        self.checker_on_delete = []
        self.historique = []
        self.tour = 1
        self.log = False
        self.widgets = {
            "tour": QLabel(f"Tour n°{self.tour}")
        }
        self.setAcceptDrops(True)
        self.setFixedWidth(FIELD_SIZE)
        self.setFixedHeight(FIELD_SIZE)
        layout = QGridLayout()
        self.board = [[Square(i, j, self) for j in range(10)] for i in range(10)]
        for i in range(10):
            for j in range(10):
                layout.addWidget(self[i, j], i, j)
        for i in range(4):
            for j in range(1, 10, 2):
                self[i, j - i % 2].checker = self.black_pawns[i * 5 + j // 2]
                self.black_pawns[i * 5 + j // 2].square = self[i, j - i % 2]
                self[6 + i, j - i % 2].checker = self.white_pawns[i * 5 + j // 2]
                self.white_pawns[i * 5 + j // 2].square = self[6 + i, j - i % 2]
        self.setLayout(layout)
        self.find_moves()

    def __getitem__(self, key: Tuple[int, int]):
        if key[0] < 10 and key[0] > -1 and key[1] < 10 and key[1] > -1:
            return self.board[key[0]][key[1]]
        else:
            return False

    def find_moves(self):
        self.moves = []
        if self.checker_on_prise == -1:
            moves = [self.get_move(i) for i in range(len(self.white_pawns) if self.tour % 2 else len(self.black_pawns))]
            max = 2
            for elt in moves[1:]:
                if len(elt) == 4:
                    max = 4
                    self.checker_on_prise = True
                    break
            for elt in moves:
                for move in elt:
                    self.moves.append(move)
        else:
            return self.get_move(self.checker_on_prise)

    def get_move(self, i):
        """def cheminement(direction_initial, j):
            while i_s[direction_initial][j][1] != -1:
                yield moves[direction_initial][j]
                j = i_s[direction_initial][j][1]"""

        pawn = self.white_pawns[i] if self.tour % 2 else self.black_pawns[i]
        pos = pawn.square.get_pos()
        directions = ((-1, -1), (1, -1), (-1, 1), (1, 1))
        moves = [None for i in range(4)]
        queue = []
        # if not pawn.is_queen:
        for j in range(4):
            square = self[pos[0] + directions[j][0], pos[1] + directions[j][1]]
            if square:
                if square.checker and not square.checker == pawn:
                    queue.append(((pos[0] + directions[j][0], pos[1] + directions[j][1]), j, j))

        while queue:
            elt = queue.pop(0)
            direction_initial = elt[2]
            direction = elt[1]
            pos = elt[0]
            square = self[pos[0] + directions[direction][0], pos[1] + directions[direction][1]]
            if square:
                if None == square.checker:
                    moves[direction_initial] = square.get_pos()
                """pos = square.get_pos()
                    print("on est a ", pos)
                    for j in range(4):
                        square = self[pos[0] + directions[j][0], pos[1] + directions[j][1]]
                    if square:
                        print("vérification case suivant")
                        print(square.get_pos())
                        for elt in cheminement(direction_initial, prev_i):
                            print(elt, end=", ")
                        print()
                    if not square.checker == pawn and square.checker and square.get_pos() not in cheminement(direction_initial, prev_i):
                        queue.append((square.get_pos(), j, prev_i, direction_initial))"""
        for elt in moves:
            if elt:
                return moves

        # aucune prise
        moves = [None for i in range(2)]
        direction = -1 if self.tour % 2 else 1
        squares = [self[pos[0] + direction, pos[1] - 1], self[pos[0] + direction, pos[1] + 1]]
        for i, square in enumerate(squares):
            if square:
                if None == square.checker:
                    moves[i] = square.get_pos()
        return moves

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
            last_pos = tuple([int(last_pos[0][1:]), int(last_pos[1][:-1].replace(' ', ''))])
            print(last_pos, "->", square.get_pos())
            if square.is_playable() and not square.checker:
                if square.get_pos() in self.moves:
                    offset = (abs(last_pos[0] - square.row), abs(last_pos[1] - square.col))
                    if offset[0] == -2 or offset[0] == 2:
                        last_pos
                    self[last_pos].checker.move(square)
                    if self.checker_on_prise == -1:
                        self.tour += 1
                    self.find_moves()
            else:
                self[last_pos].checker.show()

            event.setDropAction(QtCore.Qt.MoveAction)
            event.accept()
        else:
            event.ignore()
