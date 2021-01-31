# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaymentDetails.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_paymentDetailsWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 200)
        self.dialog = Dialog
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.userLabel = QtWidgets.QLabel(Dialog)
        self.userLabel.setObjectName("userLabel")
        self.verticalLayout.addWidget(self.userLabel)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(310)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.__connect()
        self.__displayData()

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Detale transferu"))
        self.userLabel.setText(_translate("Dialog", "TextLabel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Tytuł"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Kwota"))
        self.closeButton.setText(_translate("Dialog", "Zamknij"))

    def __displayData(self):
        self.userLabel.setText(self.name + " za okres " + self.date)
        self.tableWidget.setRowCount(len(self.paymentData))
        idx = 0
        for data in self.paymentData:
            title, value = data
            item = QTableWidgetItem()
            item.setText(title)
            item.setFlags(item.flags() & (~(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)))
            self.tableWidget.setItem(idx, 0, item)
            item = QTableWidgetItem()
            item.setText(str(value))
            item.setFlags(item.flags() & (~(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)))
            self.tableWidget.setItem(idx, 1, item)
            idx = idx + 1

    def __close(self):
        self.dialog.close()

    def __connect(self):
        self.closeButton.clicked.connect(self.__close)

    def __init__(self, userId, name, date, paymentData):
        self.name = name
        self.userId = userId
        self.date = date
        self.paymentData = paymentData
