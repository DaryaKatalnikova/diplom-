from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *

import RedactFour
import RedactOne
import RedactThree
import RedactTwo
from app.modules import onDataBase


class WindowRedact(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Академическая Школа Информационных Технологий")
        self.setStyleSheet('''
            QWidget{
                background-color: #d1d1d1;
                color: #D9D9D9;
            }
            QLabel{
                font-family: Ubuntu Mono;
                font-size: 18px;
                color: #D9D9D9;
            }
            QPixmap{
                width: 400px; 
                height: 400px;
                color: #D9D9D9;
            }
            QPushButton{
                font-size: 14px;
                font-family: Ubuntu Mono;
                color: #FFFFFF;
                background-color: #3657ff;
                border-radius: 15px;
            }
            QPushButton:hover{
                background-color: #002bff;
            }
        ''')
        self.initUI()
        self.setFixedSize(QSize(750, 550))

    def initUI(self):

        self.buttonRedOsn = QPushButton('Изменить основыне\nданные студента', self)
        self.buttonRedOsn.move(50, 50)
        self.buttonRedOsn.resize(300, 100)
        self.buttonRedOsn.clicked.connect(self.RedOsnSt)
        self.buttonRedOsn.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonRedPas = QPushButton('Изменить паспортные\nданные студента', self)
        self.buttonRedPas.move(50, 175)
        self.buttonRedPas.resize(300, 100)
        self.buttonRedPas.clicked.connect(self.RedPasSt)
        self.buttonRedPas.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonRedSch = QPushButton('Изменить данные\nо школе студента', self)
        self.buttonRedSch.move(50, 300)
        self.buttonRedSch.resize(300, 100)
        self.buttonRedSch.clicked.connect(self.RedSchSt)
        self.buttonRedSch.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonRedOsnRod = QPushButton('Изменить основные\nданные родителя', self)
        self.buttonRedOsnRod.move(400, 50)
        self.buttonRedOsnRod.resize(300, 100)
        self.buttonRedOsnRod.clicked.connect(self.RedOsnRod)
        self.buttonRedOsnRod.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonRedPasRod = QPushButton('Изменить паспортные\nданные родителя', self)
        self.buttonRedPasRod.move(400, 175)
        self.buttonRedPasRod.resize(300, 100)
        self.buttonRedPasRod.clicked.connect(self.RedPasRod)
        self.buttonRedPasRod.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonDel = QPushButton('Удалит все данные\nо студенте', self)
        self.buttonDel.move(400, 300)
        self.buttonDel.resize(300, 100)
        self.buttonDel.clicked.connect(self.Del)
        self.buttonDel.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.move(225, 425)
        self.buttonBack.resize(300, 100)
        self.buttonBack.clicked.connect(self.Back)
        self.buttonBack.setStyleSheet(
            "font-size: 25px;"
        )

    def Back(self):
        self.close()

    def RedPasSt(self):
        file = open("../static/proverka1.txt", "w", encoding='utf-8')
        file.write("АДМИН")
        self.w = RedactTwo.WindowRedactTwo()
        self.w.showMaximized()
        self.close()

    def RedOsnSt(self):
        file = open("../static/proverka1.txt", "w", encoding='utf-8')
        file.write("АДМИН")
        self.w = RedactOne.WindowRedactOne()
        self.w.showMaximized()
        self.close()

    def RedSchSt(self):
        file = open("../static/proverka1.txt", "w", encoding='utf-8')
        file.write("АДМИН")
        self.w = RedactThree.WindowRedactThree()
        self.w.showMaximized()
        self.close()

    def RedOsnRod(self):
        file = open("../static/proverka1.txt", "w", encoding='utf-8')
        file.write("АДМИН")
        self.w = RedactFour.WindowRedactFour()
        self.w.showMaximized()
        self.close()

    def RedPasRod(self):
        file = open("../static/proverka1.txt", "w", encoding='utf-8')
        file.write("АДМИН")
        self.w = RedactFour.WindowRedactFour()
        self.w.showMaximized()
        self.close()

    def Del(self):
        # msgBox = QMessageBox()
        # msgBox.setText("The document has been modified.")
        # msgBox.setInformativeText("Do you want to save your changes?")
        # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        # msgBox.setDefaultButton(QMessageBox.Save)
        # ret = msgBox.exec()
        f = open('../static/proverka.txt', 'r')
        if (f != ''):
            id_st = int(f.read())
        else:
            print("ошибка")
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        delet = "DELETE FROM student where id_student = '%d'" % (id_st)
        with connection.cursor() as cursor:
            cursor.execute(delet)
            connection.commit()
            self.close()