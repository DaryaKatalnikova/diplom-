import OpekunBlankTwo, AbiturInputTwo, onDataBase
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *
import pytesseract
import cv2
from mysql.connector import Error

import End

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


class WindowInputThree(QWidget):
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
                ''')
        self.initUI()
        self.resize(QSize(500, 400))
        self.pixmap = QPixmap('3.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

    def initUI(self):
        self.labelNameBlank = QLabel('Бланк для абитуриента\n'
                                     '   данные о школе', self)
        self.labelNameBlank.setStyleSheet(
            "font-size: 20px;"
        )

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
        self.comboboxObrazovanie.addItems(lschool)
        self.comboboxObrazovanie.setStyleSheet(
            "font-size: 20px;"
        )

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

        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.clicked.connect(self.Back)
        self.buttonBack.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonBack.setFixedSize(250, 50)

        self.buttonNext = QPushButton('Завершить ввод данных\nоб абитриенте', self)
        self.buttonNext.clicked.connect(self.Acept)
        self.buttonNext.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonNext.setFixedSize(250, 50)

        self.labelStep = QLabel('Шаг 3 из 3', self)
        self.labelStep.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonScan = QPushButton('Отсканировать документы', self)
        self.buttonScan.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonScan.setFixedSize(250, 50)

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
        layout.addWidget(self.labelStep, 8, 1, 2, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.buttonNext, 8, 3, 2, 1)
        layout.setRowStretch(7, 1)
        layout.setRowStretch(6, 1)
        self.setLayout(layout)

    def Acept(self):
        f = open('../static/proverka.txt', 'r')
        if (f != ''):
            id_st = int(f.read())
        else:
            print("ошибка")

        mat = self.comboboxMath.currentText()
        phy = self.comboboxPhys.currentText()
        rus = self.comboboxRus.currentText()
        it = self.comboboxIt.currentText()
        summ = int(mat) + int(rus) + int(phy) + int(it)
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
            predobrazovanie = " ".join(self.comboboxObrazovanie.currentText().split()).title()
            sred = str(self.Scan())
            if self.Check9.isChecked():
                check = " ".join("База 9 классов").title()
            elif self.Check11.isChecked():
                check = " ".join("База 11 классов").title()
            sredtwo = summ/4

            zapis1 = (check, sred, sredtwo, id_st)
            newRow1 = "UPDATE student SET bazovoeobrazovanie = %s, srednocenkaattestat = %s, srednocenka = %s  where id_student = %s"
            cursor.execute(newRow1, zapis1)
            connection.commit()

            nameschl = self.comboboxObrazovanie.currentText()
            def main_lamb(x):
                return x.split(' ')[0]
            itg = list(map(main_lamb, nameschl.split(', ')))
            cursor = connection.cursor()
            postgresql_select_query = "select nameschool from school where id_school = %s"
            cursor.execute(postgresql_select_query, (itg[0],))
            d = list(cursor.fetchone())
            c = d[0]
            zapis2 = (itg[0], id_st)
            newRow2 = "UPDATE student SET id_school = %s  where id_student = %s"
            cursor.execute(newRow2, zapis2)
            connection.commit()


            if centers == []:
                id_oc = 1
            else:
                id_oc = centers[len(centers) - 1][0]
                id_oc += 1
            zapis = (id_oc, math, mathOcen, id_st)
            newRow = "INSERT INTO ocenki (id_ocenki, predmet, ocenka, id_student) values (%s, %s, %s, %s)"

            cursor.execute(newRow,zapis)
            connection.commit()

            id_oc += 1
            zapis = (id_oc, rus, rusOcen, id_st)
            newRow = "INSERT INTO ocenki (id_ocenki, predmet, ocenka, id_student) values (%s, %s, %s, %s)"

            cursor.execute(newRow, zapis)
            connection.commit()

            id_oc += 1
            zapis = (id_oc, phys, physOcen, id_st)
            newRow = "INSERT INTO ocenki (id_ocenki, predmet, ocenka, id_student) values (%s, %s, %s, %s)"

            cursor.execute(newRow, zapis)
            connection.commit()

            id_oc += 1
            zapis = (id_oc, infor, inforOcen, id_st)
            newRow = "INSERT INTO ocenki (id_ocenki, predmet, ocenka, id_student) values (%s, %s, %s, %s)"

            cursor.execute(newRow, zapis)
            connection.commit()

            connection.close()
            self.Next()

    def Scan(self):
        image = cv2.imread("attestat.png")
        #C:\Users\g219.CIT\AppData\Local\Programs\Tesseract-OCR
        #C:\Program Files\Tesseract-OCR
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        string = pytesseract.image_to_string(image, lang='rus')
        with open('../static/atestat', 'w') as text_file:
            text_file.write(string)
        h = open('../static/atestat', 'r')
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

    def Next(self):
        f = open('../static/proverka.txt', 'r')
        if (f != ''):
            id_st = int(f.read())
        else:
            print("ошибка")
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        cursor = connection.cursor()
        postgresql_select_query = "select oplata from student where id_student = %s"
        cursor.execute(postgresql_select_query, (id_st,))
        d = list(cursor.fetchone())
        c = str(d[0])
        if c == "П Л А Т И Т   А Б И Т У Р И Е Н Т":
            self.w = End.WindowEnd()
            self.w.showMaximized()
            self.close()
        else:
            self.w = OpekunBlankTwo.WindowOpekunBlankTwo()
            self.w.showMaximized()
            self.close()

    def Back(self):
        self.w = AbiturInputTwo.WindowInputTwo()
        self.w.showMaximized()
        self.close()