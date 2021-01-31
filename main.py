# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMdiSubWindow, QFileDialog
import icons_rc
import sys
import Ui_userWindow
import Ui_reportPaymentWindow
import sqlite3
from transfer import Transfer
from progress import Progress

class Ui_MainWindow(Progress):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.userButton = QtWidgets.QToolButton(self.frame)
        self.userButton.setMinimumSize(QtCore.QSize(100, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/img/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton.setIcon(icon)
        self.userButton.setIconSize(QtCore.QSize(65, 65))
        self.userButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.userButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.userButton.setAutoRaise(True)
        self.userButton.setObjectName("userButton")
        self.verticalLayout.addWidget(self.userButton)
        self.importButton = QtWidgets.QToolButton(self.frame)
        self.importButton.setMinimumSize(QtCore.QSize(100, 0))
        self.importButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/img/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importButton.setIcon(icon1)
        self.importButton.setIconSize(QtCore.QSize(65, 65))
        self.importButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.importButton.setAutoRaise(True)
        self.importButton.setObjectName("importButton")
        self.verticalLayout.addWidget(self.importButton)
        self.reportButton = QtWidgets.QToolButton(self.frame)
        self.reportButton.setMinimumSize(QtCore.QSize(100, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/img/schedule.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reportButton.setIcon(icon2)
        self.reportButton.setIconSize(QtCore.QSize(65, 65))
        self.reportButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.reportButton.setAutoRaise(True)
        self.reportButton.setObjectName("reportButton")
        self.verticalLayout.addWidget(self.reportButton)
        self.messageButton = QtWidgets.QToolButton(self.frame)
        self.messageButton.setMinimumSize(QtCore.QSize(100, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/img/phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.messageButton.setIcon(icon3)
        self.messageButton.setIconSize(QtCore.QSize(65, 65))
        self.messageButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.messageButton.setAutoRaise(True)
        self.messageButton.setObjectName("messageButton")
        self.verticalLayout.addWidget(self.messageButton)
        self.settingsButton = QtWidgets.QToolButton(self.frame)
        self.settingsButton.setMinimumSize(QtCore.QSize(100, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon4)
        self.settingsButton.setIconSize(QtCore.QSize(65, 65))
        self.settingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.settingsButton.setAutoRaise(True)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)
        self.exitButton = QtWidgets.QToolButton(self.frame)
        self.exitButton.setMinimumSize(QtCore.QSize(100, 0))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/img/off_mobile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon5)
        self.exitButton.setIconSize(QtCore.QSize(65, 65))
        self.exitButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.exitButton.setAutoRaise(True)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout_2.addWidget(self.mdiArea)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStatusTip("")
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 22))
        self.menubar.setObjectName("menubar")
        self.menuPomoc = QtWidgets.QMenu(self.menubar)
        self.menuPomoc.setObjectName("menuPomoc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionO_programie = QtWidgets.QAction(MainWindow)
        self.actionO_programie.setObjectName("actionO_programie")
        self.menuPomoc.addAction(self.actionO_programie)
        self.menubar.addAction(self.menuPomoc.menuAction())

        self.retranslateUi(MainWindow)
        self.connect()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kartoteka"))
        self.userButton.setText(_translate("MainWindow", "Użytkownicy"))
        self.importButton.setText(_translate("MainWindow", "Importuj dane"))
        self.reportButton.setText(_translate("MainWindow", "Raporty"))
        self.messageButton.setText(_translate("MainWindow", "Wiadomości"))
        self.settingsButton.setText(_translate("MainWindow", "Ustawienia"))
        self.exitButton.setText(_translate("MainWindow", "Zakończ "))
        self.menuPomoc.setTitle(_translate("MainWindow", "Pomoc"))
        self.actionO_programie.setText(_translate("MainWindow", "O programie"))

    def initialize(self, stepsCount):
        """Overrides Progress.initialize"""
        if stepsCount <=0:
            self.progressBar.setValue(0)
        else:
            self.stepProgressBar = 100.0/stepsCount
            self.curentProgressStep = stepsCount
            self.progressBar.setValue(self.curentProgressStep)

    def makeStep(self):
        """Overrides Progress.makeStep"""
        self.progressBar.value()
        self.curentProgressStep = self.curentProgressStep - 1
        if self.curentProgressStep == 0:
            self.progressBar.setValue(100)
        else:
            self.progressBar.setValue(self.progressBar.value() + self.stepProgressBar)

    def connect(self):
        self.userButton.clicked.connect(self.__displayUsers)
        self.exitButton.clicked.connect(self.__exit)
        self.settingsButton.clicked.connect(self.notimplemented)
        self.messageButton.clicked.connect(self.notimplemented)
        self.reportButton.clicked.connect(self.__displayReports)
        self.importButton.clicked.connect(self.__importCSV)
        self.actionO_programie.triggered.connect(self.__about)

    def notimplemented(self):
        msg = QMessageBox()
        msg.setText("Not implemented yet")
        msg.exec_()

    def __init__(self):
        fileExist = False
        self.sub = QMdiSubWindow()
        self.subReport = QMdiSubWindow()
        if os.path.isfile('file.db'):
            fileExist = True
        self.conn = sqlite3.connect('file.db')
        c = self.conn.cursor()

        if not fileExist:
            # Create tables if file doesn't exist
            c.execute('''CREATE TABLE users (userId  INTEGER PRIMARY KEY AUTOINCREMENT, email text, name text, 
            address text, phone text, userFlag INTEGER)''')

            c.execute('''CREATE TABLE accounts
                         (accountId INTEGER PRIMARY KEY AUTOINCREMENT, number text, userId integer)''')

            c.execute('''CREATE TABLE transactions
                         (transactionId text PRIMARY KEY, day date, value integer, title text, userId integer)''')

            c.execute('''CREATE TABLE groupConnector
                         (groupConnectorId INTEGER PRIMARY KEY, userId INTEGER, groupId INTEGER)''')

            c.execute('''CREATE TABLE groups
                         (groupId INTEGER PRIMARY KEY, name text)''')

            c.execute('''CREATE TABLE messages
                         (messageId INTEGER PRIMARY KEY, groupId INTEGER, message text)''')

            c.execute('''CREATE TABLE settings (settingId INTEGER PRIMARY KEY, userNameInFileIdx text, addressInFileIdx 
            text, emailInFileIdx text, phoneInFileIdx text, bankAccountInFileIdx text, transferDateInFileIdx text, 
            titleInFileIdx text, transferValueInFileIdx text)''')

            # Save (commit) the changes
            self.conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.conn.close()

    def __exit(self):
        exit(0)

    def __about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("O programie")
        msg.setText("Kartoteka")
        msg.setInformativeText("Autor : Krzysztof Richert (krzysiek.richert@gmail.com)\n\nProgram może być wykorzystywany w celach komercyjnych przez Pomorski Klub Karate Kyokushin")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def __displayReports(self):
        self.ui_reportWnd = Ui_reportPaymentWindow.Ui_reportPaymentWindow()
        self.subReport.setWidget(self.ui_reportWnd.ret())
        self.subReport.resize(640, 423)
        self.mdiArea.addSubWindow(self.subReport)
        self.subReport.show()

    def __importCSV(self):
        importData = Transfer()

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "CSV Files (*.csv)", options=options)
        if fileName != "":
            importData.loadFile(fileName)
            importData.storeInDB(self)
            msg = QMessageBox()
            msg.setText("Dane zostały zaimportowane. Wymagane odświeżenie raportów.")
            msg.exec_()

    def __displayUsers(self):
        self.ui_userWnd = Ui_userWindow.Ui_userWindow(self)
        self.sub.setWidget(self.ui_userWnd.ret())
        self.sub.resize(640, 423)
        self.mdiArea.addSubWindow(self.sub)
        #self.mdiArea.subWindowActivated.connect(self.handleActivationChange)
        #self.mdiArea.cascadeSubWindows()
        #self.mdiArea.tileSubWindows()
        self.sub.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
