import sys, MenuAdmin
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *

class WindowSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Академичсекая Школа Информационных Технологий")
        self.initUI()
        self.resize(QSize(700, 500))

    def initUI(self):
        self.labelSearch = QLabel('        Поиск в базе данных \nвыполняется по ФИО студента', self)
        self.labelSearch.move(150, 20)
        self.labelSearch.resize(400, 80)
        self.labelSearch.setStyleSheet(
            "font-size: 25px;"
        )

        self.labelName = QLabel('Имя:', self)
        self.labelName.move(20, 100)
        self.labelName.resize(70, 60)
        self.labelName.setStyleSheet(
            "font-size: 25px;"
        )

        self.textboxSearchName = QLineEdit(self)
        self.textboxSearchName.move(170, 115)
        self.textboxSearchName.resize(300, 30)
        self.textboxSearchName.setStyleSheet(
            "font-size: 25px;"
        )

        self.labelSearchSecondName = QLabel('Фамилия:', self)
        self.labelSearchSecondName.move(20, 160)
        self.labelSearchSecondName.resize(150, 60)
        self.labelSearchSecondName.setStyleSheet(
            "font-size: 25px;"
        )
        self.textboxSearchSecondName = QLineEdit(self)
        self.textboxSearchSecondName.move(170, 175)
        self.textboxSearchSecondName.resize(300, 30)
        self.textboxSearchSecondName.setStyleSheet(
            "font-size: 25px;"
        )

        self.labelSearchMiddleName = QLabel('Отчество:', self)
        self.labelSearchMiddleName.move(20, 220)
        self.labelSearchMiddleName.resize(150, 60)
        self.labelSearchMiddleName.setStyleSheet(
            "font-size: 25px;"
        )
        self.textboxSearchMiddleName = QLineEdit(self)
        self.textboxSearchMiddleName.move(170, 235)
        self.textboxSearchMiddleName.resize(300, 30)
        self.textboxSearchMiddleName.setStyleSheet(
            "font-size: 25px;"
        )


        self.buttonSearch = QPushButton('Найти', self)
        self.buttonSearch.move(500, 400)
        self.buttonSearch.resize(150, 50)
        self.buttonSearch.clicked.connect(self.Search)
        self.buttonSearch.setStyleSheet(
            "font-size: 25px;"
        )

        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.move(50, 400)
        self.buttonBack.resize(150, 50)
        self.buttonBack.clicked.connect(self.Back)
        self.buttonBack.setStyleSheet(
            "font-size: 25px;"
        )

    def Back(self):
        self.w = MenuAdmin.WindowMenuAdmin()
        self.w.showMaximized()
        self.close()

    def Search(self):
        # Поиск в БД
        self.w = MenuAdmin.WindowMenuAdmin()
        self.w.show()
        self.close()
