# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\20212\software\implement\CIMS_project\UI\Reportcheck.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1038, 753)
        self.ContentsTextEdit = QtWidgets.QTextEdit(Dialog)
        self.ContentsTextEdit.setGeometry(QtCore.QRect(150, 250, 811, 381))
        self.ContentsTextEdit.setObjectName("ContentsTextEdit")
        self.ReportButton_2 = QtWidgets.QPushButton(Dialog)
        self.ReportButton_2.setGeometry(QtCore.QRect(840, 640, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ReportButton_2.setFont(font)
        self.ReportButton_2.setObjectName("ReportButton_2")
        self.ReportChechkLabel = QtWidgets.QLabel(Dialog)
        self.ReportChechkLabel.setGeometry(QtCore.QRect(10, 50, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.ReportChechkLabel.setFont(font)
        self.ReportChechkLabel.setObjectName("ReportChechkLabel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.CancleButton = QtWidgets.QPushButton(Dialog)
        self.CancleButton.setGeometry(QtCore.QRect(710, 640, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.CancleButton.setFont(font)
        self.CancleButton.setObjectName("CancleButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(150, 160, 811, 41))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ReportButton_2.setText(_translate("Dialog", "Report"))
        self.ReportChechkLabel.setText(_translate("Dialog", "Report Check"))
        self.label.setText(_translate("Dialog", "Title :"))
        self.CancleButton.setText(_translate("Dialog", "Cancle"))
        self.label_2.setText(_translate("Dialog", "Contents :"))
