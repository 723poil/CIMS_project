# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\20212\software\implement\CIMS_project\UI\AlarmList.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AlarmList(object):
    def setupUi(self, AlarmList):
        AlarmList.setObjectName("AlarmList")
        AlarmList.resize(683, 642)
        self.SearchButton = QtWidgets.QPushButton(AlarmList)
        self.SearchButton.setGeometry(QtCore.QRect(530, 560, 131, 61))
        self.SearchButton.setObjectName("SearchButton")
        self.textBrowser = QtWidgets.QTextBrowser(AlarmList)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 621, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.AlarmListScroll = QtWidgets.QSlider(AlarmList)
        self.AlarmListScroll.setGeometry(QtCore.QRect(650, 20, 22, 521))
        self.AlarmListScroll.setOrientation(QtCore.Qt.Vertical)
        self.AlarmListScroll.setObjectName("AlarmListScroll")

        self.retranslateUi(AlarmList)
        QtCore.QMetaObject.connectSlotsByName(AlarmList)

    def retranslateUi(self, AlarmList):
        _translate = QtCore.QCoreApplication.translate
        AlarmList.setWindowTitle(_translate("AlarmList", "Alarm List"))
        self.SearchButton.setText(_translate("AlarmList", "Search"))
