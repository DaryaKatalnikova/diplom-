import OpekunBlankTwo, onDataBase
from app.modules import End
from datetime import date

from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *

from mysql.connector import Error

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


class WindowOpekunBlank(QWidget):
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
        self.pixmap = QPixmap('3.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

    def initUI(self):
        f = open('../static/proverka.txt', 'r')
        if (f != ''):
            id_st = int(f.read())
        else:
            print("ошибка")
        self.labelNameBlank = QLabel('Бланк для законного представителя\n'
                                     '        паспортные данные', self)
        self.labelNameBlank.setStyleSheet(
            "font-size: 20px;"
        )

        self.labelPasport = QLabel('Серия паспорта и \nномер паспорта', self)
        self.labelPasport.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPasport.setFixedSize(400, 100)
        self.textboxPasport = QLineEdit(self)
        self.textboxPasport.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxPasport.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+")))
        self.textboxPasport.setMaxLength(10)

        self.labelPasport1 = QLabel('Кем выдан', self)
        self.labelPasport1.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPasport1.setFixedSize(400, 100)
        self.textboxPasport1 = QLineEdit(self)
        self.textboxPasport1.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxPasport1.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-' ']+")))

        self.labelPasport2 = QLabel('Когда выдан', self)
        self.labelPasport2.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPasport2.setFixedSize(400, 100)
        self.date = QDateEdit(self)
        self.date.setStyleSheet(
            "font-size: 20px;"
        )

        self.labelPropiska = QLabel('Укажите адрес прописки         ', self)
        self.labelPropiska.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPropiska.setFixedSize(400, 100)
        self.textboxPropiska = QLineEdit(self)
        self.textboxPropiska.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxPropiska.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-' '0-9]+")))

        self.labelProjivanie = QLabel('Укажите адрес \nфактического проживания    ', self)
        self.labelProjivanie.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelProjivanie.setFixedSize(400, 100)
        self.textboxProjivanie = QLineEdit(self)
        self.textboxProjivanie.setStyleSheet(
            "font-size: 20px;"
        )

        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonBack.setFixedSize(250, 50)
        self.buttonBack.clicked.connect(self.Back)


        self.buttonNext = QPushButton('Завершить', self)
        self.buttonNext.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonNext.setFixedSize(250, 50)
        self.buttonNext.clicked.connect(self.Acept)

        self.labelStep = QLabel('Шаг 2 из 2', self)
        self.labelStep.setStyleSheet(
            "font-size: 20px;"
        )

        layout = QGridLayout()

        layout.addWidget(self.labelNameBlank, 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.addWidget(self.labelPasport, 1, 0, 2, 1)
        layout.addWidget(self.textboxPasport, 1, 1, 2, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.addWidget(self.labelPasport1, 2, 0, 2, 1)
        layout.addWidget(self.textboxPasport1, 2, 1, 2, 1)
        layout.setRowStretch(3, 1)
        layout.addWidget(self.labelPasport2, 3, 0, 2, 1)
        layout.addWidget(self.date, 3, 1, 2, 1)
        layout.addWidget(self.labelPropiska, 4, 0, 2, 1)
        layout.addWidget(self.textboxPropiska, 4, 1, 2, 1)
        layout.setRowStretch(4, 1)
        layout.addWidget(self.labelProjivanie, 5, 0, 2, 1)
        layout.addWidget(self.textboxProjivanie, 5, 1, 2, 1)
        layout.setRowStretch(5, 1)
        layout.addWidget(self.buttonBack, 7, 0, 2, 1)
        layout.addWidget(self.buttonNext, 7, 3, 2, 1)
        layout.addWidget(self.labelStep, 7, 1, 2, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setRowStretch(6, 1)
        layout.setRowStretch(7, 1)
        self.setLayout(layout)

    def Acept(self):
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
            propiska = " ".join(self.textboxPropiska.text().split()).title()
            projivanie = " ".join(self.textboxProjivanie.text().split()).title()
            numberPasport = " ".join(self.textboxPasport.text().split()).title()
            kemVidan = " ".join(self.textboxPasport1.text().split()).title()

            dateVidachi = date(yearB, monthB, dayB)
            zapis = (propiska, projivanie, numberPasport, kemVidan, dateVidachi, OpekunBlankTwo.id_rd)
            newRow = "UPDATE roditel SET propiska = %s, projivanie = %s, numberpasport = %s, vidanpasport = %s, datepasport = %s where id_roditel = %s"

            cursor.execute(newRow, zapis)
            connection.commit()
            connection.close()
            self.Next()

    def Next(self):
        self.w = End.WindowEnd()
        self.w.showMaximized()
        self.close()

    def Back(self):
        self.w = OpekunBlankTwo.WindowOpekunBlankTwo()
        self.w.showMaximized()
        self.close()