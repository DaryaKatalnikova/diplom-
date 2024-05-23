import sys, main
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *

import Output


class WindowLoginAdm(QWidget):
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
        self.setFixedSize(QSize(700, 500))

    def initUI(self):
        self.labelLogin = QLabel('Логин:', self)
        self.labelLogin.move(50, 50)
        self.labelLogin.resize(100, 40)
        self.labelLogin.setStyleSheet(
            "font-size: 25px;"
        )
        self.textboxLogin = QLineEdit(self)
        self.textboxLogin.move(200, 50)
        self.textboxLogin.resize(300 ,40)

        self.labelPassword = QLabel('Пароль:', self)
        self.labelPassword.move(50, 100)
        self.labelPassword.resize(125, 40)
        self.labelPassword.setStyleSheet(
            "font-size: 25px;"
        )
        self.textboxPassword = QLineEdit(self)
        self.textboxPassword.move(200, 100)
        self.textboxPassword.resize(300, 40)

        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.move(250, 330)
        self.buttonBack.resize(200, 60)
        self.buttonBack.clicked.connect(self.Back)
        self.buttonBack.setStyleSheet(
            "font-size: 25px;"
        )

        self.buttonLogIn = QPushButton('Войти', self)
        self.buttonLogIn.move(250, 250)
        self.buttonLogIn.resize(200, 60)
        self.buttonLogIn.clicked.connect(self.LogIn)
        self.buttonLogIn.setStyleSheet(
            "font-size: 25px;"
        )


    def Back(self):
        self.w = main.WindowMain()
        self.w.showMaximized()
        self.close()

    def LogIn(self):
        # тут условие на логин и пароль
        self.w = Output.WindowOutput()
        self.w.showMaximized()
        self.close()


