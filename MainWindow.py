# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import textwrap

size = random.randint(3, 5)
n = random.randint(50, 53)
m = random.randint(300, 400)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 609)
        MainWindow.setStyleSheet("*{\n"
                                 "background-image: url(/Users/denysgashaw/Desktop/КПИ/3 курс/6labcipher/img/cryptoimg.png);\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    color: black;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 40, 451, 491))
        self.textEdit.setStyleSheet("#textEdit{\n"
                                    "    background: grey;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 120, 281, 31))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 180, 281, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 420, 121, 51))
        self.pushButton.setStyleSheet("color: white;\n"
                                      "border-radius: 20px;\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 420, 121, 51))
        self.pushButton_2.setStyleSheet("color: white;\n"
                                        "border-radius: 20px;\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 370, 161, 51))
        self.pushButton_3.setStyleSheet("\n"
                                        "color: white;\n"
                                        "border-radius: 20px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(270, 20, 71, 51))
        self.toolButton.setStyleSheet("border-radius: 20px;")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/key-emoji1.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 240, 281, 91))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(221, 461, 161, 51))
        self.pushButton_4.setStyleSheet("color: white;\n"
                                        "border-radius: 15px;")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #logic
        self.pushButton_3.clicked.connect(lambda: self.public_key(n, m, size))
        self.pushButton.clicked.connect(self.encryption)
        self.pushButton_2.clicked.connect(self.decryption)
        self.pushButton_4.clicked.connect(self.clear)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate(
            "MainWindow", "Введите начальный текст"))
        self.lineEdit_3.setPlaceholderText(
            _translate("MainWindow", "Открытый ключ"))
        self.pushButton.setText(_translate("MainWindow", "Зашифровать"))
        self.pushButton_2.setText(_translate("MainWindow", "Разшифровать"))
        self.pushButton_3.setText(_translate(
            "MainWindow", "Сгенерировать ключи"))
        self.lineEdit_2.setPlaceholderText(
            _translate("MainWindow", "Результат"))
        self.pushButton_4.setText(_translate("MainWindow", "Очистить поля"))

    def generate_super_increasing_knapsack(self, size):
        first = random.randint(2, 2+size)
        knapsack = [first]
        sum = first
        for _ in range(size-1):
            element = sum + random.randint(1, size)
            knapsack.append(element)
            sum += element
        print("Это ваш приватный ключ:", knapsack)
        return knapsack

    def public_key(self, n, m, size):
        private_key = self.generate_super_increasing_knapsack(size)
        suma = sum(private_key)
        if suma >= m:
            raise AttributeError(
                'm должно быть больше чем сумма всех элементов приватного ключа')
        public_key_int = [(k*n) % m for k in private_key]
        # конвертируем лист интов в строку
        public_key_string = " ".join(map(str, public_key_int))
        print("N = {} и M = {}".format(n, m))
        self.lineEdit_3.setText(public_key_string)

    def plain_text_to_binary(self):
        plain_text = self.lineEdit.text()
        binary_str = ''.join(format(ord(x), 'b') for x in plain_text)
        binary_str = textwrap.wrap(binary_str, size)
        last_element = list(binary_str.pop())
        while len(last_element) < size:
            last_element.insert(0, '0')
        new_string = ''.join(last_element)
        binary_str.append(new_string)
        print(binary_str)
        return binary_str

    def type_convertation(self, public_key):
        splited_string = public_key.split(" ")
        splited_int_list = [int(d) for d in splited_string]
        return splited_int_list

    def encryption(self):
        public_key = self.lineEdit_3.text()
        public_key = self.type_convertation(public_key)
        binary_str = self.plain_text_to_binary()
        binary_list = [list(d) for d in binary_str]
        number_list = [[int(y) for y in x] for x in binary_list]
        print(binary_list)
        result = []
        for i in range(len(number_list)):
            result.append(0)

        for i in range(len(number_list)):
            for j in range(len(public_key)):
                result[i] += public_key[j] * number_list[i][j]
        result = str(result)
        self.lineEdit_2.setText(result)

    def decryption(self):
        text_for_decryption = self.lineEdit.text()
        self.lineEdit_2.setText(text_for_decryption)
        
    def clear(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
