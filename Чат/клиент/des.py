# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
# Created by: PyQt5 UI code generator 5.14.2

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 461, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 431, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"border: 1px solid black;\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 330, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 280, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 280, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 230, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 123, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 20, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 70, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 184, 431, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Очистить"))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))
        self.pushButton_2.setText(_translate("MainWindow", "Подключится"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Текст сообщения.."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Чат"))
        self.pushButton_5.setText(_translate("MainWindow", "Сгенерировать данные для подключения"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Адрес сервера.."))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Порт сервера.."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Настройки"))
