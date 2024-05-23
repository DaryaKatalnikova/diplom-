import sys, MenuAdmin
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *

class WindowSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Академичсекая Школа Информационных Технологий")
        self.initUI()
        self.resize(QSize(300, 300))

    def initUI(self):
        self.labelSearch = QLabel('Поиск в базе данных \n выполняется по ..........', self)
        self.labelSearch.move(85, 20)
        self.labelSearch.resize(150, 60)
        self.textboxSearch = QLineEdit(self)
        self.textboxSearch.move(50, 80)
        self.textboxSearch.resize(200, 30)

        self.buttonSearch = QPushButton('Найти', self)
        self.buttonSearch.move(175, 250)
        #self.buttonSearch.clicked.connect(self.Search)

        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.move(50, 250)
        #self.buttonBack.clicked.connect(self.Back)

    # def Back(self):
    #     self.w = MenuAdmin.WindowMenuAdmin()
    #     self.w.show()
    #     self.close()
    #
    # def Search(self):
    #     # Поиск в БД
    #     self.w = MenuAdmin.WindowMenuAdmin()
    #     self.w.show()
    #     self.close()
