# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesainDial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Masuk_2 = QtWidgets.QPushButton(self.tab)
        self.Masuk_2.setGeometry(QtCore.QRect(170, 220, 75, 23))
        self.Masuk_2.setObjectName("Masuk_2")
        self.Keluar_2 = QtWidgets.QPushButton(self.tab)
        self.Keluar_2.setGeometry(QtCore.QRect(310, 220, 75, 23))
        self.Keluar_2.setObjectName("Keluar_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.dial = QtWidgets.QDial(self.tab_2)
        self.dial.setGeometry(QtCore.QRect(130, 150, 71, 71))
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber.setGeometry(QtCore.QRect(250, 160, 131, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCopy = QtWidgets.QMenu(self.menuFile)
        self.menuCopy.setObjectName("menuCopy")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.ActionNew = QtWidgets.QAction(MainWindow)
        self.ActionNew.setCheckable(True)
        self.ActionNew.setEnabled(True)
        self.ActionNew.setObjectName("ActionNew")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionSebagian = QtWidgets.QAction(MainWindow)
        self.actionSebagian.setObjectName("actionSebagian")
        self.actionSemuanya = QtWidgets.QAction(MainWindow)
        self.actionSemuanya.setObjectName("actionSemuanya")
        self.menuCopy.addAction(self.actionSebagian)
        self.menuCopy.addAction(self.actionSemuanya)
        self.menuFile.addAction(self.ActionNew)
        self.menuFile.addAction(self.menuCopy.menuAction())
        self.menuFile.addAction(self.actionEdit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Masuk_2.setText(_translate("MainWindow", "Masuk"))
        self.Keluar_2.setText(_translate("MainWindow", "Keluar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCopy.setTitle(_translate("MainWindow", "Copy"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.ActionNew.setText(_translate("MainWindow", "New"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionSebagian.setText(_translate("MainWindow", "Sebagian"))
        self.actionSemuanya.setText(_translate("MainWindow", "Semuanya"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

