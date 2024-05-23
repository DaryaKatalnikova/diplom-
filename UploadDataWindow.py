from PyQt6.QtWidgets import *
import main, onDataBase
from mysql.connector import Error
from main import *

connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "EducationPayTracker")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


class UploadData(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EducationPayTracker-Upload-Data-Window")
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

        # Текст для изменения
        self.lineupload = QLineEdit(self)
        self.lineupload.setPlaceholderText('Введите данные...')

        # Кнопка добавить данные
        self.btn_upload_data = QPushButton('Добавить данные в ячейку', self)
        self.btn_upload_data.clicked.connect(self.upload_data)

        # Кнопка назад
        self.btn_back = QPushButton('Вернуться в главное окно', self)
        self.btn_back.clicked.connect(self.BackMainWindow)

        # Сетка
        upload_layout = QGridLayout()
        upload_layout.addWidget(self.lineupload, 0, 2)
        upload_layout.addWidget(self.btn_upload_data, 1, 3)
        upload_layout.addWidget(self.btn_back, 1, 0)
        upload_layout.setRowStretch(0, 1)
        self.setLayout(upload_layout)
    
    # Функция назад в меню
    def BackMainWindow(self):
        self.o = main.WindowMain()
        self.o.show()
        self.close()
    
    # Функция перезаписи данных
    def upload_data(self):
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "EducationPayTracker")
        cursor = connection.cursor()

        textedit = self.lineupload.text()
        file = open("G:\Diplomchik2\EducationPayTrackerNEW\dataindex", "r")

        data = str(file.read()).split(',')
        dataROWint = int(data[0]) + 1
        dataCOLUMNint = int(data[1])

        if dataCOLUMNint == 1:
            cursor = connection.cursor()
            
            zapis = (textedit, dataROWint)
            zaprosName = "UPDATE students SET fio = %s WHERE id_students = %s"
            
            cursor.execute(zaprosName, zapis)
            connection.commit()

        elif dataCOLUMNint == 2:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosGroup = "UPDATE students SET numbergroup = %s WHERE id_students = %s"
            
            cursor.execute(zaprosGroup, zapis)
            connection.commit()

        elif dataCOLUMNint == 3:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosTypePlace = "UPDATE students SET formobuch = %s WHERE id_students = %s"
            
            cursor.execute(zaprosTypePlace, zapis)
            connection.commit()

        elif dataCOLUMNint == 4:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosContractNubmer = "UPDATE contracts SET contractnumber = %s WHERE id_students = %s"
            
            cursor.execute(zaprosContractNubmer, zapis)
            connection.commit()

        elif dataCOLUMNint == 5:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosAcademicYear = "UPDATE students SET academicyear = %s WHERE id_students = %s"
            
            cursor.execute(zaprosAcademicYear, zapis)
            connection.commit()

        elif dataCOLUMNint == 6:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosYearSum = "UPDATE students SET yearsum = %s WHERE id_students = %s"
            
            cursor.execute(zaprosYearSum, zapis)
            connection.commit()

        elif dataCOLUMNint == 8:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosOrderSum = "UPDATE ordercost SET sumordercost = %s WHERE id_students = %s"
            
            cursor.execute(zaprosOrderSum, zapis)
            connection.commit()

        elif dataCOLUMNint == 9:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosPlanSum = "UPDATE students SET plansum = %s WHERE id_students = %s"
            
            cursor.execute(zaprosPlanSum, zapis)
            connection.commit()

        elif dataCOLUMNint == 10:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosPlanDate = "UPDATE students SET plandate = %s WHERE id_students = %s"
            
            cursor.execute(zaprosPlanDate, zapis)
            connection.commit()

        elif dataCOLUMNint == 11:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosFactSum = "UPDATE pay SET sumpay = %s WHERE id_students = %s"
            
            cursor.execute(zaprosFactSum, zapis)
            connection.commit()

        elif dataCOLUMNint == 12:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosFactDate = "UPDATE pay SET datepay = %s WHERE id_students = %s"
            
            cursor.execute(zaprosFactDate, zapis)
            connection.commit()

        elif dataCOLUMNint == 13:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosStatementSum = "UPDATE statements SET statementsum = %s WHERE id_students = %s"
            
            cursor.execute(zaprosStatementSum, zapis)
            connection.commit()

        elif dataCOLUMNint == 14:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosStatementDate = "UPDATE statements SET statementdate = %s WHERE id_students = %s"
            
            cursor.execute(zaprosStatementDate, zapis)
            connection.commit()

        elif dataCOLUMNint == 15:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosDebt = "UPDATE students SET debt = %s WHERE id_students = %s"
            
            cursor.execute(zaprosDebt, zapis)
            connection.commit()

        elif dataCOLUMNint == 16:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosOverpayment = "UPDATE students SET overpayment = %s WHERE id_students = %s"
            
            cursor.execute(zaprosOverpayment, zapis)
            connection.commit()

        elif dataCOLUMNint == 17:
            cursor = connection.cursor()
            
            zapis = (textedit, dataROWint)
            zaprosPayer = "UPDATE students SET payer = %s WHERE id_students = %s"
            
            cursor.execute(zaprosPayer, zapis)
            connection.commit()

        elif dataCOLUMNint == 18:
            cursor = connection.cursor()

            zapis = (textedit, dataROWint)
            zaprosPayer = "UPDATE students SET Note = %s WHERE id_students = %s"
            
            cursor.execute(zaprosPayer, zapis)
            connection.commit()