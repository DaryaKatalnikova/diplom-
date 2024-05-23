import sys, main, AbiturInputTwo, onDataBase, End
from datetime import date, datetime

from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from mysql.connector import Error

import AbiturInputOne
import Output

connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")



class WindowRedactOne(QWidget):
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
                        color: #000000;
                    }
                    QLineEdit{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        background-color: #FFFFFF;
                        color: #000000;
                    }
                    QComboBox QListView::item{
                        padding-left: 10px;
                    }
                    QComboBox QListView::item:hover{
                        padding-left: 10px;
                        background-color: #14365B;
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
                    QCheckBox{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        color: #000000;
                    }
                    QTableWidget{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        background-color: #FFFFFF;
                        color: #000000;
                    }
                    QHeaderView::section{
                        font-family: Ubuntu Mono;
                        font-size: 13px;
                        background-color: #FFFFFF;
                        color: #000000;
                        }
                    QRadioButton{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        color: #000000;
                    } 
                    QDateEdit{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        color: #000000;
                    }
                ''')
        self.initUI()
        self.pixmap = QPixmap('3.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

    def initUI(self):
        f = open('proverka.txt', 'r')
        if (f != ''):
            id_st = int(f.read())
        else:
            print("ошибка")
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        self.labelNameBlank = QLabel('Бланк для абитуриента\n'
                                     '   основыне данные', self)
        self.labelNameBlank.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelSecondName = QLabel('Фамилия', self)
        self.labelSecondName.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelSecondName.setFixedSize(400, 100)
        self.textboxSecondName = QLineEdit(self)
        self.textboxSecondName.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxSecondName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-' ']+")))
        cursor = connection.cursor()
        postgresql_select_query = "select secondname from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxSecondName.setText(c)


        self.labelName = QLabel('Имя', self)
        self.labelName.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelName.setFixedSize(400, 100)
        self.textboxName = QLineEdit(self)
        self.textboxName.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select namee from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxName.setText(c)
        self.textboxName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-' ']+")))

        self.labelMiddleName = QLabel('Отчество', self)
        self.labelMiddleName.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelMiddleName.setFixedSize(400, 100)
        self.textboxMiddleName = QLineEdit(self)
        self.textboxMiddleName.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select midlename from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxMiddleName.setText(c)
        self.textboxMiddleName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-' ']+")))

        self.labelHB = QLabel('Укажите свою \nдату рождения', self)
        self.labelHB.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelHB.setFixedSize(400, 100)
        self.date = QDateEdit(self)
        self.date.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select datehb from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = d[0]
        self.date.setDate(c)

        self.labelPhone = QLabel('Введите ваш \nномер телефона', self)
        self.labelPhone.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPhone.setFixedSize(400, 100)
        self.textboxPhone = QLineEdit(self)
        self.textboxPhone.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select numberphone from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxPhone.setText(c)
        self.textboxPhone.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+")))
        self.textboxPhone.setMaxLength(11)

        self.labelEmail = QLabel('Введите ваш Email', self)
        self.labelEmail.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelEmail.setFixedSize(400, 100)
        self.textboxEmail = QLineEdit(self)
        self.textboxEmail.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select email from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxEmail.setText(c)

        self.buttonBack = QPushButton('Отмена', self)
        self.buttonBack.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonBack.setFixedSize(250, 50)
        self.buttonBack.clicked.connect(self.Back)

        self.buttonNext = QPushButton('Изменить', self)
        self.buttonNext.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonNext.setFixedSize(250, 50)
        self.buttonNext.clicked.connect(self.Acept)



        layout = QGridLayout()

        layout.addWidget(self.labelNameBlank, 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setRowStretch(0, 1)
        layout.addWidget(self.labelSecondName, 1, 0, 2, 1)
        layout.addWidget(self.textboxSecondName, 1, 1, 2, 1)
        layout.setRowStretch(1, 1)
        layout.addWidget(self.labelName, 2, 0, 2, 1)
        layout.addWidget(self.textboxName, 2, 1, 2, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.addWidget(self.labelMiddleName, 3, 0, 2, 1)
        layout.addWidget(self.textboxMiddleName, 3, 1, 2, 1)
        layout.setRowStretch(3, 1)
        layout.addWidget(self.labelHB, 4, 0, 2, 1)
        layout.addWidget(self.date, 4, 1, 2, 1)
        layout.setRowStretch(4, 1)
        layout.addWidget(self.buttonBack, 8, 0, 2, 1)
        layout.addWidget(self.labelPhone, 5, 0, 2, 1)
        layout.addWidget(self.textboxPhone, 5, 1, 2, 1)
        layout.setRowStretch(5, 1)
        layout.addWidget(self.labelEmail, 6, 0, 2, 1)
        layout.addWidget(self.textboxEmail, 6, 1, 2, 1)
        layout.setRowStretch(6, 1)
        layout.addWidget(self.buttonNext, 8, 3, 2, 1)
        layout.setRowStretch(7, 1)
        self.setLayout(layout)

    def Acept(self):
        f = open('proverka.txt', 'r')
        if (f != ''):
            id_st = int(f.read())
        else:
            print("ошибка")
        lineEdits = self.findChildren(QLineEdit)
        text = ''
        for lineEdit in lineEdits:
            if not lineEdit.text():
                text = f'Заполните все поля!\n'
        if text:
            msg = QMessageBox.information(self, 'Внимание', text)
        else:
            connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
            cursor = connection.cursor()
            yearB = int(self.date.date().toString("yyyy.MM.dd").split('.')[0])
            monthB = int(self.date.date().toString("yyyy.MM.dd").split('.')[1])
            dayB = int(self.date.date().toString("yyyy.MM.dd").split('.')[2])
            familia = " ".join(self.textboxSecondName.text().split()).title()
            imya = " ".join(self.textboxName.text().split()).title()
            otchestvo = " ".join(self.textboxMiddleName.text().split()).title()
            numberphone = " ".join(self.textboxPhone.text().split()).title()
            email = " ".join(self.textboxEmail.text().split()).title()
            birthday = date(yearB, monthB, dayB)
            zapis = (birthday, familia, imya, otchestvo, numberphone, email, id_st)
            newRow = "UPDATE student SET datehb = %s, secondname = %s, namee = %s, midlename = %s, numberphone = %s, email = %s where id_student = %s"

            cursor.execute(newRow, zapis)
            connection.commit()
            connection.close()
            self.Next()

    def Next(self):
        f = open('proverka1.txt', 'r', encoding='utf-8')
        tex = f.read()
        if (tex == 'АДМИН'):
            self.w = Output.WindowOutput()
            self.w.showMaximized()
            self.close()
        else:
            self.w = End.WindowEnd()
            self.w.showMaximized()
            self.close()

    def Back(self):
        self.w = End.WindowEnd()
        self.w.showMaximized()
        self.close()

