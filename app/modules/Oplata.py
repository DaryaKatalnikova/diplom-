from app.modules import FileAddNewOplata
#import PrikaziAddWindow
#import ZayavAddWindow
#import UploadDataWindow
import sys
import onDataBase
import datetime

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from mysql.connector import Error


connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbasit")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result   
    except Error as e:
        print(f"The error '{e}' occurred")


class Oplata(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Академиеская школа информационных технологий")
        min_height = 720
        min_weight = 1280
        self.setMinimumSize(min_weight, min_height)
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
                        font-size: 16px;
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
        self.initUi()

    def initUi(self):

        self.pixmap = QPixmap('image/logo.png')
        self.labelpix = QLabel(self)
        self.labelpix.setPixmap(self.pixmap)
        self.labelpix.setStyleSheet('''background-color: transparent;''')

        hbox1 = QHBoxLayout()
        self.addfile = QPushButton("Добавить новый\nфайл оплат", self)
        self.addfile.setFixedSize(250, 70)
        self.addfile.setStyleSheet("font-size: 25px;")
        self.addfile.clicked.connect(self.open_file_add_new_window)
        hbox1.addWidget(self.addfile)
        self.adddate = QPushButton("Добавить новый\nсрок оплаты", self)
        self.adddate.setFixedSize(250, 70)
        self.adddate.setStyleSheet("font-size:25px;")
        hbox1.addWidget(self.adddate)
        #self.adddate.clicked.connect(self.addDate)

        # Строка поиска
        hbox2 = QHBoxLayout()
        self.linepoisk = QLineEdit(self)
        self.linepoisk.setPlaceholderText('Введите ФИО студента, которого нужно найти')
        self.linepoisk.setFixedHeight(50)
        hbox2.addWidget(self.linepoisk)
        self.cancel = QPushButton("X", self)
        self.cancel.setFixedSize(30, 30)
        self.cancel.setStyleSheet("font - size: 18px; backgroud-color: red")
        hbox2.addWidget(self.cancel)
        self.cancel.clicked.connect(self.tableView)
        
        # Кнопка найти студента
        self.btn_poisk = QPushButton('Найти студента', self)
        self.btn_poisk.setStyleSheet("font-size: 25px;")
        self.btn_poisk.clicked.connect(self.FindInDB)

        # Таблица
        self.table = QTableWidget(self)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['ФИО', 'Группа', '№Договора', 'Б/ВБ', 'Плановая дата', 'Плановая Сумма', 'Фактическая дата', 'Сумма', 'Комментарий'])

        # Установка ширины столбцов и кол-во строк
        header = self.table.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.Stretch)
        
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbasit")
        select_sotrs = "SELECT * FROM student"
        sotrs = execute_read_query(connection, select_sotrs)
        lSotrs = list()
        for s in sotrs:
            lSotrs.append(str(s).split(',')[0][1:])
        id_st_data_base = lSotrs[-1]
        id_st = int(id_st_data_base) 
        self.tableView()
        main_layout = QVBoxLayout()
        main_layout.addLayout(hbox1)
        main_layout.addLayout(hbox2)
        main_layout.addWidget(self.labelpix, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.btn_poisk)
        main_layout.addWidget(self.table)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    
    def tableView(self):    # Прогрузка таблицы
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbasit")
        cursor = connection.cursor()
        cursor.execute("SELECT student.secondname, student.namee, student.midlename, UGroup.name_group, dogovor.numberdogovor, dogovor.placeBud, student.id_student FROM student join UGroup on student.id_group=UGroup.id_group join dogovor on student.id_student=dogovor.id_student left join pay on pay.id_student=student.id_student")
        result = list(cursor.fetchall())
        row = 0
        cursor = connection.cursor()
        cursor.execute("SELECT summa_b, summa_vb, plan_date FROM plan_pay limit 1")
        plan_pay = list(cursor.fetchall())
        i = 0
        self.table.setRowCount(len(result))
        while i < len(result):
            cursor = connection.cursor()
            a = int(result[i][6])
            opl = "SELECT pay.pay_date, pay.summa from pay where pay.id_student = '%s'" %(a)
            oplpay = execute_read_query(connection, opl)
            t = 0
            sumopl = 0  
            self.table.setItem(row, 0, QTableWidgetItem(result[i][0] + ' ' + result[i][1] +' '+ result[i][2]))
            self.table.setItem(row, 1, QTableWidgetItem(result[i][3]))
            self.table.setItem(row, 2, QTableWidgetItem(result[i][4]))
            self.table.setItem(row, 3, QTableWidgetItem(result[i][5]))
            self.table.setItem(row, 4, QTableWidgetItem(str(plan_pay[0][2])))
            for j in range(len(oplpay)):
                self.table.setItem(row, 6, QTableWidgetItem(str(oplpay[j][0])))
                self.table.setItem(row, 7, QTableWidgetItem(str(oplpay[j][1])))
                if oplpay[j][1] !=None:
                    sumopl += float(oplpay[j][1])
                row+=1
                t +=1
            if len(oplpay) ==0:
                date_pay = datetime.date.today().isoformat()
            else:
                date_pay = str(oplpay[j-1][0])
            if t!=0:
                print(str(result[i][5]))
                if str(result[i][5]) == 'Бюджет':
                    self.table.setItem((row-1), 5, QTableWidgetItem(str(plan_pay[0][0])))
                    self.Komment(date_pay, float(plan_pay[0][0]), sumopl, row-1)
                else:    
                    self.table.setItem((row-1), 5, QTableWidgetItem(str(plan_pay[0][1])))
                    self.Komment(date_pay, float(plan_pay[0][1]), sumopl, row-1)
            else:
                if str(result[i][5]) == 'Бюджет':
                    self.table.setItem(row, 5, QTableWidgetItem(str(plan_pay[0][0])))
                    self.Komment(date_pay, float(plan_pay[0][0]), sumopl, row-1)
                else:    
                    self.table.setItem(row, 5, QTableWidgetItem(str(plan_pay[0][1])))
                    self.Komment(date_pay, float(plan_pay[0][1]), sumopl, row-1)
                row+=1
            if(len(oplpay) !=1):
                print(a)
                k = i + 1
                while k<len(result):
                    if(int(result[k][6]) == a):
                        print('zxcv')
                        result.pop(k)
                    else:
                        k+=1
            i+=1
        
