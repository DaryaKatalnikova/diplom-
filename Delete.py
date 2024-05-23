import sys, MenuAdmin
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *

class WindowDelete(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Академичсекая Школа Информационных Технологий")
        self.initUI()
        self.resize(QSize(700, 500))

    def initUI(self):
        self.labelDelete = QLabel('Поиск в базе данных, для дальнейшего удаления \n               выполняется по ФИО студента', self)
        self.labelDelete.move(75, 20)
        self.labelDelete.resize(570, 80)
        self.labelDelete.setStyleSheet(
            "font-size: 25px;"
        )

        self.labelName = QLabel('Имя:', self)
        self.labelName.move(20, 100)
        self.labelName.resize(70, 60)
        self.labelName.setStyleSheet(
            "font-size: 25px;"
        )

        self.textboxName = QLineEdit(self)
        self.textboxName.move(170, 115)
        self.textboxName.resize(300, 30)
        self.textboxName.setStyleSheet(
            "font-size: 25px;"
        )

        self.labelSecondName = QLabel('Фамилия:', self)
        self.labelSecondName.move(20, 160)
        self.labelSecondName.resize(150, 60)
        self.labelSecondName.setStyleSheet(
            "font-size: 25px;"
        )
        self.textboxSecondName = QLineEdit(self)
        self.textboxSecondName.move(170, 175)
        self.textboxSecondName.resize(300, 30)
        self.textboxSecondName.setStyleSheet(
            "font-size: 25px;"
        )

        self.labelMiddleName = QLabel('Отчество:', self)
        self.labelMiddleName.move(20, 220)
        self.labelMiddleName.resize(150, 60)
        self.labelMiddleName.setStyleSheet(
            "font-size: 25px;"
        )
        self.textboxMiddleName = QLineEdit(self)
        self.textboxMiddleName.move(170, 235)
        self.textboxMiddleName.resize(300, 30)
        self.textboxMiddleName.setStyleSheet(
            "font-size: 25px;"
        )

        self.buttonDelete = QPushButton('Найти', self)
        self.buttonDelete.move(500, 400)
        self.buttonDelete.resize(150, 50)
        self.buttonDelete.clicked.connect(self.Delet)
        self.buttonDelete.setStyleSheet(
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

    def Delet(self):
        # Поиск в БД и удаление
        self.w = MenuAdmin.WindowMenuAdmin()
        self.w.show()
        self.close()