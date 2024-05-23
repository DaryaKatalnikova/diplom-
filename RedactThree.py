import sys, OpekunBlankTwo, AbiturInputTwo, onDataBase, AbiturInputOne
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *
import pytesseract
import cv2
from mysql.connector import Error, cursor

import End
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

selectST = "SELECT * FROM ocenki"
centers = execute_read_query(connection, selectST)
if centers == []:
    id_oc = 1
else:
    id_oc = centers[len(centers)-1][0]
    id_oc += 1


class WindowRedactThree(QWidget):
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
                     QComboBox{
                        border: 1px solid #ced4da;
                        border-raduis 4px;
                        padding-left: 10px;
                        color: black;
                    }
                    QComboBox::on{
                        border: 4px solid #3657ff;
                    }
                    QComboBox QListView::item{
                        padding-left: 10px;
                        color: black;
                        background-color: #fff;
                    }
                    QComboBox QListView::item:hover{
                        padding-left: 10px;
                        color: black;
                        background-color: #1e90ff;
                    }
                    QComboBox QListView::item:selected{
                        background-color: #3657ff;
                    }
                    QComboBox::down-arrow{
                        width: 12px;
                        heidth: 12px;
                        margin-right 15px;
                    }
                    QRadioButton{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        color: #000000;
                    } 
                    QDateTime{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
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
        self.labelNameBlank = QLabel('Бланк для абитуриента\n'
                                     '   данные о школе', self)
        self.labelNameBlank.setStyleSheet(
            "font-size: 20px;"
        )
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        select_school = "SELECT * FROM school"
        school = execute_read_query(connection, select_school)
        lschool = list()
        for d in school:
            lschool.append(str(d).split(',')[0][1:] + " " + str(d).split(',')[1][2:len(str(d).split(',')[1]) - 1])
        self.labelObrazovanie = QLabel('Предыдущая образвательная организация', self)
        self.labelObrazovanie.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelObrazovanie.setFixedSize(400, 100)
        self.comboboxObrazovanie = QComboBox(self)
        self.comboboxObrazovanie.setStyleSheet(
            "font-size: 20px;"
        )
        self.comboboxObrazovanie.addItems(lschool)


        spisok = ['3', '4', '5']
        self.comboboxMath = QComboBox(self)
        self.labelMath = QLabel('Математика', self)
        self.labelMath.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelMath.setFixedSize(400, 100)
        self.comboboxMath.addItems(spisok)
        self.comboboxMath.setStyleSheet(
            "font-size: 20px;"
        )

        self.comboboxPhys = QComboBox(self)
        self.labelPhys = QLabel('Физика', self)
        self.labelPhys.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelPhys.setFixedSize(400, 100)
        self.comboboxPhys.addItems(spisok)
        self.comboboxPhys.setStyleSheet(
            "font-size: 20px;"
        )


        self.comboboxRus = QComboBox(self)
        self.labelRus = QLabel('Русский', self)
        self.labelRus.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelRus.setFixedSize(400, 100)
        self.comboboxRus.addItems(spisok)
        self.comboboxRus.setStyleSheet(
            "font-size: 20px;"
        )

        self.comboboxIt = QComboBox(self)
        self.labelIt = QLabel('Информатика', self)
        self.labelIt.setStyleSheet(
            "font-size: 20px;"
        )
        self.labelIt.setFixedSize(400, 100)
        self.comboboxIt.addItems(spisok)
        self.comboboxIt.setStyleSheet(
            "font-size: 20px;"
        )
        #self.comboboxIt.setEditable(True)



        #currentText()	Извлекает текст выбранного в данный момент элемента

        self.Check9 = QRadioButton('На базе 9 классов', self)
        self.Check9.setStyleSheet(
            "font-size: 20px;"
        )

        self.Check11 = QRadioButton('На базе 11 классов', self)
        self.Check11.setStyleSheet(
            "font-size: 20px;"
        )

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.Check9)
        self.button_group.addButton(self.Check11)

        self.buttonBack = QPushButton('Отмена', self)
        self.buttonBack.clicked.connect(self.Back)
        self.buttonBack.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonBack.setFixedSize(250, 50)

        self.buttonNext = QPushButton('Изменить', self)
        self.buttonNext.clicked.connect(self.Acept)
        self.buttonNext.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonNext.setFixedSize(250, 50)

        self.buttonScan = QPushButton('Отсканировать аттестат\nдля подсчета среденго бала', self)
        self.buttonScan.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonScan.setFixedSize(250, 50)

        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        cursor = connection.cursor()
        postgresql_select_query = "select bazovoeobrazovanie from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        if c == "Б А З А   1 1   К Л А С С О В":
            self.Check11.click()
        else:
            self.Check9.click()

        layout = QGridLayout()

        layout.addWidget(self.labelNameBlank, 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setRowStretch(0, 1)
        layout.addWidget(self.labelObrazovanie, 1, 0, 2, 1)
        layout.addWidget(self.comboboxObrazovanie, 1, 1, 2, 1)
        layout.addWidget(self.labelMath, 2, 0, 2, 1)
        layout.addWidget(self.comboboxMath, 2, 1, 2, 1)
        layout.setRowStretch(1, 1)
        layout.addWidget(self.labelIt, 3, 0, 2, 1)
        layout.addWidget(self.comboboxIt, 3, 1, 2, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.addWidget(self.labelRus, 4, 0, 2, 1)
        layout.addWidget(self.comboboxRus, 4, 1, 2, 1)
        layout.setRowStretch(3, 1)
        layout.addWidget(self.labelPhys, 5, 0, 2, 1)
        layout.addWidget(self.comboboxPhys, 5, 1, 2, 1)
        layout.setRowStretch(4, 1)
        layout.addWidget(self.buttonScan, 2, 3, 2, 1)
        layout.addWidget(self.Check9, 6, 1, 2, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.Check11, 6, 2, 2, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.buttonBack, 8, 0, 2, 1)
        layout.setRowStretch(5, 1)
        layout.addWidget(self.buttonNext, 8, 3, 2, 1)
        layout.setRowStretch(7, 1)
        layout.setRowStretch(6, 1)
        self.setLayout(layout)

    def Scan(self):
        image = cv2.imread("attestat.png")
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        string = pytesseract.image_to_string(image, lang='rus')
        with open('atestat', 'w') as text_file:
            text_file.write(string)
        h = open('atestat', 'r')
        content = h.readlines()
        a = 0
        b = 0
        for line in content:
            for i in line:
                if i.isdigit() == True:
                    a += int(i)
                    b += 1
        sredn = a/b
        return (sredn)

    def Acept(self, id_oc):
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
            math = " ".join(self.labelMath.text().split()).title()
            rus = " ".join(self.labelRus.text().split()).title()
            phys = " ".join(self.labelPhys.text().split()).title()
            infor = " ".join(self.labelIt.text().split()).title()
            mathOcen = int(" ".join(self.comboboxMath.currentText()).title())
            rusOcen = int(" ".join(self.comboboxRus.currentText()).title())
            physOcen = int(" ".join(self.comboboxPhys.currentText()).title())
            inforOcen = int(" ".join(self.comboboxIt.currentText()).title())
            sred = str(self.Scan())
            if self.Check9.isChecked():
                check = " ".join("База 9 классов").title()

            elif self.Check11.isChecked():
                check = " ".join("База 11 классов").title()

            zapis1 = (check, sred, id_st)
            newRow1 = "UPDATE student SET bazovoeobrazovanie = %s, srednocenkaattestat = %s  where id_student = %s"
            cursor.execute(newRow1, zapis1)
            connection.commit()

            if centers == []:
                id_oc = 1
            else:
                id_oc = centers[len(centers) - 1][0]
                id_oc += 1
            zapis = (math, mathOcen, id_oc, id_st)
            newRow = "UPDATE ocenki SET predmet = %s, ocenka = %s where id_ocenki = %s and id_student = %s"

            cursor.execute(newRow, zapis)
            connection.commit()

            id_oc += 1
            zapis = (rus, rusOcen, id_oc, id_st)
            newRow = "UPDATE ocenki SET predmet = %s, ocenka = %s where id_ocenki = %s and id_student = %s"

            cursor.execute(newRow, zapis)
            connection.commit()

            id_oc += 1
            zapis = (phys, physOcen, id_oc, id_st)
            newRow = "UPDATE ocenki SET predmet = %s, ocenka = %s where id_ocenki = %s and id_student = %s"

            cursor.execute(newRow, zapis)
            connection.commit()

            id_oc += 1
            zapis = (infor, inforOcen, id_oc, id_st)
            newRow = "UPDATE ocenki SET predmet = %s, ocenka = %s where id_ocenki = %s and id_student = %s"

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