# Видимо еще одна сетка
        
    def Komment(self, fact_date, plan_sum, fact_sum, row):
        if fact_date == 'None':
            self.table.setItem(row, 8, QTableWidgetItem('Задолженность: ' + str(plan_sum)))
        elif fact_sum<plan_sum:
            #print(2)
            self.table.setItem(row, 8, QTableWidgetItem('Задолженность: ' + str((plan_sum)-(fact_sum))))
        elif fact_sum > plan_sum:
            #print(3)
            self.table.setItem(row, 8, QTableWidgetItem('Переплата: ' + str((fact_sum)-(plan_sum))))
        
        connection.close()
        


        '''
            comboboxQTableYacheika = QComboBox(self)
            for i in range(len(resultorder)):
                comboboxQTableYacheika.addItems(resultorder[i])
            self.table.setItem(row, 8, QTableWidgetItem(str(resultordersum[i][0])))
            self.table.setCellWidget(row, 7, comboboxQTableYacheika)
            row += 1
            '''
        
        # Нажатие на ячейку
        #self.table.cellPressed[int, int].connect(self.clickedRowColumn)
    
    def FindInDB(self):
        connection = onDataBase.create_connection("localhost", "root", "HarryPotterand3", "dbasit")
        cursor = connection.cursor()

        try:
            sn = self.linepoisk.text().split()[0]
            n = self.linepoisk.text().split()[1]
            mn = self.linepoisk.text().split()[2]
            cursor.execute(f"SELECT student.secondname, student.namee, student.midlename, UGroup.name_group, dogovor.numberdogovor, dogovor.placeBud, student.id_student FROM student join UGroup on student.id_group=UGroup.id_group join dogovor on student.id_student=dogovor.id_student left join pay on pay.id_student=student.id_student WHERE secondname LIKE '%{sn}%' and namee LIKE '%{n}%' and midlename LIKE '%{mn}%'")
            results = cursor.fetchall()
            cursor = connection.cursor()
            cursor.execute("SELECT summa_b, summa_vb, plan_date FROM plan_pay limit 1")
            plan_pay = list(cursor.fetchall())
            self.table.clear()
            print(results)
            self.table.setHorizontalHeaderLabels(['ФИО', 'Группа', '№Договора', 'Б/ВБ', 'Плановая дата', 'Плановая Сумма', 'Фактическая дата', 'Сумма', 'Комментарий'])
            self.table.setRowCount(len(results))
            row = 0
            i = 0
            while i < len(results):
                a = int(results[i][6])
                opl = "SELECT pay.pay_date, pay.summa from pay where pay.id_student = '%s'" %(a)
                oplpay = execute_read_query(connection, opl)
                print(oplpay)
                sumopl = 0
                t = 0
                self.table.setItem(row, 0, QTableWidgetItem(results[i][0] + ' ' + results[i][1] +' '+ results[i][2]))
                self.table.setItem(row, 1, QTableWidgetItem(results[i][3]))
                self.table.setItem(row, 2, QTableWidgetItem(results[i][4]))
                self.table.setItem(row, 3, QTableWidgetItem(results[i][5]))
                self.table.setItem(row, 4, QTableWidgetItem(str(plan_pay[0][2])))
                for j in range(len(oplpay)):
                    self.table.setItem(row, 6, QTableWidgetItem(str(oplpay[j][0])))
                    self.table.setItem(row, 7, QTableWidgetItem(str(oplpay[j][1])))
                    if oplpay[j][1] !=None:
                        sumopl += float(oplpay[j][1])
                    row+=1
                    t +=1
                if len(oplpay) ==0:
                    date_pay = datetime.date.today().isoformat()
                else:
                    date_pay = str(oplpay[j-1][0])
                if t!=0:
                    if str(results[i][5]) == 'Бюджет':
                        self.table.setItem((row-1), 5, QTableWidgetItem(str(plan_pay[0][0])))
                        self.Komment(date_pay, float(plan_pay[0][0]), sumopl, row-1)
                    else:    
                        self.table.setItem((row-1), 5, QTableWidgetItem(str(plan_pay[0][1])))
                        self.Komment(date_pay, float(plan_pay[0][1]), sumopl, row-1)
                else:
                    if str(results[i][5]) == 'Бюджет':
                        self.table.setItem(row, 5, QTableWidgetItem(str(plan_pay[0][0])))
                        self.Komment(date_pay, float(plan_pay[0][0]), sumopl, row-1)
                    else:    
                        self.table.setItem(row, 5, QTableWidgetItem(str(plan_pay[0][1])))
                        self.Komment(date_pay, float(plan_pay[0][1]), sumopl, row-1)
                        row+=1
                if(len(oplpay) !=1):
                    k = i + 1
                    while k<len(results):
                        if(int(results[k][6]) == a):
                            results.pop(k)
                        else:
                            k+=1
                i+=1
            header = self.table.horizontalHeader()
            header.setStretchLastSection(True)

        except Error as e:
            print(e)
            connection.rollback()
            connection.close()
        

    # Функция выхода
    def quit(self):
        self.close()

    
    # Функция открытия окна Добавления Файла Оплаты
    
    def open_file_add_new_window(self):
        self.o = FileAddNewOplata.AddWindowOplata()
        self.o.show()  
        self.timer = QTimer()
        self.timer.start(10000)# Интервал в миллисекундах
        self.close()
'''
    # Функция открытия окна Добавления Приказа
    def open_prikazi_add_window(self):
        self.o = PrikaziAddWindow.AddWindowPrikaz()
        self.o.show()
        self.close()
    
    # Функция поиск ячейки и запись в файл
    def clickedRowColumn(self, row, colum):
        yacheika = self.table.currentItem()
        self.o = UploadDataWindow.UploadData()
        self.o.show()
        file = open("dataindex", "w")
        file.write(str(row) + "," + str(colum))
    '''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Oplata()
    window.show()

    app.exec()