import sys, AbiturInputOne, AbiturInputThree, onDataBase
from datetime import date

from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *
import pytesseract
import cv2
from mysql.connector import Error

import End
import OpekunBlankTwo
import Output

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


class WindowRedactTwo(QWidget):
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

        self.labelNameBlank = QLabel('Бланк для абитуриента\n'
                                     '  паспортные данные', self)
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
        cursor = connection.cursor()
        postgresql_select_query = "select numberpasport from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxPasport.setText(c)
        self.textboxPasport.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9' ']+")))
        self.textboxPasport.setMaxLength(11)

        self.labelPasport1 = QLabel('Кем выдан', self)
        self.labelPasport1.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPasport1.setFixedSize(400, 100)
        self.textboxPasport1 = QLineEdit(self)
        self.textboxPasport1.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select vidanpasport from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxPasport1.setText(c)
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
        cursor = connection.cursor()
        postgresql_select_query = "select datepasport from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = d[0]
        self.date.setDate(c)

        self.labelPropiska = QLabel('Укажите адрес прописки         ', self)
        self.labelPropiska.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPropiska.setFixedSize(400, 100)
        self.textboxPropiska = QLineEdit(self)
        self.textboxPropiska.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select propiska from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxPropiska.setText(c)
        self.textboxPropiska.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-]+")))

        self.labelProjivanie = QLabel('Укажите адрес \nфактического проживания    ', self)
        self.labelProjivanie.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelProjivanie.setFixedSize(400, 100)
        self.textboxProjivanie = QLineEdit(self)
        self.textboxProjivanie.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select projivanie from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        self.textboxProjivanie.setText(c)
        self.textboxProjivanie.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Zа-яА-Я-]+")))

        self.CheckOplata = QCheckBox(
            'Если абитуриент будет оплачивать учебу самостоятельно, \nто необходимо поставить галочку', self)
        self.CheckOplata.setStyleSheet(
            "font-size: 20px;"
        )
        cursor = connection.cursor()
        postgresql_select_query = "select oplata from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        print(c)
        if c == "П Л А Т И Т   А Б И Т У Р И Е Н Т":
            self.CheckOplata.setChecked(True)


        self.buttonBack = QPushButton('Отмена', self)
        self.buttonBack.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonBack.setFixedSize(250, 50)
        self.buttonBack.clicked.connect(self.Back1)


        self.buttonNext = QPushButton('Изменить', self)
        self.buttonNext.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonNext.setFixedSize(250, 50)
        self.buttonNext.clicked.connect(self.Acept)



        layout = QGridLayout()

        layout.addWidget(self.labelNameBlank, 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setRowStretch(0, 1)
        layout.addWidget(self.labelPasport, 1, 0, 2, 1)
        layout.addWidget(self.textboxPasport, 1, 1, 2, 1)
        layout.setRowStretch(1, 1)
        layout.addWidget(self.labelPasport1, 2, 0, 2, 1)
        layout.addWidget(self.textboxPasport1, 2, 1, 2, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.addWidget(self.labelPasport2, 3, 0, 2, 1)
        layout.addWidget(self.date, 3, 1, 2, 1)
        layout.setRowStretch(3, 1)
        layout.addWidget(self.labelPropiska, 4, 0, 2, 1)
        layout.addWidget(self.textboxPropiska, 4, 1, 2, 1)
        layout.setRowStretch(4, 1)
        layout.addWidget(self.labelProjivanie, 5, 0, 2, 1)
        layout.addWidget(self.textboxProjivanie, 5, 1, 2, 1)
        layout.addWidget(self.CheckOplata, 6, 1, 2, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.buttonBack, 8, 0, 2, 1)
        layout.setRowStretch(5, 1)
        layout.addWidget(self.buttonNext, 8, 3, 2, 1)
        layout.setRowStretch(7, 1)
        layout.setRowStretch(6, 1)
        self.setLayout(layout)


    def Scan(self):
        image = cv2.imread("snils.png")
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        string = pytesseract.image_to_string(image, lang='rus')
        with open('snilsScun.txt', 'w') as text_file:
            text_file.write(string)
        h = open('snilsScun.txt', 'r')
        content = h.readlines()
        snils = ''
        for line in content:
            for i in line:
                if i.isdigit() == True:
                    snils = snils + i
            if snils != "":
                break
        print(snils)
        return (snils)


    def Acept(self, id_st):
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
            propiska = " ".join(self.textboxPropiska.text().split()).title()
            projivanie = " ".join(self.textboxProjivanie.text().split()).title()
            numberPasport = " ".join(self.textboxPasport.text().split()).title()
            kemVidan = " ".join(self.textboxPasport1.text().split()).title()

            if self.CheckOplata.isChecked():
                check = " ".join("Платит абитуриент").title()
            else:
                check = " ".join("Платит представитель абитуриента").title()
            dateVidachi = date(yearB, monthB, dayB)
            zapis = (propiska, projivanie, numberPasport, kemVidan, dateVidachi, check, id_st)
            newRow = "UPDATE student SET propiska = %s, projivanie = %s, numberpasport = %s, " \
                     "vidanpasport = %s, datepasport = %s, oplata = %s where id_student = %s"

            cursor.execute(newRow, zapis)
            connection.commit()
            connection.close()
            connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
            cursor = connection.cursor()
            postgresql_select_query = "select oplata from student where id_student = %s"
            cursor.execute(postgresql_select_query, (id_st,))
            d = list(cursor.fetchone())
            c = str(d[0])

            if c == "П Л А Т И Т   А Б И Т У Р И Е Н Т":
                self.Next()
            else:
                self.Next1()

    def Next1(self):
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

    def Back1(self):
        self.w = End.WindowEnd()
        self.w.showMaximized()
        self.close()