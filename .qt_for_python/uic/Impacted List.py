# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\20212\software\implement\CIMS_project\UI\Impacted List.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImpactedPlaceList(object):
    def setupUi(self, ImpactedPlaceList):
        ImpactedPlaceList.setObjectName("ImpactedPlaceList")
        ImpactedPlaceList.resize(683, 643)
        self.ImpactedPlaceListScroll = QtWidgets.QSlider(ImpactedPlaceList)
        self.ImpactedPlaceListScroll.setGeometry(QtCore.QRect(650, 20, 22, 521))
        self.ImpactedPlaceListScroll.setOrientation(QtCore.Qt.Vertical)
        self.ImpactedPlaceListScroll.setObjectName("ImpactedPlaceListScroll")
        self.textBrowser = QtWidgets.QTextBrowser(ImpactedPlaceList)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 621, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.SearchButton = QtWidgets.QPushButton(ImpactedPlaceList)
        self.SearchButton.setGeometry(QtCore.QRect(530, 560, 131, 61))
        self.SearchButton.setObjectName("SearchButton")

        self.retranslateUi(ImpactedPlaceList)
        QtCore.QMetaObject.connectSlotsByName(ImpactedPlaceList)

    def retranslateUi(self, ImpactedPlaceList):
        _translate = QtCore.QCoreApplication.translate
        ImpactedPlaceList.setWindowTitle(_translate("ImpactedPlaceList", "Impacted Place List"))
        self.SearchButton.setText(_translate("ImpactedPlaceList", "Search"))
