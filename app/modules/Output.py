from PyQt6.QtWidgets import *
from mysql.connector import Error

import onDataBase, readact, Oplata
from app import main
from app.modules import AbiturInputOne

connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbasit")
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
    id_st = 1
else:
    id_st = centers[len(centers)-1][0]
    id_st += 1

class WindowOutput(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Академичсекая Школа Информационных Технологий")
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
                    QTableWidget{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        background-color: #FFFFFF;
                        color: #000000;
                    }
                    QHeaderView::section{
                        font-family: Ubuntu Mono;
                        font-size: 15;
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

    def initUI(self):
        self.table = QTableWidget(0, 24)
        self.table.setHorizontalHeaderLabels(["Дата подписания\nдоговора", "Номер договора", "Базавое образование",
                                              "Фамилия", "Имя", "Отчество", "Снилс", "М", "Ф", "Р", "И",
                                              "С/б", "С/б/а", "Предыдущая образовательная\nорганизация", "Телефон",
                                              "e-mail", "Адре прописки", "Фактический адрес\nпроживания",
                                              "Фамилия\nродителя", "Имя\nродителя", "Отчество\nродителя", "Телефон\nродителя", "e-mail\nродителя"])

        self.table.setColumnWidth(0, 15)
        self.table.setColumnWidth(1, 120)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 300)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 150)
        self.table.setColumnWidth(7, 100)
        self.table.setColumnWidth(8, 15)
        self.table.setColumnWidth(9, 15)
        self.table.setColumnWidth(10, 15)
        self.table.setColumnWidth(11, 15)
        self.table.setColumnWidth(12, 35)
        self.table.setColumnWidth(13, 45)
        self.table.setColumnWidth(14, 300)
        self.table.setColumnWidth(15, 200)
        self.table.setColumnWidth(16, 200)
        self.table.setColumnWidth(17, 300)
        self.table.setColumnWidth(18, 300)
        self.table.setColumnWidth(19, 150)
        self.table.setColumnWidth(20, 150)
        self.table.setColumnWidth(21, 150)
        self.table.setColumnWidth(22, 150)
        self.table.setColumnWidth(23, 200)
        self.table.setColumnWidth(24, 200)
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(10, 10, 150, 40)
        self.comboBox.setPlaceholderText('Сортировать по')
        self.comboBox.addItem('алфавиту А-Я')
        self.comboBox.addItem('алфавиту Я-А')
        self.comboBox.addItem('убыванию средней оценки')
        self.comboBox.addItem('возрастанию срдней оценки')
        self.comboBox.activated.connect(self.OnActivated)

        self.table.cellPressed[int, int].connect(self.clickedRowColumn)
        self.table.setRowCount(0)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student ORDER BY id_student")
        results = list(cursor.fetchall())
        for i in results:
            idd = int(i[0])
            a = "select ocenka from ocenki where id_student = %s"
            cursor.execute(a, (idd,))
            d = cursor.fetchall()
            rowPosition = self.table.rowCount()
            self.table.insertRow(rowPosition)
            for a in d:
                m = d[0][0]
                self.table.setItem(rowPosition, 7, QTableWidgetItem(str(m)))
                r = d[1][0]
                self.table.setItem(rowPosition, 8, QTableWidgetItem(str(r)))
                phs = d[2][0]
                self.table.setItem(rowPosition, 9, QTableWidgetItem(str(phs)))
                inf = d[3][0]
                self.table.setItem(rowPosition, 10, QTableWidgetItem(str(inf)))
            a = "select numberdogovor, datedogovor from dogovor where id_student = %s"
            cursor.execute(a, (idd,))
            dogv = cursor.fetchall()
            for a in d:
                self.table.setItem(rowPosition, 1, QTableWidgetItem(str(dogv[0][0])))
                self.table.setItem(rowPosition, 0, QTableWidgetItem(str(dogv[0][1])))
            a = "select secondname, namee, midlename, email, numberphone from roditel where id_student = %s"
            cursor.execute(a, (idd,))
            rod = cursor.fetchall()
            if rod != []:
                for a in d:
                    self.table.setItem(rowPosition, 18, QTableWidgetItem(rod[0][0]))
                    self.table.setItem(rowPosition, 19, QTableWidgetItem(rod[0][1]))
                    self.table.setItem(rowPosition, 20, QTableWidgetItem(rod[0][2]))
                    self.table.setItem(rowPosition, 21, QTableWidgetItem(rod[0][3]))
                    self.table.setItem(rowPosition, 22, QTableWidgetItem(rod[0][4]))
            else:
                self.table.setItem(rowPosition, 18, QTableWidgetItem("-"))
                self.table.setItem(rowPosition, 19, QTableWidgetItem("-"))
                self.table.setItem(rowPosition, 20, QTableWidgetItem("-"))
                self.table.setItem(rowPosition, 21, QTableWidgetItem("-"))
                self.table.setItem(rowPosition, 22, QTableWidgetItem("-"))
            secondName = str(i[1])
            name = str(i[2])
            midleName = str(i[3])
            phone = str(i[5])
            emaill = str(i[4])
            propiska = str(i[8])
            projivanie = str(i[9])
            idSch = str(i[11])
            baza = str(i[13])
            srednOcen = str(i[15])
            srednOcenAtt = str(i[16])
            self.table.setItem(rowPosition, 2, QTableWidgetItem(baza))
            self.table.setItem(rowPosition, 3, QTableWidgetItem(secondName))
            self.table.setItem(rowPosition, 4, QTableWidgetItem(name))
            self.table.setItem(rowPosition, 5, QTableWidgetItem(midleName))
            self.table.setItem(rowPosition, 11, QTableWidgetItem(srednOcen))
            self.table.setItem(rowPosition, 12, QTableWidgetItem(srednOcenAtt))
            self.table.setItem(rowPosition, 13, QTableWidgetItem(idSch))
            self.table.setItem(rowPosition, 14, QTableWidgetItem(phone))
            self.table.setItem(rowPosition, 15, QTableWidgetItem(emaill))
            self.table.setItem(rowPosition, 16, QTableWidgetItem(propiska))
            self.table.setItem(rowPosition, 17, QTableWidgetItem(projivanie))
        self.buttonPay = QPushButton("Оплаты" , self)
        self.buttonPay.setFixedSize(250, 70)
        self.buttonPay.setStyleSheet("font-size: 25px;")
        self.buttonPay.clicked.connect(self.Pay)

        self.buttonM = QPushButton("Найти", self)
        self.buttonM.setFixedSize(250, 70)
        self.buttonM.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonM.clicked.connect(self.Search)
        self.buttonSearch = QPushButton("Добавить\nстудента", self)
        self.buttonSearch.setFixedSize(250, 70)
        self.buttonSearch.setStyleSheet(
            "font-size: 25px;"
        )
        self.textboxsearch = QLineEdit(self)
        self.textboxsearch.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonSearch.clicked.connect(self.Input)
        self.buttonInput = QPushButton('Назад', self)
        self.buttonInput.setFixedSize(250, 70)
        self.buttonInput.setStyleSheet(
            "font-size: 25px;"
        )
        self.buttonInput.clicked.connect(self.Back)
        vbox = QVBoxLayout()
        vbox.addWidget(self.comboBox)
        vbox.addWidget(self.table)
        vbox.addWidget(self.textboxsearch)
        vbox = QVBoxLayout()
        vbox.addWidget(self.comboBox)
        vbox.addWidget(self.table)
        vbox.addWidget(self.textboxsearch)
        hbox = QHBoxLayout()
        hbox.addWidget(self.buttonInput)
        hbox.addWidget(self.buttonM)
        hbox.addWidget(self.buttonSearch)
        hbox.addWidget(self.buttonPay)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setLayout(vbox)
        #, alignment=Qt.AlignmentFlag.AlignRight , alignment=Qt.AlignmentFlag.AlignCenter , alignment=Qt.AlignmentFlag.AlignLeft

    def Input(self):
        file = open("../static/proverka1.txt", "w", encoding='utf-8')
        file.write("АДМИН")
        self.w = AbiturInputOne.WindowInputOne()
        self.w.showMaximized()
        self.close()

    def Search(self):
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        cursor = connection.cursor()
        try:
            request = " ".join(self.textboxsearch.text().split()).title()
            cursor.execute(
                f"SELECT * FROM student WHERE secondname LIKE '%{request}%' or namee LIKE '%{request}%' or midlename LIKE '%{request}%'")
            results = cursor.fetchall()
            self.table.setRowCount(0)
            print(results)
            for x in results:
                self.table.setRowCount(0)
                for i in results:
                    idd = int(i[0])
                    print(idd)
                    a = "select ocenka from ocenki where id_student = %s"
                    cursor.execute(a, (idd,))
                    d = cursor.fetchall()
                    rowPosition = self.table.rowCount()
                    self.table.insertRow(rowPosition)
                    for a in d:
                        m = d[0][0]
                        self.table.setItem(rowPosition, 8, QTableWidgetItem(str(m)))
                        r = d[1][0]
                        self.table.setItem(rowPosition, 9, QTableWidgetItem(str(r)))
                        phs = d[2][0]
                        self.table.setItem(rowPosition, 10, QTableWidgetItem(str(phs)))
                        inf = d[3][0]
                        self.table.setItem(rowPosition, 11, QTableWidgetItem(str(inf)))
                    a = "select numberdogovor, datedogovor from dogovor where id_student = %s"
                    cursor.execute(a, (idd,))
                    dogv = cursor.fetchall()
                    for a in d:
                        self.table.setItem(rowPosition, 2, QTableWidgetItem(str(dogv[0][0])))
                        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(dogv[0][1])))
                    a = "select secondname, namee, midlename, email, numberphone from roditel where id_student = %s"
                    cursor.execute(a, (idd,))
                    rod = cursor.fetchall()
                    if rod != []:
                        for a in d:
                            self.table.setItem(rowPosition, 19, QTableWidgetItem(rod[0][0]))
                            self.table.setItem(rowPosition, 20, QTableWidgetItem(rod[0][1]))
                            self.table.setItem(rowPosition, 21, QTableWidgetItem(rod[0][2]))
                            self.table.setItem(rowPosition, 22, QTableWidgetItem(rod[0][3]))
                            self.table.setItem(rowPosition, 23, QTableWidgetItem(rod[0][4]))
                    else:
                        self.table.setItem(rowPosition, 19, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 20, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 21, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 22, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 23, QTableWidgetItem("-"))
                    secondName = str(i[1])
                    name = str(i[2])
                    midleName = str(i[3])
                    phone = str(i[5])
                    emaill = str(i[4])
                    propiska = str(i[8])
                    projivanie = str(i[9])
                    idSch = str(i[11])
                    baza = str(i[13])
                    srednOcen = str(i[15])
                    srednOcenAtt = str(i[16])
                    self.table.setItem(rowPosition, 0, QTableWidgetItem(str(idd)))
                    self.table.setItem(rowPosition, 3, QTableWidgetItem(baza))
                    self.table.setItem(rowPosition, 4, QTableWidgetItem(secondName))
                    self.table.setItem(rowPosition, 5, QTableWidgetItem(name))
                    self.table.setItem(rowPosition, 6, QTableWidgetItem(midleName))
                    self.table.setItem(rowPosition, 12, QTableWidgetItem(srednOcen))
                    self.table.setItem(rowPosition, 13, QTableWidgetItem(srednOcenAtt))
                    self.table.setItem(rowPosition, 14, QTableWidgetItem(idSch))
                    self.table.setItem(rowPosition, 15, QTableWidgetItem(phone))
                    self.table.setItem(rowPosition, 16, QTableWidgetItem(emaill))
                    self.table.setItem(rowPosition, 17, QTableWidgetItem(propiska))
                    self.table.setItem(rowPosition, 18, QTableWidgetItem(projivanie))

        except Error as e:
            print(e)
            connection.rollback()
            connection.close()

    def clickedRowColumn(self, r, c):
        d = 0
        if c == 0:
            d = self.table.currentItem().text()
            print(d)
        file = open("../static/proverka.txt", "w")
        file.write(str(d))
        self.w = readact.WindowRedact()
        self.w.show()

    def OnActivated(self):
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbASIT")
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT count(*) FROM student")
            kolstr = str(cursor.fetchall())
            kolstr1 = int(kolstr[2])
            self.table.removeRow(kolstr1)
            text = " ".join(self.comboBox.currentText().split())
            if text == 'убыванию средней оценки':
                self.table.setRowCount(0)
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM student ORDER BY srednocenka desc")
                results = list(cursor.fetchall())
                for i in results:
                    idd = int(i[0])
                    a = "select ocenka from ocenki where id_student = %s"
                    cursor.execute(a, (idd,))
                    d = cursor.fetchall()
                    rowPosition = self.table.rowCount()
                    self.table.insertRow(rowPosition)
                    for a in d:
                        m = d[0][0]
                        self.table.setItem(rowPosition, 8, QTableWidgetItem(str(m)))
                        r = d[1][0]
                        self.table.setItem(rowPosition, 9, QTableWidgetItem(str(r)))
                        phs = d[2][0]
                        self.table.setItem(rowPosition, 10, QTableWidgetItem(str(phs)))
                        inf = d[3][0]
                        self.table.setItem(rowPosition, 11, QTableWidgetItem(str(inf)))
                    a = "select numberdogovor, datedogovor from dogovor where id_student = %s"
                    cursor.execute(a, (idd,))
                    dogv = cursor.fetchall()
                    for a in d:
                        self.table.setItem(rowPosition, 2, QTableWidgetItem(str(dogv[0][0])))
                        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(dogv[0][1])))
                    a = "select secondname, namee, midlename, email, numberphone from roditel where id_student = %s"
                    cursor.execute(a, (idd,))
                    rod = cursor.fetchall()
                    if rod != []:
                        for a in d:
                            self.table.setItem(rowPosition, 19, QTableWidgetItem(rod[0][0]))
                            self.table.setItem(rowPosition, 20, QTableWidgetItem(rod[0][1]))
                            self.table.setItem(rowPosition, 21, QTableWidgetItem(rod[0][2]))
                            self.table.setItem(rowPosition, 22, QTableWidgetItem(rod[0][3]))
                            self.table.setItem(rowPosition, 23, QTableWidgetItem(rod[0][4]))
                    else:
                        self.table.setItem(rowPosition, 19, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 20, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 21, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 22, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 23, QTableWidgetItem("-"))
                    secondName = str(i[1])
                    name = str(i[2])
                    midleName = str(i[3])
                    phone = str(i[5])
                    emaill = str(i[4])
                    propiska = str(i[8])
                    projivanie = str(i[9])
                    idSch = str(i[11])
                    baza = str(i[13])
                    srednOcen = str(i[15])
                    srednOcenAtt = str(i[16])
                    self.table.setItem(rowPosition, 0, QTableWidgetItem(str(idd)))
                    self.table.setItem(rowPosition, 3, QTableWidgetItem(baza))
                    self.table.setItem(rowPosition, 4, QTableWidgetItem(secondName))
                    self.table.setItem(rowPosition, 5, QTableWidgetItem(name))
                    self.table.setItem(rowPosition, 6, QTableWidgetItem(midleName))
                    self.table.setItem(rowPosition, 12, QTableWidgetItem(srednOcen))
                    self.table.setItem(rowPosition, 13, QTableWidgetItem(srednOcenAtt))
                    self.table.setItem(rowPosition, 14, QTableWidgetItem(idSch))
                    self.table.setItem(rowPosition, 15, QTableWidgetItem(phone))
                    self.table.setItem(rowPosition, 16, QTableWidgetItem(emaill))
                    self.table.setItem(rowPosition, 17, QTableWidgetItem(propiska))
                    self.table.setItem(rowPosition, 18, QTableWidgetItem(projivanie))
            elif text == 'возрастанию срдней оценки':
                self.table.setRowCount(0)
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM student ORDER BY srednocenka asc")
                results = list(cursor.fetchall())
                for i in results:
                    idd = int(i[0])
                    a = "select ocenka from ocenki where id_student = %s"
                    cursor.execute(a, (idd,))
                    d = cursor.fetchall()
                    rowPosition = self.table.rowCount()
                    self.table.insertRow(rowPosition)
                    for a in d:
                        m = d[0][0]
                        self.table.setItem(rowPosition, 8, QTableWidgetItem(str(m)))
                        r = d[1][0]
                        self.table.setItem(rowPosition, 9, QTableWidgetItem(str(r)))
                        phs = d[2][0]
                        self.table.setItem(rowPosition, 10, QTableWidgetItem(str(phs)))
                        inf = d[3][0]
                        self.table.setItem(rowPosition, 11, QTableWidgetItem(str(inf)))
                    a = "select numberdogovor, datedogovor from dogovor where id_student = %s"
                    cursor.execute(a, (idd,))
                    dogv = cursor.fetchall()
                    for a in d:
                        self.table.setItem(rowPosition, 2, QTableWidgetItem(str(dogv[0][0])))
                        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(dogv[0][1])))
                    a = "select secondname, namee, midlename, email, numberphone from roditel where id_student = %s"
                    cursor.execute(a, (idd,))
                    rod = cursor.fetchall()
                    if rod != []:
                        for a in d:
                            self.table.setItem(rowPosition, 19, QTableWidgetItem(rod[0][0]))
                            self.table.setItem(rowPosition, 20, QTableWidgetItem(rod[0][1]))
                            self.table.setItem(rowPosition, 21, QTableWidgetItem(rod[0][2]))
                            self.table.setItem(rowPosition, 22, QTableWidgetItem(rod[0][3]))
                            self.table.setItem(rowPosition, 23, QTableWidgetItem(rod[0][4]))
                    else:
                        self.table.setItem(rowPosition, 19, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 20, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 21, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 22, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 23, QTableWidgetItem("-"))
                    secondName = str(i[1])
                    name = str(i[2])
                    midleName = str(i[3])
                    phone = str(i[5])
                    emaill = str(i[4])
                    propiska = str(i[8])
                    projivanie = str(i[9])
                    idSch = str(i[11])
                    baza = str(i[13])
                    srednOcen = str(i[15])
                    srednOcenAtt = str(i[16])
                    self.table.setItem(rowPosition, 0, QTableWidgetItem(str(idd)))
                    self.table.setItem(rowPosition, 3, QTableWidgetItem(baza))
                    self.table.setItem(rowPosition, 4, QTableWidgetItem(secondName))
                    self.table.setItem(rowPosition, 5, QTableWidgetItem(name))
                    self.table.setItem(rowPosition, 6, QTableWidgetItem(midleName))
                    self.table.setItem(rowPosition, 12, QTableWidgetItem(srednOcen))
                    self.table.setItem(rowPosition, 13, QTableWidgetItem(srednOcenAtt))
                    self.table.setItem(rowPosition, 14, QTableWidgetItem(idSch))
                    self.table.setItem(rowPosition, 15, QTableWidgetItem(phone))
                    self.table.setItem(rowPosition, 16, QTableWidgetItem(emaill))
                    self.table.setItem(rowPosition, 17, QTableWidgetItem(propiska))
                    self.table.setItem(rowPosition, 18, QTableWidgetItem(projivanie))
            elif text == 'алфавиту А-Я':
                self.table.setRowCount(0)
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM student ORDER BY secondname asc")
                results = list(cursor.fetchall())
                for i in results:
                    idd = int(i[0])
                    a = "select ocenka from ocenki where id_student = %s"
                    cursor.execute(a, (idd,))
                    d = cursor.fetchall()
                    rowPosition = self.table.rowCount()
                    self.table.insertRow(rowPosition)
                    for a in d:
                        m = d[0][0]
                        self.table.setItem(rowPosition, 8, QTableWidgetItem(str(m)))
                        r = d[1][0]
                        self.table.setItem(rowPosition, 9, QTableWidgetItem(str(r)))
                        phs = d[2][0]
                        self.table.setItem(rowPosition, 10, QTableWidgetItem(str(phs)))
                        inf = d[3][0]
                        self.table.setItem(rowPosition, 11, QTableWidgetItem(str(inf)))
                    a = "select numberdogovor, datedogovor from dogovor where id_student = %s"
                    cursor.execute(a, (idd,))
                    dogv = cursor.fetchall()
                    for a in d:
                        self.table.setItem(rowPosition, 2, QTableWidgetItem(str(dogv[0][0])))
                        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(dogv[0][1])))
                    a = "select secondname, namee, midlename, email, numberphone from roditel where id_student = %s"
                    cursor.execute(a, (idd,))
                    rod = cursor.fetchall()
                    if rod != []:
                        for a in d:
                            self.table.setItem(rowPosition, 19, QTableWidgetItem(rod[0][0]))
                            self.table.setItem(rowPosition, 20, QTableWidgetItem(rod[0][1]))
                            self.table.setItem(rowPosition, 21, QTableWidgetItem(rod[0][2]))
                            self.table.setItem(rowPosition, 22, QTableWidgetItem(rod[0][3]))
                            self.table.setItem(rowPosition, 23, QTableWidgetItem(rod[0][4]))
                    else:
                        self.table.setItem(rowPosition, 19, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 20, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 21, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 22, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 23, QTableWidgetItem("-"))
                    secondName = str(i[1])
                    name = str(i[2])
                    midleName = str(i[3])
                    phone = str(i[5])
                    emaill = str(i[4])
                    propiska = str(i[8])
                    projivanie = str(i[9])
                    idSch = str(i[11])
                    baza = str(i[13])
                    srednOcen = str(i[15])
                    srednOcenAtt = str(i[16])
                    self.table.setItem(rowPosition, 0, QTableWidgetItem(str(idd)))
                    self.table.setItem(rowPosition, 3, QTableWidgetItem(baza))
                    self.table.setItem(rowPosition, 4, QTableWidgetItem(secondName))
                    self.table.setItem(rowPosition, 5, QTableWidgetItem(name))
                    self.table.setItem(rowPosition, 6, QTableWidgetItem(midleName))
                    self.table.setItem(rowPosition, 12, QTableWidgetItem(srednOcen))
                    self.table.setItem(rowPosition, 13, QTableWidgetItem(srednOcenAtt))
                    self.table.setItem(rowPosition, 14, QTableWidgetItem(idSch))
                    self.table.setItem(rowPosition, 15, QTableWidgetItem(phone))
                    self.table.setItem(rowPosition, 16, QTableWidgetItem(emaill))
                    self.table.setItem(rowPosition, 17, QTableWidgetItem(propiska))
                    self.table.setItem(rowPosition, 18, QTableWidgetItem(projivanie))
            elif text == 'алфавиту Я-А':
                self.table.setRowCount(0)
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM student ORDER BY secondname desc")
                results = list(cursor.fetchall())
                for i in results:
                    idd = int(i[0])
                    a = "select ocenka from ocenki where id_student = %s"
                    cursor.execute(a, (idd,))
                    d = cursor.fetchall()
                    rowPosition = self.table.rowCount()
                    self.table.insertRow(rowPosition)
                    for a in d:
                        m = d[0][0]
                        self.table.setItem(rowPosition, 8, QTableWidgetItem(str(m)))
                        r = d[1][0]
                        self.table.setItem(rowPosition, 9, QTableWidgetItem(str(r)))
                        phs = d[2][0]
                        self.table.setItem(rowPosition, 10, QTableWidgetItem(str(phs)))
                        inf = d[3][0]
                        self.table.setItem(rowPosition, 11, QTableWidgetItem(str(inf)))
                    a = "select numberdogovor, datedogovor from dogovor where id_student = %s"
                    cursor.execute(a, (idd,))
                    dogv = cursor.fetchall()
                    for a in d:
                        self.table.setItem(rowPosition, 2, QTableWidgetItem(str(dogv[0][0])))
                        self.table.setItem(rowPosition, 1, QTableWidgetItem(str(dogv[0][1])))
                    a = "select secondname, namee, midlename, email, numberphone from roditel where id_student = %s"
                    cursor.execute(a, (idd,))
                    rod = cursor.fetchall()
                    if rod != []:
                        for a in d:
                            self.table.setItem(rowPosition, 19, QTableWidgetItem(rod[0][0]))
                            self.table.setItem(rowPosition, 20, QTableWidgetItem(rod[0][1]))
                            self.table.setItem(rowPosition, 21, QTableWidgetItem(rod[0][2]))
                            self.table.setItem(rowPosition, 22, QTableWidgetItem(rod[0][3]))
                            self.table.setItem(rowPosition, 23, QTableWidgetItem(rod[0][4]))
                    else:
                        self.table.setItem(rowPosition, 19, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 20, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 21, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 22, QTableWidgetItem("-"))
                        self.table.setItem(rowPosition, 23, QTableWidgetItem("-"))
                    secondName = str(i[1])
                    name = str(i[2])
                    midleName = str(i[3])
                    phone = str(i[5])
                    emaill = str(i[4])
                    propiska = str(i[8])
                    projivanie = str(i[9])
                    idSch = str(i[11])
                    baza = str(i[13])
                    srednOcen = str(i[15])
                    srednOcenAtt = str(i[16])
                    self.table.setItem(rowPosition, 0, QTableWidgetItem(str(idd)))
                    self.table.setItem(rowPosition, 3, QTableWidgetItem(baza))
                    self.table.setItem(rowPosition, 4, QTableWidgetItem(secondName))
                    self.table.setItem(rowPosition, 5, QTableWidgetItem(name))
                    self.table.setItem(rowPosition, 6, QTableWidgetItem(midleName))
                    self.table.setItem(rowPosition, 12, QTableWidgetItem(srednOcen))
                    self.table.setItem(rowPosition, 13, QTableWidgetItem(srednOcenAtt))
                    self.table.setItem(rowPosition, 14, QTableWidgetItem(idSch))
                    self.table.setItem(rowPosition, 15, QTableWidgetItem(phone))
                    self.table.setItem(rowPosition, 16, QTableWidgetItem(emaill))
                    self.table.setItem(rowPosition, 17, QTableWidgetItem(propiska))
                    self.table.setItem(rowPosition, 18, QTableWidgetItem(projivanie))
        except Error as e:
            print(e)
            connection.rollback()
            connection.close()

    def Back(self):
        self.w = main.WindowMain()
        self.w.showMaximized()
        self.close()

    def Pay(self):
        self.w = Oplata.Oplata()
        self.w.showMaximized()
        