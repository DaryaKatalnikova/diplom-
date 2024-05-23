import sys, AbiturInputThree, OpekunBlank, onDataBase, End, AbiturInputOne
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *
from mysql.connector import Error

import OpekunBlankTwo
import Output

connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")



class WindowRedactFour(QWidget):
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
        self.resize(QSize(500, 400))
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
        self.labelNameBlank = QLabel('Бланк для законного представителя\n'
                                     '         основыне данные', self)
        self.labelNameBlank.setStyleSheet(
            "font-size: 20px;"
        )

        self.labelName = QLabel('Фамилия', self)
        self.labelName.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelName.setFixedSize(400, 100)
        self.textboxName = QLineEdit(self)
        self.textboxName.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select midlename from roditel where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxName.setText(c)
        self.textboxName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-]+")))

        self.labelSecondName = QLabel('Имя', self)
        self.labelSecondName.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelSecondName.setFixedSize(400, 100)
        self.textboxSecondName = QLineEdit(self)
        self.textboxSecondName.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select namee from roditel where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxSecondName.setText(c)
        self.textboxSecondName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-]+")))

        self.labelMidleName = QLabel('Отчество', self)
        self.labelMidleName.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelMidleName.setFixedSize(400, 100)
        self.textboxMidleName = QLineEdit(self)
        self.textboxMidleName.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select midlename from roditel where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxMidleName.setText(c)
        self.textboxMidleName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-]+")))

        self.labelNumberPhone = QLabel('Номер телефона', self)
        self.labelNumberPhone.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelNumberPhone.setFixedSize(400, 100)
        self.textboxPhone = QLineEdit(self)
        self.textboxPhone.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select numberphone from roditel where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxPhone.setText(c)
        self.textboxPhone.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+")))
        self.textboxPhone.setMaxLength(11)

        self.labelEmail = QLabel('Укажите ваш Email', self)
        self.labelEmail.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelEmail.setFixedSize(400, 100)
        self.textboxEmail = QLineEdit(self)
        self.textboxEmail.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select email from roditel where id_student = %s"
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
        layout.addWidget(self.labelNumberPhone, 1, 0, 2, 1)
        layout.addWidget(self.textboxPhone, 1, 1, 2, 1)
        layout.addWidget(self.labelEmail, 2, 0, 2, 1)
        layout.addWidget(self.textboxEmail, 2, 1, 2, 1)
        layout.setRowStretch(1, 1)
        layout.addWidget(self.labelName, 3, 0, 2, 1)
        layout.addWidget(self.textboxName, 3, 1, 2, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.addWidget(self.labelSecondName, 4, 0, 2, 1)
        layout.addWidget(self.textboxSecondName, 4, 1, 2, 1)
        layout.setRowStretch(3, 1)
        layout.addWidget(self.labelMidleName, 5, 0, 2, 1)
        layout.addWidget(self.textboxMidleName, 5, 1, 2, 1)
        layout.setRowStretch(4, 1)
        layout.addWidget(self.buttonBack, 8, 0, 2, 1)
        layout.setRowStretch(5, 1)
        layout.addWidget(self.buttonNext, 8, 3, 2, 1)
        layout.setRowStretch(7, 1)
        layout.setRowStretch(6, 1)
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
            familia = " ".join(self.textboxSecondName.text().split()).title()
            imya = " ".join(self.textboxName.text().split()).title()
            otchestvo = " ".join(self.textboxMidleName.text().split()).title()
            numberphone = " ".join(self.textboxPhone.text().split()).title()
            email = " ".join(self.textboxEmail.text().split()).title()
            zapis = (familia, imya, otchestvo, numberphone, email, id_st, OpekunBlankTwo.id_rd)
            newRow = "UPDATE roditel SET secondname = %s, namee = %s, midlename = %s, numberphone = %s, email = %s where id_student = %s and id_roditel = %s"
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