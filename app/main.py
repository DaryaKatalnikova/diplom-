import sys



from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
class WindowMain(QMainWindow):
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
                ''')
        self.initUI()
        self.setWindowIcon(QIcon('2.png'))
        self.pixmap = QPixmap('3.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),self.pixmap.height())

    def initUI(self):
        self.buttonAbiturient = QPushButton('Абитуриент', self)
        self.buttonAbiturient.clicked.connect(self.AbiturInOne)
        self.buttonAbiturient.setFixedSize(500, 100)
        self.buttonAbiturient.setStyleSheet(
            "font-size: 40px;"
        )


        self.buttonAdmin = QPushButton('Админ', self)
        self.buttonAdmin.clicked.connect(self.LogAdmin)
        self.buttonAdmin.setFixedSize(500, 100)
        self.buttonAdmin.setStyleSheet(
            "font-size: 40px;"
        )

        layout = QVBoxLayout()
        layout.addWidget(self.buttonAbiturient)
        layout.addWidget(self.buttonAdmin)
        layout.setContentsMargins(500, 50, 500, 50)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def AbiturInOne(self):
        from app.modules import AbiturInputOne
        self.w = AbiturInputOne.WindowInputOne()
        self.w.showMaximized()
        self.close()

    def LogAdmin(self):
        from app.modules import LoginAdm
        self.w = LoginAdm.WindowLoginAdm()
        self.w.show()
        self.close()


app = QApplication(sys.argv)
window = WindowMain()
window.showMaximized()

app.exec()