# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenu, QMessageBox, QFileDialog

from Ui_importUserWindow import Ui_importUserWindow
from transfer import Transfer
from users import Users


from PyQt5.QtWidgets import QTableWidgetItem


class Ui_userWindow(object):
    def setupUi(self, userWindow):
        userWindow.setObjectName("userWindow")
        userWindow.resize(636, 582)
        self.verticalLayout = QtWidgets.QVBoxLayout(userWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.userTable = QtWidgets.QTableWidget(userWindow)
        self.userTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.userTable.setAcceptDrops(False)
        self.userTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.userTable.setAlternatingRowColors(False)
        self.userTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.userTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.userTable.setRowCount(1)
        self.userTable.setColumnCount(3)
        self.userTable.setObjectName("userTable")
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTable.setHorizontalHeaderItem(2, item)
        self.userTable.horizontalHeader().setDefaultSectionSize(300)
        self.userTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.userTable)
        self.label = QtWidgets.QLabel(userWindow)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.accountTable = QtWidgets.QTableWidget(userWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountTable.sizePolicy().hasHeightForWidth())
        self.accountTable.setSizePolicy(sizePolicy)
        self.accountTable.setMinimumSize(QtCore.QSize(0, 192))
        self.accountTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.accountTable.setRowCount(1)
        self.accountTable.setObjectName("accountTable")
        self.accountTable.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.accountTable.setHorizontalHeaderItem(0, item)
        self.accountTable.horizontalHeader().setVisible(False)
        self.accountTable.horizontalHeader().setDefaultSectionSize(600)
        self.accountTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.accountTable, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(userWindow)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(userWindow)
        QtCore.QMetaObject.connectSlotsByName(userWindow)

    def retranslateUi(self, userWindow):
        _translate = QtCore.QCoreApplication.translate
        userWindow.setWindowTitle(_translate("userWindow", "Użytkownicy"))
        item = self.userTable.horizontalHeaderItem(0)
        item.setText(_translate("userWindow", "Użytkownik"))
        item = self.userTable.horizontalHeaderItem(1)
        item.setText(_translate("userWindow", "Email"))
        item = self.userTable.horizontalHeaderItem(2)
        item.setText(_translate("userWindow", "key"))
        self.label.setText(_translate("userWindow", "Konta bankowe"))
        item = self.accountTable.horizontalHeaderItem(0)
        item.setText(_translate("userWindow", "Numer konta"))
        self.saveButton.setText(_translate("userWindow", "Zapisz zmiany"))

    def ret(self):
        return self.userWindow


    def __displayUsers(self):
        rowCount = 0
        self.userTable.clearSelection()
        self.userTable.setRowCount(self.usersData.getUsersCount())
        self.accountTable.setRowCount(0)
        self.userTable.setSortingEnabled(False)

        for item in self.usersData:
            if item.delete == False:
                name = QTableWidgetItem()
                email = QTableWidgetItem()
                id = QTableWidgetItem()
                name.setText(item.name)
                email.setText(item.email)
                id.setText(str(item.id))
                self.userTable.setItem(rowCount, 0, name)
                self.userTable.setItem(rowCount, 1, email)
                self.userTable.setItem(rowCount, 2, id)
                rowCount = rowCount + 1
        self.userTable.setRowCount(rowCount)
        self.userTable.setSortingEnabled(True)


    def contextMenuAccountTable(self, position):
        menu = QMenu()
        addAction = menu.addAction("Dodaj konto")
        deleteAction = menu.addAction("Usuń konto")
        action = menu.exec_(self.accountTable.mapToGlobal(position))

        if len(self.userTable.selectedIndexes()) > 0:
            id = int(self.userTable.item(self.userTable.currentIndex().row(), 2).text())

            if action == addAction:
                self.usersData.addBankAccount(id)
                self.__displayAccounts()

            if action == deleteAction:
                if len(self.accountTable.selectedIndexes()) > 0:
                    self.usersData.delBankAccount(id, self.accountTable.currentIndex().row())
                    self.__displayAccounts()


    def contextMenuUserTable(self, position):
        menu = QMenu()
        addAction = menu.addAction("Dodaj użytkownika")
        addFromFileAction = menu.addAction("Dodaj użytkowników z pliku")
        deleteAction = menu.addAction("Usuń użytkownika")
        action = menu.exec_(self.userTable.mapToGlobal(position))
        if action == addAction:
            self.usersData.addNewUser()
            self.__displayUsers()

        if action == deleteAction:
            if len(self.userTable.selectedIndexes()) > 0:
                id = int(self.userTable.item(self.userTable.currentIndex().row(), 2).text())
                self.usersData.delUser(id)
                self.__displayUsers()

        if action == addFromFileAction:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                      "CSV Files (*.csv)", options=options)
            if fileName != "":
                self.__importUsersFromFile(fileName)



    def __importUsersFromFile(self, fileName):
        importData = Transfer()
        importData.loadFile(fileName)
        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        ui = Ui_importUserWindow(importData, self.__progressBar)
        ui.setupUi(Dialog)
        Dialog.exec_()
        if ui.importPerformed():
            self.usersData = Users()
            self.__displayUsers()

    def __modifyAccount(self):
        if (len(self.accountTable.selectedIndexes()) > 0 and self.accountTable.currentIndex().row() != -1):
            id = int(self.userTable.item(self.userTable.currentIndex().row(), 2).text())
            self.usersData.updateUserBankAccount(id, self.accountTable.currentIndex().row(), self.accountTable.item(self.accountTable.currentIndex().row(), 0).text())

    def __modifyUser(self):
        if (len(self.userTable.selectedIndexes()) > 0 and self.userTable.currentIndex().row() != -1):
            id = int(self.userTable.item(self.userTable.currentIndex().row(), 2).text())
            self.usersData.updateUserData(id, self.userTable.item(self.userTable.currentIndex().row(), 0).text(), self.userTable.item(self.userTable.currentIndex().row(), 1).text())

    def __displayAccounts(self):
        if len(self.userTable.selectedIndexes()) > 0:
            print (self.userTable.item(self.userTable.currentIndex().row(),1).text())
            id = int(self.userTable.item(self.userTable.currentIndex().row(), 2).text())
            self.accountTable.clear()
            for item in self.usersData:
                if (item.id == id):
                    i = 0
                    self.accountTable.setRowCount(len(item.bankAccounts))
                    for number in item.bankAccounts:
                        item = QTableWidgetItem()
                        item.setText(number)
                        self.accountTable.setItem(i, 0, item)
                        i = i + 1
                    break

    def __saveAction(self):
        msg = QMessageBox()
        msg.setText("Zmiany zapisane")
        self.usersData.storeUsedData(self.__progressBar)
        msg.exec_()



    def __init__(self, progressBar):
        self.userWindow = QtWidgets.QWidget()
        self.setupUi(self.userWindow)

        self.__progressBar = progressBar
        self.usersData = Users()
        self.__displayUsers()

        self.userTable.setColumnHidden(2, True)
        self.userTable.itemSelectionChanged.connect(self.__displayAccounts)
        self.userTable.customContextMenuRequested.connect(self.contextMenuUserTable)
        self.userTable.itemChanged.connect(self.__modifyUser)
        self.accountTable.itemChanged.connect(self.__modifyAccount)
        self.accountTable.customContextMenuRequested.connect(self.contextMenuAccountTable)

        self.saveButton.clicked.connect(self.__saveAction)


