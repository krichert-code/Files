# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportUserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from transfer import Transfer, Record
from users import Users


class Ui_importUserWindow(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(627, 492)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importButton = QtWidgets.QPushButton(Dialog)
        self.importButton.setObjectName("importButton")
        self.horizontalLayout.addWidget(self.importButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancleButton = QtWidgets.QPushButton(Dialog)
        self.cancleButton.setObjectName("cancleButton")
        self.horizontalLayout.addWidget(self.cancleButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.__connect()
        self.__displayData()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Użytkownicy  - importowanie"))
        self.label.setText(_translate("Dialog", "Wybierz użytkowników do zaimportowania :"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Użytkownik"))
        self.importButton.setText(_translate("Dialog", "Importuj"))
        self.cancleButton.setText(_translate("Dialog", "Anuluj"))


    def __close(self):
        self.dialog.close()

    def __importUsers(self):
        rowIdx = 0
        users = Users()
        for userFromFile in self.usersFromFile:
            userId = -1
            chkBoxItem = self.tableWidget.item(rowIdx, 1)
            if chkBoxItem.checkState() == QtCore.Qt.Checked:
                found, userId = users.findUserIdByAccount(userFromFile.getAcountNumber())
                if not found:
                    userId = users.addNewUser(userFromFile.getUserName(), "")
                    users.addBankAccount(userId, userFromFile.getAcountNumber())
            rowIdx = rowIdx + 1

        users.storeUsedData(self.__progressBar)
        self.__importDataOccur = True
        self.dialog.close()


    def __connect(self):
        self.cancleButton.clicked.connect(self.__close)
        self.importButton.clicked.connect(self.__importUsers)

    def __displayData(self):
        self.tableWidget.setRowCount(1)
        rowCount = 0
        for userItem in self.usersFromFile:
            name = QTableWidgetItem()
            name.setText(userItem.getUserName())
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Checked)

            self.tableWidget.setRowCount(rowCount+1)
            self.tableWidget.setItem(rowCount, 0, name)
            self.tableWidget.setItem(rowCount, 1, chkBoxItem)
            rowCount = rowCount + 1

    def importPerformed(self):
        return self.__importDataOccur

    def __init__(self, usersFromFile, progressBar):
        self.usersFromFile = usersFromFile
        self.__importDataOccur = False
        self.__progressBar = progressBar