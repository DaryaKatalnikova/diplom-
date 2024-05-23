from PyQt6.QtWidgets import *
import main, onDataBase
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

selectOC = "SELECT * FROM ordercost"
centers = execute_read_query(connection, selectOC)
if centers ==[]:
    id_oc = 1
else:
    id_oc = centers[len(centers)-1][0]
    id_oc += 1

class AddWindowPrikaz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EducationPayTracker-Add-New-Prikaz")
        #min_height = 480
        #min_weight = 480
        #self.setMinimumSize(min_weight, min_height)
        self.setGeometry(100, 100, 700, 250)
        self.setStyleSheet('''
                    QWidget{
                        background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(217, 217, 217, 1), stop:0.427447 rgba(217, 217, 217, 1), stop:1 rgba(217, 217, 217, 1));
                        color: #D9D9D9;
                    }
                    QLabel{
                        font-family: Ubuntu Mono;
                        font-size: 18px;
                        color: #D9D9D9;
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
        self.button_add_prikaz = QPushButton('Добавить Приказ', self)
        self.button_back_main_window_prikaz = QPushButton('Вернуться на главное окно', self)
        self.naz_prikaz = QLineEdit(self)
        self.sum_prikaz = QLineEdit(self)
        self.naz_prikaz.setPlaceholderText('Введите название Приказа')
        self.sum_prikaz.setPlaceholderText('Введите Сумму по Приказу')

        # Сетка
        prikaz_layout = QGridLayout()
        prikaz_layout.addWidget(self.naz_prikaz, 0, 3)
        prikaz_layout.addWidget(self.sum_prikaz, 1, 3)
        prikaz_layout.addWidget(self.button_back_main_window_prikaz, 2, 2)
        prikaz_layout.addWidget(self.button_add_prikaz, 2, 4)
        prikaz_layout.setRowStretch(0, 1)
        self.setLayout(prikaz_layout)

        self.button_back_main_window_prikaz.clicked.connect(self.BackMainWindow)
        self.button_add_prikaz.clicked.connect(self.Add_Prikaz)

    def BackMainWindow(self):
        self.o = main.WindowMain()
        self.o.show()
        self.close()

    def Add_Prikaz(self):
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
            nazprikaz = " ".join(self.naz_prikaz.text().split()).title()
            sumprikaz = " ".join(self.sum_prikaz.text().split()).title()
            zapis = (id_oc, nazprikaz, sumprikaz)
            newprikaz = "INSERT INTO ordercost (id_ordercost, nazordercost, sumordercost) values (%s, %s, %s)"

            cursor.execute(newprikaz, zapis)
            connection.commit()
            connection.close()