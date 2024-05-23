import sys, AbiturInputThree, OpekunBlank, onDataBase
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *
from mysql.connector import Error

import AbiturInputOne

connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

selectST = "SELECT * FROM student"
centers = execute_read_query(connection, selectST)
if centers ==[]:
    id_rd = 1
else:
    id_rd = centers[len(centers)-1][0]
    id_rd += 1

class WindowOpekunBlankTwo(QWidget):
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
        self.textboxName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-' ']+")))

        self.labelSecondName = QLabel('Имя', self)
        self.labelSecondName.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelSecondName.setFixedSize(400, 100)
        self.textboxSecondName = QLineEdit(self)
        self.textboxSecondName.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxSecondName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-' ']+")))

        self.labelMidleName = QLabel('Отчество', self)
        self.labelMidleName.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelMidleName.setFixedSize(400, 100)
        self.textboxMidleName = QLineEdit(self)
        self.textboxMidleName.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxMidleName.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-' ']+")))

        self.labelNumberPhone = QLabel('Номер телефона', self)
        self.labelNumberPhone.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelNumberPhone.setFixedSize(400, 100)
        self.textboxPhone = QLineEdit(self)
        self.textboxPhone.setStyleSheet(
            "font-size: 20px;"
        )
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

        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonBack.setFixedSize(250, 50)
        self.buttonBack.clicked.connect(self.Back)


        self.buttonNext = QPushButton('Вперед', self)
        self.buttonNext.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonNext.setFixedSize(250, 50)
        self.buttonNext.clicked.connect(self.Acept)

        self.labelStep = QLabel('Шаг 1 из 2', self)
        self.labelStep.setStyleSheet(
            "font-size: 20px;"
        )

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
        layout.addWidget(self.labelStep, 8, 1, 2, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
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
            zapis = (id_rd, familia, imya, otchestvo, numberphone, email,  id_st)
            newRow = "INSERT INTO roditel (id_roditel, secondname, namee, midlename, numberphone, email, id_student) values (%s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(newRow, zapis)
            connection.commit()
            connection.close()
            self.Next()


    def Next(self):
        self.w = OpekunBlank.WindowOpekunBlank()
        self.w.showMaximized()
        self.close()

    def Back(self):
        self.w = AbiturInputThree.WindowInputThree()
        self.w.showMaximized()
        self.close()