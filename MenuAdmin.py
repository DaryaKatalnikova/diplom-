import sys, Search, main, Delete
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *

import AbiturInputOne
import Delete
import Output


class WindowMenuAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Академическая Школа Информационных Технологий")
        self.initUI()
        self.resize(QSize(300, 300))

    def initUI(self):
        self.buttonSearch = QPushButton('Найти', self)
        self.buttonSearch.setFixedSize(300, 100)
        self.buttonSearch.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonSearch.clicked.connect(self.Search)

        self.buttonOutput = QPushButton('Вывести', self)
        self.buttonOutput.setFixedSize(300, 100)
        self.buttonOutput.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonOutput.clicked.connect(self.Output)

        self.buttonInput = QPushButton('Добавить', self)
        self.buttonInput.setFixedSize(300, 100)
        self.buttonInput.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonInput.clicked.connect(self.Input)

        self.buttonDelete = QPushButton('Удалить', self)
        self.buttonDelete.setFixedSize(300, 100)
        self.buttonDelete.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonDelete.clicked.connect(self.Delete)

        self.buttonExit = QPushButton('Выйти', self)
        self.buttonExit.setFixedSize(300, 100)
        self.buttonExit.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonExit.clicked.connect(self.Exit)



        hbox = QVBoxLayout()
        hbox.addWidget(self.buttonSearch, alignment=Qt.AlignmentFlag.AlignHCenter)
        hbox.addWidget(self.buttonOutput, alignment=Qt.AlignmentFlag.AlignHCenter)
        hbox.addWidget(self.buttonInput, alignment=Qt.AlignmentFlag.AlignHCenter)
        hbox.addWidget(self.buttonDelete, alignment=Qt.AlignmentFlag.AlignHCenter)
        hbox.addWidget(self.buttonExit, alignment=Qt.AlignmentFlag.AlignHCenter)

        vbox = QHBoxLayout()
        vbox.addLayout(hbox)

        #vbox.setContentsMargins(800, 50, 800, 50)
        self.setLayout(vbox)
        self.setGeometry(300, 50, 200, 50)

    def Output(self):
        self.w = Output.WindowOutput()
        self.w.showMaximized()
        self.close()

    def Input(self):
        self.w = AbiturInputOne.WindowInputOne()
        self.w.showMaximized()
        self.close()

    def Delete(self):
        self.w = Delete.WindowDelete()
        self.w.showMaximized()
        self.close()

    def Search(self):
        self.w = Search.WindowSearch()
        self.w.showMaximized()
        self.close()

    def Exit(self):
        self.w = main.WindowMain()
        self.w.showMaximized()
        self.close()


