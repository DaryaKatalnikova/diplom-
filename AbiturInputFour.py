import sys, AbiturInputThree, OpekunBlankTwo, End
from PyQt6.QtGui     import *
from PyQt6.QtCore    import *
from PyQt6.QtWidgets import *

class WindowInputFour(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Академическая Школа Информационных Технологий")
        self.initUI()
        self.resize(QSize(500, 400))

    def initUI(self):
        self.labelNameBlank = QLabel('Бланк для абитуриента', self)
        self.labelNameBlank.setStyleSheet(
            "font-size: 20px;"
        )

        self.labelPropiska = QLabel('Укажите адрес прописки         ' , self)
        self.labelPropiska.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxPropiska = QLineEdit(self)
        self.textboxPropiska.setStyleSheet(
            "font-size: 20px;"
        )

        self.labelProjivanie = QLabel('Укажите адрес \nфактического проживания    ', self)
        self.labelProjivanie.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxProjivanie = QLineEdit(self)
        self.textboxProjivanie.setStyleSheet(
            "font-size: 20px;"
        )

        self.labelObrazovanie = QLabel('Предыдущая \nобразвательная организация', self)
        self.labelObrazovanie.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxObrazovanie = QLineEdit(self)
        self.textboxObrazovanie.setStyleSheet(
            "font-size: 20px;"
        )

        self.labelEmail = QLabel('Укжаите ваш Email                    ', self)
        self.labelEmail.setStyleSheet(
            "font-size: 20px;"
        )
        self.textboxEmail = QLineEdit(self)
        self.textboxEmail.setStyleSheet(
            "font-size: 20px;"
        )

        self.CheckOplata = QCheckBox(
            'Если абитуриент будет оплачивать учебу самостоятельно, \nто необходимо поставить галочку', self)
        self.CheckOplata.setStyleSheet(
            "font-size: 20px;"
        )

        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonBack.clicked.connect(self.Back)


        self.buttonNext = QPushButton('Завершить', self)
        self.buttonNext.setStyleSheet(
            "font-size: 20px;"
        )
        self.buttonNext.clicked.connect(self.Next)

        self.labelStep = QLabel('Шаг 4 из 4 ', self)
        self.labelStep.setStyleSheet(
            "font-size: 20px;"
        )

        layout = QGridLayout()

        layout.addWidget(self.labelNameBlank, 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.setRowStretch(0, 1)
        layout.addWidget(self.labelPropiska, 1, 0, 2, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.textboxPropiska, 1, 1, 2, 1)
        layout.setRowStretch(1, 1)
        layout.addWidget(self.labelProjivanie, 2, 0, 2, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.textboxProjivanie, 2, 1, 2, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.addWidget(self.labelObrazovanie, 3, 0, 2, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.textboxObrazovanie, 3, 1, 2, 1)
        layout.setRowStretch(3, 1)
        layout.addWidget(self.CheckOplata, 5, 1, 2, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.labelEmail, 4, 0, 2, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.textboxEmail, 4, 1, 2, 1)
        layout.setRowStretch(4, 1)
        layout.addWidget(self.buttonBack, 6, 0, 2, 1)
        layout.setRowStretch(5, 1)
        layout.addWidget(self.labelStep, 6, 1, 2, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.buttonNext, 6, 3, 2, 1)
        layout.setRowStretch(6, 1)
        self.setLayout(layout)

    def Next(self):
        if self.CheckOplata.isChecked():
            checkin = "Абитуриент оплачивает обучение самостоятельно"
        else:
            checkin = "Представитель абитуриента опалчивает обучение"

        FIO = "\n" + self.textboxEmail.text() + '\n' + self.textboxPropiska.text() + '\n' + self.textboxProjivanie.text() + '\n' + self.textboxObrazovanie.text() + '\n' + checkin
        f = open('fio.txt', 'a', encoding="utf-16")
        f.write(FIO)
        if self.CheckOplata.isChecked():
            self.w = End.WindowEnd()
            self.w.showMaximized()
            self.close()
        else:
            self.w = OpekunBlankTwo.WindowOpekunBlankTwo()
            self.w.showMaximized()
            self.close()

    def Back(self):
        self.w = AbiturInputThree.WindowInputThree()
        self.w.showMaximized()
        self.close()