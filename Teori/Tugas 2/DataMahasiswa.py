# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataMahasiswa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Form")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 60, 441, 321))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_DataMahasiswa = QtWidgets.QLabel(self.centralwidget)
        self.label_DataMahasiswa.setGeometry(QtCore.QRect(240, 20, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        # Label untuk Text Mahasiswa
        self.label_DataMahasiswa.setFont(font)
        self.label_DataMahasiswa.setObjectName("label_DataMahasiswa")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 530, 320, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Tambah = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.Tambah.setFont(font)

        # Label untuk Text Tambah
        self.Tambah.setObjectName("Tambah")
        self.horizontalLayout.addWidget(self.Tambah)
        self.Edit = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.Edit.setFont(font)

         # Label untuk Text Edit
        self.Edit.setObjectName("Edit")
        self.horizontalLayout.addWidget(self.Edit)
        self.Clear = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.Clear.setFont(font)

         # Label untuk Text Clear
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)
        self.Hapus = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.Hapus.setFont(font)

         # Label untuk Text Hapus
        self.Hapus.setObjectName("Hapus")
        self.horizontalLayout.addWidget(self.Hapus)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(110, 388, 441, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_NoTelp = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.label_NoTelp.setFont(font)

         # Label untuk Text No. Telp
        self.label_NoTelp.setObjectName("label_NoTelp")
        self.gridLayout.addWidget(self.label_NoTelp, 4, 0, 1, 1)
        self.label_Jurusan = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.label_Jurusan.setFont(font)

         # Label untuk Text Jurusan
        self.label_Jurusan.setObjectName("label_Jurusan")
        self.gridLayout.addWidget(self.label_Jurusan, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.label_NIM = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.label_NIM.setFont(font)
        
        # Label untuk Text NIM
        self.label_NIM.setObjectName("label_NIM")
        self.gridLayout.addWidget(self.label_NIM, 0, 0, 1, 1)
        self.label_Nama = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.label_Nama.setFont(font)

        #Label untuk Text Nama
        self.label_Nama.setObjectName("label_Nama")
        self.gridLayout.addWidget(self.label_Nama, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 2, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_DataMahasiswa.setText(_translate("MainWindow", "Data Mahasiswa"))
        self.Tambah.setText(_translate("MainWindow", "TAMBAH"))
        self.Edit.setText(_translate("MainWindow", "EDIT"))
        self.Clear.setText(_translate("MainWindow", "CLEAR"))
        self.Hapus.setText(_translate("MainWindow", "HAPUS"))
        self.label_NoTelp.setText(_translate("MainWindow", "No. Telp"))
        self.label_Jurusan.setText(_translate("MainWindow", "Jurusan"))
        self.label_NIM.setText(_translate("MainWindow", "NIM"))
        self.label_Nama.setText(_translate("MainWindow", "Nama"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

