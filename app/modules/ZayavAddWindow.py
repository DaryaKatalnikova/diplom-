from PyQt6.QtWidgets import *
from app.modules import onDataBase
from app import main
from datetime import date
from mysql.connector import Error


connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "EducationPayTracker")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

selectOC = "SELECT * FROM statements"
centers = execute_read_query(connection, selectOC)
if centers ==[]:
    id_sm = 1
else:
    id_sm = centers[len(centers)-1][0]
    id_sm += 1

class AddWindowZayav(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EducationPayTracker-Add-New-Zayavlenie")
        #min_height = 480
        #min_weight = 480
        #self.setMinimumSize(min_weight, min_height)
        self.setGeometry(100, 100, 700, 250)
        self.setStyleSheet('''
                    QWidget{
                        background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(217, 217, 217, 1), stop:0.427447 rgba(217, 217, 217, 1), stop:1 rgba(217, 217, 217, 1));
                        color: #D9D9D9;
                    }
                    QComboBox{
                        border: 1px solid #424242;
                        border-raduis 4px;
                        padding-left: 10px;
                        color: black;
                    }
                    QComboBox::on{
                        border: 4px solid #60669B;
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
                        background-color: #60669B;
                    }
                    QComboBox::down-arrow{
                        width: 12px;
                        heigth: 12px;
                        margin-right 15px;
                    }
                    QLabel{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        color: #D9D9D9;
                    }
                    QDateEdit{
                        font-family: Ubunty Mono;
                        font-size: 14px;
                        background-color: #fff;
                        color: black;
                    }
                    QMenuBar {
                        color: #000000;
                        border: 1px solid #424242;
                        border-radius: 7px;
                    }
                    QMenuBar::item {
                         spacing: 3px;
                         padding: 1px 4px;
                         background: transparent;
                         border-radius: 4px;
                     }
                    QLineEdit{
                        background-color: rgba(255, 255, 255, 30);
                        border: 1px solid #424242;
                        border-radius: 7px;
                        color: black;
                        font-weight: light;
                        font-size: 12pt;
                        padding-left: 10px;
                    }
                    QPushButton{
                        color: black;
                        background-color: rgba(255, 255, 255, 30);
                        border: 1px solid #424242;
                        border-radius: 7px;
                        width: 230px;
                        height: 30px;
                    }
                    QPushButton:hover{
                        background-color: rgba(255, 255, 255, 40);
                    }
                    QPushButton:pressed{
                        background-color: rgba(255, 255, 255, 70);
                    }
                    QTableWidget{
                        color: black;
                        border: 1px solid #424242;
                        border-bottom-right-radius: 7px;
                        border-bottom-left-radius: 7px;
                    }
                    QHeaderView::section{
                        Font-size:14px;
                        Font-family: "Microsoft YaHei";
                        Color: #FFFFFF;
                        Background:#60669B;
                        Border:none;
                        Text-align:left;
                        Min-height: 49px;
                        max-height:49px; 
                        Margin-left:0px;
                        Padding-left: 0px;
                    }
                ''')
        self.initUI()

    def initUI(self):

        # Основные кнопки
        self.button_add_zayav = QPushButton('Добавить Заявление', self)
        self.button_back_main_window_zayav = QPushButton('Вернуться на главное окно', self)
        self.naz_zayav = QLineEdit(self)
        self.sum_zayav = QLineEdit(self)
        self.naz_zayav.setPlaceholderText('Введите название Заявления')
        self.sum_zayav.setPlaceholderText('Введите сумму Заявления')
        self.date_zayav = QDateEdit(self)
        self.combo_student = QComboBox(self)

        # Сетка
        zayav_layout = QGridLayout()
        zayav_layout.addWidget(self.naz_zayav, 0, 3)
        zayav_layout.addWidget(self.sum_zayav, 1, 3)
        zayav_layout.addWidget(self.date_zayav, 2, 3)
        zayav_layout.addWidget(self.combo_student, 3, 3)
        zayav_layout.addWidget(self.button_back_main_window_zayav, 4, 2)
        zayav_layout.addWidget(self.button_add_zayav, 4, 4)
        self.setLayout(zayav_layout)


        self.button_back_main_window_zayav.clicked.connect(self.BackMainWindow)
        self.button_add_zayav.clicked.connect(self.Add_Zayav)

        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "EducationPayTracker")
        select_sotrs = "SELECT * FROM students"
        sotrs = execute_read_query(connection, select_sotrs)
        lSotrs = list()
        for s in sotrs:
            lSotrs.append(str(s).split(',')[1][2:len(str(s).split(',')[1]) - 1])
        self.combo_student.addItems(lSotrs)
        

    def BackMainWindow(self):
        self.o = main.WindowMain()
        self.o.show()
        self.close()
    
    def Add_Zayav(self):
        lineEdits = self.findChildren(QLineEdit)
        text = ''
        for lineEdit in lineEdits:
            if not lineEdit.text():
                text = f'Заполните все поля!\n'
        if text:
            msg = QMessageBox.information(self, 'Внимание', text)
        else:
            connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "EducationPayTracker")
            cursor = connection.cursor()
            nazzayav = " ".join(self.naz_zayav.text().split()).title()
            sumzayav = " ".join(self.sum_zayav.text().split()).title()
            yearB = int(self.date_zayav.date().toString("yyyy.MM.dd").split('.')[0])
            monthB = int(self.date_zayav.date().toString("yyyy.MM.dd").split('.')[1])
            dayB = int(self.date_zayav.date().toString("yyyy.MM.dd").split('.')[2])
            datezayav = date(yearB, monthB, dayB)

            a = self.combo_student.currentText()
            comboboxzayav = "SELECT id_students FROM students WHERE fio = '%s'" % (a)
            b = execute_read_query(connection, comboboxzayav)
            zapis = (id_sm, nazzayav, sumzayav, datezayav, b[0][0])
            newzayav = "INSERT INTO statements (id_statements, nazstatement, statementsum, statementdate, id_students) values (%s, %s, %s, %s, %s)"

            cursor.execute(newzayav, zapis)
            connection.commit()
            connection.close()