import sys, AbiturInputOne, onDataBase, RedactOne, RedactThree, RedactTwo, RedactFour, RedactFive
from datetime import datetime

from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *
from mysql.connector import cursor
from mysql.connector import Error

import Output
import jinja2, pdfkit

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

selectST = "SELECT * FROM dogovor"
centers = execute_read_query(connection, selectST)
if centers ==[]:
    id_dg = 1
else:
    id_dg = centers[len(centers)-1][0]
    id_dg += 1

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



class WindowEnd(QWidget):
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
                        font-size: 14px;
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
                ''')
        self.initUI()
        self.pixmap = QPixmap('3.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

    def initUI(self):
        layout = QGridLayout()
        f = open('proverka.txt', 'r')
        self.labelASHIT = QLabel(self)
        if (f != ''):
            id_st = int(f.read())
        else:
            print("ошибка")
        global stroka
        self.labelAll = QLabel(self)
        self.labelAll.setStyleSheet(
            "font-size: 20px;"
        )
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        cursor = connection.cursor()
        postgresql_select_query = "select * from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        d.pop(0)
        secondName = str(d[0])
        name = str(d[1])
        midleName = str(d[2])
        hb = str(d[9])
        phone = str(d[4])
        emaill = str(d[3])
        numPas = str(d[11])
        kemVidanPas = str(d[5])
        datePas = str(d[6])
        propiska = str(d[7])
        projivanie = str(d[8])
        idSch = str(d[10])
        baza = str(d[12])
        oplt = str(d[13])
        srednOcen = str(d[14])
        srednOcenAtt = str(d[15])
        stroka1 = "Данные абиттуриента: " +'\n' + '\n' + "ФИО: " + secondName + ' ' + name + ' ' + midleName + '\n'+ "Дата рождения: " + hb + '\n' + "Номер телефона: " +phone + '\n' + "Почта: " + emaill + '\n' + \
                    '_____________________________________________________________________________________________'
        stroka2 = "Серия и номер паспорта: " + numPas + '\n' + "Кем выдан паспорт: " + kemVidanPas + '\n' + "Дата выдачи паспорта: " + datePas + '\n' + "Прописка: " + propiska + '\n' + "Проживание: " + projivanie + '\n' + \
                    '_____________________________________________________________________________________________'
        stroka3 = "Школа: " +idSch + '\n' + "Базавое образование: " + baza + '\n' + "Оплата: " +oplt + '\n' + "Средняя оценка: " +srednOcen + ' ' + \
                 "между 4 основными предметами" + '\n' + "Средняя оценка: " +srednOcenAtt + ' ' + "между всеми оценками аттестата" + '\n' \
                  + '_____________________________________________________________________________________________'

        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        cursor = connection.cursor()

        postgresql_select_query = "select oplata from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])


        if c == "П Л А Т И Т   А Б И Т У Р И Е Н Т":
            #self.labelAll.setText(str(stroka))
            self.buttonRedactPasRod = QPushButton('Отредактировать паспортные данные\n'
                                                  '    законного представителя', self)
            self.buttonRedactPasRod.setStyleSheet(
                "font-size: 20px;"
            )
            self.buttonRedactOsnRod = QPushButton('Отредактировать основные данные\n'
                                                  '    законного представителя', self)
            self.buttonRedactOsnRod.setStyleSheet(
                "font-size: 20px;"
            )
        else:
            postgresql_select_query = "select * from roditel where id_student = %s"
            cursor.execute(postgresql_select_query, (id_st,))
            b = list(cursor.fetchone())
            b.pop(0)
            secondNameR = str(b[1])
            nameR = str(b[0])
            midleNameR = str(b[2])
            phoneR = str(b[4])
            emaillR = str(b[3])
            numPasR = str(b[5])
            kemVidanPasR = str(b[6])
            datePasR = str(b[7])
            propiskaR = str(b[9])
            projivanieR = str(b[10])
            stroka4 = "Данные родителя: " + '\n' + '\n' + "ФИО: " + secondNameR + ' ' + nameR + ' ' + midleNameR + '\n' +  "Номер телефона: " + phoneR + '\n' + "Почта: " + emaillR + '\n' + \
                      '_____________________________________________________________________________________________'
            stroka5 = "Серия и номер паспорта: " + numPasR + '\n' + "Кем выдан паспорт: " + kemVidanPasR + '\n' + "Дата выдачи паспорта: " + datePasR + '\n' + "Прописка: " + propiskaR + '\n' + "Проживание: " + projivanieR + '\n' + \
                    '_____________________________________________________________________________________________'
            context = {'secondName': secondName, 'name': name, 'midleName': midleName,
                        'numPas': numPas, 'kemVidanPas': kemVidanPas, 'datePas': datePas, 'secondNameR': secondNameR, 'nameR': nameR, 'midleNameR': midleNameR,
                        'numPasR': numPasR, 'kemVidanPasR': kemVidanPasR, 'datePasR': datePasR}
            template_loader = jinja2.FileSystemLoader('./')
            template_env = jinja2.Environment(loader=template_loader)
            template = template_env.get_template('Dogovor.html')
            output_text = template.render(context)
            try:
                config = pdfkit.configuration(wkhtmltopdf='C:\\ProgramFiles\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
                pdfkit.from_string(output_text, 'pdf_generated.pdf', configuration=config)
                self.close()
            except:
                print("случилась ошибка")
            self.labelOsnR = QLabel()
            self.labelOsnR.setText(stroka4)
            self.labelOsnR.setStyleSheet(
                "font-size: 20px;"
            )
            self.labelPasR = QLabel()
            self.labelPasR.setText(stroka5)
            self.labelPasR.setStyleSheet(
                "font-size: 20px;"
            )
            layout.addWidget(self.labelOsnR, 3, 1)
            layout.addWidget(self.labelPasR, 4, 1)
            self.labelAll.setStyleSheet(
                "font-size: 20px;"
            )
            self.buttonRedactOsnRod = QPushButton('Отредактировать основные данные\n'
                                                  '    законного представителя', self)
            self.buttonRedactOsnRod.setStyleSheet(
                "font-size: 20px;"
            )
            self.buttonRedactOsnRod.clicked.connect(self.RedFour)

            self.buttonRedactPasRod = QPushButton('Отредактировать паспортные данные\n'
                                                  '    законного представителя', self)
            self.buttonRedactPasRod.setStyleSheet(
                "font-size: 20px;"
            )
            self.buttonRedactPasRod.clicked.connect(self.RedFive)
        self.labelOsn = QLabel()
        self.labelOsn.setText(stroka1)
        self.labelOsn.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPas = QLabel()
        self.labelPas.setText(stroka2)
        self.labelPas.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelSch = QLabel()
        self.labelSch.setText(stroka3)
        self.labelSch.setStyleSheet(
            "font-size: 20px;"
        )
        layout.addWidget(self.labelOsn, 0, 1)
        layout.addWidget(self.labelPas, 1, 1)
        layout.addWidget(self.labelSch, 2, 1)


        self.buttonRedactOsn = QPushButton('Отредактировать основыне данные\n ', self)
        self.buttonRedactOsn.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonRedactOsn.clicked.connect(self.RedOne)

        self.buttonRedactPas = QPushButton('Отредактировать паспортные данные\n ', self)
        self.buttonRedactPas.setStyleSheet(
            "font-size: 20px;"
            "line-height: 0px;"

        )
        self.buttonRedactPas.clicked.connect(self.RedTwo)

        self.buttonRedactSch = QPushButton('Отредактировать данные о школе\n ', self)
        self.buttonRedactSch.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonRedactSch.clicked.connect(self.RedThree)


        self.buttonExit = QPushButton('Завершить\n ', self)
        self.buttonExit.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonExit.clicked.connect(self.Exit)


        self.CheckObrabotka = QCheckBox(
            'Если абитуриент согласен на обработку персональных, \nто необходимо поставить галочку', self)
        self.CheckObrabotka.setStyleSheet(
            "font-size: 20px;"
        )


        # self.pixmap1 = QPixmap('4.png')
        # self.label1 = QLabel(self)
        # self.label1.setPixmap(self.pixmap1)
        # self.label1.resize(self.pixmap1.width(),
        #                   self.pixmap1.height())

        layout.addWidget(self.labelAll, 0, 0, 4, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setRowStretch(0, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        #layout.addWidget(self.label1, 1, 0, 6, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.buttonRedactOsn, 0, 2)
        layout.addWidget(self.buttonRedactPas, 1, 2)
        layout.addWidget(self.buttonRedactSch, 2, 2)
        layout.addWidget(self.buttonRedactOsnRod, 3, 2)
        layout.addWidget(self.buttonRedactPasRod, 4, 2)
        #layout.setRowStretch(5, 2)
        layout.addWidget(self.CheckObrabotka, 6, 1)
        layout.addWidget(self.buttonExit, 6, 2)
        self.setLayout(layout)

    def RedOne(self):
        self.w = RedactOne.WindowRedactOne()
        self.w.showMaximized()
        self.close()

    def RedTwo(self):
        self.w = RedactTwo.WindowRedactTwo()
        self.w.showMaximized()
        self.close()

    def RedThree(self):
        self.w = RedactThree.WindowRedactThree()
        self.w.showMaximized()
        self.close()

    def RedFour(self):
        self.w = RedactFour.WindowRedactFour()
        self.w.showMaximized()
        self.close()

    def RedFive(self):
        self.w = RedactFive.WindowRedactFive()
        self.w.showMaximized()
        self.close()

    def Exit(self):
        f = open('proverka.txt', 'r')
        if (f != ''):
            id_st = int(f.read())
        else:
            print("ошибка")
        if self.CheckObrabotka.isChecked():
            connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
            cursor = connection.cursor()
            postgresql_select_query = "select id_student from student where id_student = %s"
            cursor.execute(postgresql_select_query, (id_st,))
            d = list(cursor.fetchone())
            id = str(d[0])
            current_time = datetime.today().strftime("%y")
            current_time2 = datetime.today().strftime("%Y-%m-%d")
            numberDogvor = (id + "-O-" + current_time)
            connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
            cursor = connection.cursor()
            zapis = (id_dg, id_st, numberDogvor, current_time2)
            newRow = "INSERT INTO dogovor (id_dogovor, id_student, numberdogovor, datedogovor) values (%s, %s, %s, %s)"
            cursor.execute(newRow, zapis)
            connection.commit()
            connection.close()
            fil = open('proverka1.txt', 'r')
            if (fil == 'АДМИН'):
                #self.w = Output.WindowOutput()
                #self.w.showMaximized()
                self.close()
            else:
                #self.w = Output.WindowOutput()
                #self.w.showMaximized()
                self.close()
        else:
            connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
            delet = "DELETE FROM student where id_student = '%d'" % (id_st)
            with connection.cursor() as cursor:
                cursor.execute(delet)
                connection.commit()
                self.close()
            fil = open('proverka1.txt', 'r')
            if (fil == 'АДМИН'):
                self.w = Output.WindowOutput()
                self.w.showMaximized()
                self.close()
            else:
                self.close()

