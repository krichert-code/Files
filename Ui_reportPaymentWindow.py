# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportPaymentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from paymants import Payments
from Ui_paymentDetailsWindow import Ui_paymentDetailsWindow


class Ui_reportPaymentWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(658, 534)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(12)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.filterTable = QtWidgets.QTableWidget(Form)
        self.filterTable.setObjectName("filterTable")
        self.filterTable.setColumnCount(14)
        self.filterTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(13, item)
        self.filterTable.horizontalHeader().setDefaultSectionSize(180)
        self.filterTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.filterTable)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Raport płatności"))
        self.label.setText(_translate("Form", "Raport za ilość miesięcy :"))
        self.filterTable.setSortingEnabled(True)
        item = self.filterTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Użytkownik"))
        item = self.filterTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(12)
        item.setText(_translate("Form", "Nowa kolumna"))
        item = self.filterTable.horizontalHeaderItem(13)
        item.setText(_translate("Form", "userId"))


    def __refreshReport(self):
        data = Payments()
        userData = data.getPaymentsForLastMonths(self.spinBox.value() - 1)
        header = data.getPaymentsMonths()

        self.filterTable.setSortingEnabled(False)

        self.filterTable.setColumnHidden(0, False)
        for idx in range(1, self.filterTable.columnCount()):
            if idx > len(header):
                self.filterTable.setColumnHidden(idx, True)
            else:
                self.filterTable.setColumnHidden(idx, False)

        idx = 0
        for headerItem in header:
            item = self.filterTable.horizontalHeaderItem(idx+1)
            item.setText(headerItem)
            self.filterTable.setHorizontalHeaderItem(idx+1, item)
            idx = idx + 1

        self.filterTable.setRowCount(len(userData))
        idx = 0
        for key in userData:
            userId, name = key
            values = userData[key]
            item = QTableWidgetItem()
            item.setText(name)
            item.setFlags(item.flags() & (~(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)))
            self.filterTable.setItem(idx, 0, item)

            item = QTableWidgetItem()
            item.setText(str(userId))
            self.filterTable.setItem(idx, 13, item)

            col = 1
            for value in values:
                item = QTableWidgetItem()
                item.setText(str(value))

                item.setFlags(item.flags() & (~(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable)))
                if value == 0:
                    item.setBackground(QtGui.QColor(230,0,0))
                else:
                    item.setBackground(QtGui.QColor(0, 200, 0))

                self.filterTable.setItem(idx, col, item)
                col = col + 1
            idx = idx + 1

        self.filterTable.setSortingEnabled(True)

    def __paymentDetails(self):
        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        name = self.filterTable.item(self.filterTable.currentRow(),0).text()
        userId = self.filterTable.item(self.filterTable.currentRow(), 13).text()
        date = self.filterTable.horizontalHeaderItem(self.filterTable.currentColumn()).text()
        ui = Ui_paymentDetailsWindow(userId, name, date, Payments().getPamentsByUserAndDate(userId, date))
        ui.setupUi(Dialog)
        Dialog.exec_()

    def ret(self):
        return self.reportWindow

    def __init__(self):
        self.reportWindow = QtWidgets.QWidget()
        self.setupUi(self.reportWindow)
        self.spinBox.valueChanged.connect(self.__refreshReport)
        self.filterTable.doubleClicked.connect(self.__paymentDetails)

        for idx in range(0, self.filterTable.columnCount()):
            self.filterTable.setColumnHidden(idx, True)
        self.__refreshReport()


